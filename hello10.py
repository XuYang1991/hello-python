import os

path = os.environ.get('PATH')
print(path)
print(os.getcwd())

a = 20


def print_te():
    global a
    a = 10
    print(a)


print_te()
print(type({"name": "yang", "age": 30}))

b = {"a", "b", "c"}
b.pop()
print(b)

x = lambda a1, b1: a1 * b1
print(x(5, 6))
i = 0
def increment():
    for var in dir(os):
        global i
        i += 1
        print(str(i) + "_" + var)
increment()
print(i)
x = input("what is your name?")
print(int(x))
print(x)
