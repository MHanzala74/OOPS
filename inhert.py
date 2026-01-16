# # Simple Inheritence 

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speaks(self):
#         print(f"{self.name} makes a sound.")

# # Create an instance of Animal 
# animal = Animal("Generic Animal")
# animal.speaks()

# class Dog(Animal):
#     def __init__(self):
#         self.behaviour = "Friendly"
#     def speaks(self):
#         print(f"Buddy barks. He is very {self.behaviour}")

# dog = Dog()
# dog.speaks()

##--> Super Keyword

class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} make a sound.")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks It is a {self.breed}")

dog = Dog("Golden Retriever")
dog.speak()