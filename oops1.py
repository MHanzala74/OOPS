# Initiate a class 
class employee:
    # special method | magic method | dunder method -> constructor 
    def __init__(self):
        print(id(self))
        # print("Starting executing attribute|data")
        self.id = 123
        self.salary = 500000
        self.designation = "SDE"
        # print("attribute|data have been initiated")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")


sam = employee()
# print(id(sam))
sam.name = "Ahmad"
print(sam.name)

# printing the attributes
# print(sam.id)

# Calling the methods 
# sam.travel("Islamabad")