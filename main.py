class Robot:
     # Class variable
    type = "Robot"

    # Constructor
    def __init__(self, name):
        # instance variable
        self.name = name

    # Method
    def display(self):
        print(f"My name is {self.name}")
        print(f"Welcome Back !")

# Create object
Nick = Robot("Nick")
Nick.display()