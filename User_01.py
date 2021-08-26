class User:
    def __init__(self, Name, Age, Gender):
        self.name = Name
        self.age = Age
        self.gender = Gender
        
    def show_user_details(self):
        print(f"your Name is : {self.name}")
        print(f"your Phone namber is : {self.age}")
        print(f"your Gender is : {self.gender}")