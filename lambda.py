people = [
    {"name":"Mohamed", "City":"Mogadishu"},
    {"name": "Ali", "City": "Baydhabo"},
    {"name": "NOr", "City": "Borama"}
]

def f(persons):
    return persons["name"]
people.sort(key=f)
print(people)