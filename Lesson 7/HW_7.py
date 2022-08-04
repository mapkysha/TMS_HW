import sqlite3

connect = sqlite3.connect('d:/TMS_HW/Lesson 7/donat_items.db')
cur = connect.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY AUTOINCREMENT,Name, Amount, Stoc DEFAULT Минск_Восточный,TIME datetime DEFAULT CURRENT_TIMESTAMP, Rule);
            """)
connect.commit()

def tuple_converter (data):
    return tuple(str(data).split(','))

rule = input('Выберете правило раздачи вещей (LIFO или FIFO)')
rule = rule.strip().upper()
items_list = []
while rule:
        person_item = input('Что у вас?')
        if person_item:
            amount_preson_item = int(input('Сколько?'))
            tuple_package_for_db = tuple_converter(person_item) + tuple_converter(amount_preson_item) + tuple_converter(rule)
            if rule == 'FIFO':
                items_list.insert(0, {'fork': person_item, 'amount': amount_preson_item})
                print('Спасибо!')
            else:
                items_list.append({'fork': person_item, 'amount': amount_preson_item})
                print('Спасибо!')
            cur.execute("INSERT INTO items (Name,Amount,Rule) VALUES(?,?,?);", tuple_package_for_db)
            connect.commit()
        else:
            if len(items_list):
                last_package = items_list[(len(items_list)) - 1]
                if last_package['amount'] == 1:
                    avaiable_package=items_list.pop()
                    print(f"Возьмите, вот вам {avaiable_package['fork']} {avaiable_package['amount']}(шт)")
                else:
                    last_package['amount'] -= 1
                    print("Возьмите вот вам:", last_package['fork'], "1(шт)")
            else:
                print('Извните но у нас для вас пока ничего нет, попробуйте зайти позже :(')
else:
    print('Правило раздачи вещей обязательно нужно выбрать!')