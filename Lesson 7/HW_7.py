import json

rule = input('Выберете правило раздачи вещей (LIFO или FIFO)')
rule = rule.strip().upper()
items_list = []
items_list_2 = []
while rule:
        person_item = input('Что у вас?')
        if person_item:
            amount_preson_item = input('Сколько')
            with open("d:/TMS_HW/Lesson 7/data.json", "w", encoding='utf-8') as file:
                if rule=='FIFO':
                    items_list.insert(0, {'fork': person_item, 'amount': amount_preson_item})
                    items_list_2.insert(0, {'fork': person_item, 'amount': amount_preson_item})
                    print('Спасибо!')
                else:
                    items_list.append({'fork': person_item, 'amount': amount_preson_item})
                    items_list_2.append({'fork': person_item, 'amount': amount_preson_item})
                    print('Спасибо!')
                json.dump(items_list, file, ensure_ascii=False)
        else:
            if len(items_list_2):
                avaiable_item=items_list_2.pop()
                print('Возьмите, вот вам', avaiable_item['fork'], avaiable_item['amount'], 'шт')
            else:
                print('Извните но у нас для вас пока ничего нет, попробуйте зайти позже :(')
else:
    print('Правило раздачи вещей обязательно нужно выбрать!')