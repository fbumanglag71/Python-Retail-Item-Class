class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    pet = Pet()

    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of your pet: ")
    age = int(input("Enter the age of your pet: "))

    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    print("Pet Information:")
    print("Name:", pet.get_name())
    print("Animal Type:", pet.get_animal_type())
    print("Age:", pet.get_age())


main()



