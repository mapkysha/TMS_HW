rule = input('Выберете правило раздачи вещей (LIFO или FIFO)')
rule = rule.strip().upper()
items_list = []
while rule:
    person_item = input('Что у вас?')
    if person_item:
        if rule=='FIFO':
            items_list.insert(0,person_item)
            print('Спасибо!')
        elif rule == 'LIFO':
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