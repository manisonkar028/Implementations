# # #creating Class 
# # class Student:
# #     #Methods
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
        
# #     def average(self):
# #         sum=0
# #         for val in self.marks:
# #             sum+=val
# #         print("Hi",self.name, "Your Average=",sum/3)
# # #objects  for 3 students adn their respective marks      
# # s1= Student("karan",[97,98,95])
# # s1.average()
    
# # s2=Student("arjun",[87,85,91])
# # s2.average()

# # s3=Student("thor",[90,89,95])
# # s3.average()

# #ABSTRACTION
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
        
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("Car Started")
        
# c1=Car()
# c1.start()
        
#Encapsulation

#example- create Account class with 2 attributes - balance & account no.
# Create method for debit,credit&printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.acc_no=acc
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited.")
        print("Total balance=",self.get_balance())
    #credit method    
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited.")
        print("Total balance=",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Account(10000,67891)
acc1.debit(1000)
acc1.credit(5000)
acc1.credit(10000)

