can_change_array = [1, 2, 3, 4, 5]
can_not_change_array = (1, 2, 3, 4, 5)
map2 = {"name": "yang", "age": 30}

for value in range(1, 6):
    print(value)

car = "my car"
if car != "my CAR":
    print("Yes, this is my car")
else:
    print("No, this is not my car")

num = 10
if num == -10.0 or num != 101.0:
    print("Yes, this is 10")

flag = True
if flag:
    print("Yes, this is True")

map1 = {"name": "yang", "age": 30}
print(map1.get("name"))

friendA = {"name": "yang", "age": 30}
for key, value in friendA.items():
    print(key + " " + str(value))
friends = [friendA, "regina", "james", "jane", "john"]
print(friends[0].get("name"))