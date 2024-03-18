# most code commented out will is either a function call or will work and pass 
# tests, however, it is not the most concise, and the uncommented code is the 
# more Python or 'Pythonista' way of thinking

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

# spicy_food dict is only for the last function
spicy_food = {
        "name": "Griot",
        "cuisine": "Haitian",
        "heat_level": 10,
    }

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods if True ]
    # names = []
    # for n in range (len(spicy_foods)):
    #     names.append(spicy_foods[n]["name"])
    # return names
    # 4 lines above commented out as they work, but the single line above does the same

# print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    # spiciest_foods = []
    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         spiciest_foods.append(food)
    # return spiciest_foods

# print(get_spiciest_foods(spicy_foods))  

def print_spicy_foods(spicy_foods):
    all_cuisines = ""
    for food in spicy_foods:
        chilis = " | " + "Heat Level:" + " " + (food["heat_level"])*"🌶"+ "\n"
        cuisine_type = " (" + food["cuisine"] + ")"
        all_cuisines = all_cuisines + food["name"] + cuisine_type + chilis
    print(all_cuisines.strip("\n"))

    # all_cuisines = ""
    # for n in range (len(spicy_foods)):
    #     chilis = " | " + "Heat Level:" + " " + (spicy_foods[n]["heat_level"])*"🌶"+ "\n"
    #     cuisine_type = " (" + spicy_foods[n]["cuisine"] + ")"
    #     all_cuisines = all_cuisines + spicy_foods[n]["name"] + cuisine_type + chilis
    # print(all_cuisines.strip("\n"))
    # return(all_cuisines.strip("\n"))

# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
     
    # spicy_food_by_cuisine = {}
    # for n in range (len(spicy_foods)):
    #     if spicy_foods[n]["cuisine"] == cuisine:
    #         spicy_food_by_cuisine = spicy_foods[n]
    # return spicy_food_by_cuisine

# print (get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    most_spicy_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            most_spicy_foods.append(food)
    print_spicy_foods(most_spicy_foods)        

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = 0
    ave_heat = 0
    for food in spicy_foods:
        total_heat = total_heat + food["heat_level"]
    ave_heat = total_heat/len(spicy_foods)
    return int(ave_heat)

# print(get_average_heat_level(spicy_foods))   

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return (spicy_foods)

# create_spicy_food(spicy_foods, spicy_food)
