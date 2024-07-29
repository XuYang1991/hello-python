my_dict = {"a": 1}
print(my_dict.get("b"))

if my_dict.get("b"):
   print("contain")
else:
    print("no")

a = None
print(a is None)