

def make_cook_book(recipe_file_name="recipes.txt"):
    cook_book = {}
    with open(recipe_file_name) as rec_file:
        while True:
            new_recipe_name = rec_file.readline().strip()
            if not new_recipe_name: break
            ingr_count = int(rec_file.readline())
            ingr_list = []
            for i in range(ingr_count):
                ingredient = {}
                ingr_string = rec_file.readline()
                ingr_strip = [x.strip() for x in ingr_string.split("|")]
                ingredient['ingredient_name'] = ingr_strip[0]
                ingredient['quantity'] = int(ingr_strip[1])
                ingredient['measure'] = ingr_strip[2]
                ingr_list.append(ingredient)
            cook_book[new_recipe_name] = ingr_list
            rec_file.readline() #Пропуск пустой строки
        return cook_book

my_cook_book = make_cook_book()

print(my_cook_book)


def get_shop_list_by_dishes(dishes, person_count=1, cook_book=my_cook_book):
    shop_list ={}
    for dish in dishes:
        ingr_list = cook_book[dish]
        for ingr in ingr_list:
            ingr_name = ingr['ingredient_name']
            if ingr_name in shop_list.keys():
                shop_list[ingr_name]['quantity'] += ingr['quantity']
            else:
                shop_list[ingr_name] = {"measure":ingr['measure'], "quantity": ingr['quantity']}
    if person_count > 1: #Чтобы зря не гонять цикл с умножением на 1
        for ingr_name in shop_list.keys():
            shop_list[ingr_name]["quantity"] *= person_count
    return shop_list


test_shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(test_shop_list)


breakfast_shop_list = get_shop_list_by_dishes(["Омлет", "Запеченный картофель" , "Омлет"], 2)
print(breakfast_shop_list)


single_dinner_shop_list = get_shop_list_by_dishes(["Фахитос"], 1)
print(single_dinner_shop_list)