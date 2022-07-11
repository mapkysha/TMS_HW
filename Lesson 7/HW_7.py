rule = input('Выберете правило раздачи вещей (LIFO или FIFO)')
rule = rule.strip().upper()
items_list = []
while rule:
    with open("d:/TMS_HW/Lesson 7/data.txt", "a+", encoding='utf-8') as file:
        person_item = input('Что у вас?')
        if person_item:
            file.write(f"{person_item}\n\n")
            if rule=='FIFO':
                items_list.insert(0,person_item)
                print('Спасибо!')
            else:
                items_list.append(person_item)
                print('Спасибо!')
        else:
            if len(items_list):
                avaiable_item=items_list.pop()
                print('Возьмите, вот вам', avaiable_item)
            else:
                print('Извните но у нас для вас пока ничего нет, попробуйте зайти позже :(')
else:
    print('Правило раздачи вещей обязательно нужно выбрать!')