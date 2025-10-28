class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof! Woof! Woof!"

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    def show_info(self):
        print(f"Dog's Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":
    my_dog = Dog("Ryan", 3)
    print(my_dog.bark())
    my_dog.celebrate_birthday()
    my_dog.show_info()