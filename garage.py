from random import randint as rand

number_of_cars = 5

brands = [
"BMW",
"Mercedes",
"Toyota",
"Audi",
"Lamborghini",
"Chevrolet",
"Nissan",
"Hyindai",
"Ford",
"Honda"
]

models = [
 ['x5', 'x6', 'm3', 'i8', 'e39'],
 ['GL350', 'SLK', 'Maybach', 'Brabus', 'S600'],
 ['Land Cruiser', 'Supra', 'Highlander', 'Avalon', 'RAV4'],
 ['s6', 'a1', 'a5', 'a7', 'q7'],
 ['SVG', 'Aventador', 'Galardo', 'Hurakan', 'Diablo'],
 ['Aveo', 'Camaro', 'Traverse', 'Lachetti', 'Volt'],
 ['Silvia', 'Rogue', 'Juke', 'GTR', 'Leaf'],
 ['Sonata', 'Santa Fe', 'Elantra', 'i30', 'i20'],
 ['Focus', 'Explorer', 'Expedition', 'Fusion', 'Fiesta'],
 ['CRV', 'Civic', 'CRZ', 'Jazz', 'Accord']
]


# chosen_brands = [rand(0, len(brands)-1) for i in range(number_of_cars)]
# chosen_models = [rand(0, len(models[brand]) -1) for brand in chosen_brands]

S = "I have {} {}"

for i in range(number_of_cars):
 brand = rand(0, len(brands) - 1)
 model = rand(0, len(models[brand]) - 1)
# print(brand, model)
 print(S.format(brands[brand], models[brand][model]))		