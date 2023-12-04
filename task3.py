postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}

postcards["Petra"] = "Paris" #добавили
postcards["Ivan"] = "Moscow" #добавили
postcards["Oleg"] = "Sydney" #исправили (открытка олега из сиднея)

unique_cities = len(set(postcards.values())) #выводим уникальные города
print('На самом деле в коллекции Алисы ', unique_cities, ' уникальных городов')
print('Вот они: ', set(postcards.values()))