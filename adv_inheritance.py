# Single or Basic Inheritence 
# class Parent:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print(f"Hello, My name is {self.name}")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# obj = Child("Alice")
# obj.greet()
# obj.play()

# ------------------------------------------------------
# Multilevel Inheritance 

# class GrandParent:
#     def __init__(self,name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tell a story")

# class Parent(GrandParent):
#     def work(self):
#         print(f"{self.name} is working")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# obj = Child("Charlie")
# obj.tell_story()
# obj.work()
# obj.play()

# ------------------------------------------------------------------
# Hierarchical Inheritance 
class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, My name is {self.name}")

class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing")

class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying")

ch1 = Child1("Alice")
ch2 = Child2("Era")

ch1.greet()
ch1.play()

ch2.greet()
ch2.study()