import random #импортируем библиотеку для случайного выбора элемента списка

cocktails = [
    ["мартини","грейпфрутовый сок","жасмин","тоник","лосось"],
    ["клубника","какао","мята","марсала"],
    ["водка","томатный сок","лимонный сок","вустерширский соус","черный перец","сельдерей","лосось"],
    ["джин","вермут","ликер мараскино","апельсины","коктейльная вишня","лосось"],
    ["ром","авокадо","сахарный сироп","сливки","лимонный сок","лед"],
    ["красный вермут","тоник","апельсины","лосось"],
    ["только чай"]
]
for i in range(len(cocktails)): #проходимся по списку коктейлей 
    for j in range(len(cocktails[i])): #проходимся по списку ингредиентов коктейля
        if cocktails[i][j] == 'лосось': 
            cocktails[i].pop(j) #удаляем элемент

tCocktail = random.choice(cocktails) #метод choice библиотеки random позволяет выбрать случайный элемент списка
print('Для коктейля вам понадобится:')
for i in range(len(tCocktail)):
    print(tCocktail[i])
