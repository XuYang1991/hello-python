






print("hello python")
message = 'hello" world'
print(message.title())
print(message.upper())
print("Hi Regina,\n\t\tHow are you doing today?")


print(2 + 3.6)

print("happy " + str(23) + " birthday")
# this is a test
print(3 / 2.0)

days = [10, "today", 20, "tomorrow"]
print(days.count(10))
days[0] = 20
print(days)
print(days.count(20))
days.append(30)
print(days)
days.insert(1, "yesterday")
print(days)
print(days.remove("today"))
print(days)
print(days.pop(2))
print(days)

array = [6, 2, 3, 4, 5]
#array.sort()
print(sorted(array))
print(array)

print(len(array))

for day in days:
    print(day)

for value in sorted(array):
    print(value)
print("=====================================")
array2 = range(1, 6)

can_not_change = (1, 2, 3, 4, 5)
print(can_not_change)
can_not_change = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "hello", "world", "today", "tomorrow", "yesterday", "now", "then", "later", "soon, never", "tttttttttttttttttttttttttttttttttttttttttttttttttt")
print(can_not_change)
