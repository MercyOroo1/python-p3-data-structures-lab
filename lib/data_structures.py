spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    pass
# print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]> 5]
    pass
# print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name" ,"Not Available")
        heat_level = food.get("heat_level", "0")
        chillies = "🌶" * heat_level
        cuisine = food.get("cuisine", "Not Available")
        print (f"{name} ({cuisine}) | Heat Level: {chillies}")
    pass
print (print_spicy_foods(spicy_foods))
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    return None
    pass
# print (get_spicy_food_by_cuisine (spicy_foods,"American"))
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

    pass
print ( print_spiciest_foods (spicy_foods))

def get_average_heat_level(spicy_foods):
    total = 0
    number = len(spicy_foods)

    for food in spicy_foods:
        heat_level= food.get("heat_level","0")
        total += heat_level
    average = total/number
    return average
    pass
print (get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
print (create_spicy_food (spicy_foods, 
         {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }))