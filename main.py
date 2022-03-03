from collections import Counter

def shopping_list_2_1()->list:
    '''возвращает список введенных покупок'''
    shopping = []
    count = 1
    thing = input('enter thing № {}: '.format(count))
    while (thing != ''):
        shopping.append(thing)
        count += 1
        thing = input('enter thing № {}: '.format(count))
    return shopping

def shopping_list_2_2():
    '''выводит список с суммарным кол-вом каждого товара,
    возвращает словарь без наиболее популярного товара'''
    my_shopping = shopping_list_2_1()
    num_of_thing = {i: my_shopping.count(i) for i in my_shopping}
    popular = max(num_of_thing.values())
    print(num_of_thing)
    print(popular)
    for k, v in num_of_thing.items():
        if v == popular:
            print('******')
            key_for_del = k
    del num_of_thing[key_for_del]
    print(num_of_thing)
    print('the most popular thing: ', popular, '\nand we remoted it :)')
    return num_of_thing

shopping_list_2_2()