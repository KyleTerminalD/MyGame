from grid import Grid
import json


test = Grid(5, 5, 3)

print(str(test))

with open('jason.json', 'w') as js:

    test.resize(20, 20)
    json.dump(test.__dict__(), js)
    print(test)

with open('jason.json', "r") as js:
    test2 = Grid(json_rebuild=json.load(js))
    print(test2)

test.resize(5, 5)
print(test)
print(test == test2)
