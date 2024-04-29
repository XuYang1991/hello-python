class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__private_value = 10

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

if __name__ == '__main__':
    dog = Dog("willie", 6)
    dog.sit()
    dog.roll_over()


dog = Dog("lucy", 3)
dog.sit()
dog.roll_over()
dog.name = "lucy2222"
dog.sit()
dog.roll_over()