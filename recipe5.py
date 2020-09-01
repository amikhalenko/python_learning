from pprint import pprint

def cook_book():
    with open('files/recipes.txt', 'r', encoding='utf-8-sig') as f:
        onstring = f.read().split('\n')
        cook_book = {}
        value = {}
        values = []

        for item in onstring:
           for item in onstring:
            if "|" not in item:
                try:
                    xyz = int(item)
                except ValueError:
                    if len(item) > 0:
                        key = item
                        values = []
            elif xyz > -1:
                value = {}
                subonstring = item.split('|')
                value['ingredient_name'] = subonstring[0]
                value['quantity'] = subonstring[1] 
                value['measure'] = subonstring[2]
                values.append(value)
                xyz -= 1
                if xyz > -1:
                    continue

            cook_book[key] = values
            value = {}
    from pprint import pprint
    pprint(cook_book)        
    return cook_book
cook_book()
def get_shop_list_by_dishes(dishes, person_count):
    cook_book_copy = cook_book() 
    ready_cook_book = {} 
    for item in dishes:
        for values in cook_book_copy[item]:
            if values['ingredient_name'] in ready_cook_book.keys():
                for key, value in ready_cook_book[values['ingredient_name']].items():
                    if key == 'quantity':
                        ready_cook_book[values['ingredient_name']] = {'quantity': int(values['quantity']) * person_count + int(value), 'measure': values['measure']} 
            else:
                ready_cook_book[values['ingredient_name']] = {'quantity': int(values['quantity']) * person_count, 'measure': values['measure']}

    pprint(ready_cook_book)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)