import hello3
import dog
print(hello3.i)
i = 888
print(i)
current_number = 10
while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

for current_number in range(10, 20):
    if current_number % 2 == 0:
        continue
    print(current_number)
print("=====================================")
def greet_user(username):
    print(f"Hello, {username.title()}!")


greet_user("yang")
greet_user("auto run")

def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    return person


person2 = build_person("yang", "xu")
