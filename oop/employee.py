class Employee:
    def __init__(self,name,salary,phone,e_mail):
        self.name = name
        self.salary = salary
        self.phone = phone
        self.e_mail = e_mail
    
    def display(self):
        print("Name: ",self.name)
        print("salary:",self.salary)
        print("phone:",self.phone)
        print("e_mail:",self.e_mail)



e = Employee("Pallavi Mohite",90000,9322711696,"mohitepallavi99@gmail.com")
e.display()