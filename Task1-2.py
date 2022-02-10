

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
                ingredient['quantity'] = ingr_strip[1]
                ingredient['measure'] = ingr_strip[2]
                ingr_list.append(ingredient)
            cook_book[new_recipe_name] = ingr_list
            rec_file.readline()
        return cook_book

cook_book = make_cook_book()

print(cook_book)
