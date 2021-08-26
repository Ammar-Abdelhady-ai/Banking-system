from User_01 import User

class Bank(User):
  
    def __init__(self, Name, age, Gender):
        User.__init__(self, Name, age, Gender)
        self.balance = 0
        self.Password = ""
        self.ID = 0
        
    def deposits(self, Balance):
        self.balance = self.balance + Balance
        print(f"Account New Balance is : {self.balance}")
        
    def withdraw(self, Balance):
        if Balance <= self.balance:
            self.balance = self.balance - Balance
            print(f"Account New Balance is : {self.balance}")
        else:
            print(f"sorry your Account is not enough ; And your Current Balance is : {self.balance}")

    
    def view_balance(self):
        print(f"Account New Balance is : {self.balance}")