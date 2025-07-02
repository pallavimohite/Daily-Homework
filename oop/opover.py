class Book:
    def __init__(self,name,pages,price,):
        self.name  = name
        self.pages = pages 
        self.price = price

    def __add__(self,other):
        name = self.name + other.name
        Total_Pages = self.pages + other.pages
        Total_Price = self.price + other.price
        return Book(name,Total_Pages,Total_Price)
    
    
    def __sub__(self,other):
        #Sum_of_name = self.name - other.name      #Unsupported operand type 'str' and 'str'
        name = self.name                            #Keep name of first book to avoid error
        Remaning_Pages = self.pages - other.pages
        Remaning_Price = self.price - other.price
        return Book(name,Remaning_Pages,Remaning_Price)
    
    
    def __mul__(self,other):
        name = self.name 
        Multiplied_Pages = self.pages * other.pages
        Multiplied_Price = self.price * other.price
        return Book(name,Multiplied_Pages,Multiplied_Price)
    
    
    
    def __truediv__(self,other):
        name = self.name 
        T_Pages = self.pages / other.pages
        T_Price = self.price/ other.price
        return Book(name,T_Pages,T_Price)
    
    
    
    def __floordiv__(self,other):
        name = self.name 
        T_Pages = self.pages // other.pages
        T_Price = self.price// other.price
        return Book(name,T_Pages,T_Price)
    
    
    
    def __mod__(self,other):
        name = self.name 
        T_Pages = self.pages % other.pages
        T_Price = self.price% other.price
        return Book(name,T_Pages,T_Price)
    
    
    
    def __gt__(self,other):
        name = self.name 
        T_Pages = self.pages > other.pages
        T_Price = self.price > other.price
        return Book(name,T_Pages,T_Price)
    
    def __eq__(self,other):
        return self.price == other.price
    
    def __ne__(self,other):
        return self.price != other.price
         
    
    

    def __str__(self):
        return f"Book Name : {self.name} ,Book Pages:{self.pages}, Total Price:{self.price}"
    
    

b1 = Book("Harry_Potter ,",10,20)
b2 = Book("Sherloc_Homes ,",5,10)
b3 = Book("Ikigai",2,4)
print(b1+b2+b3)
print(b1-b2-b3)
print(b1*b2*b3)
print(b1/b2/b3)
print(b1//b2//b3)
print(b1%b2%b3)
print(b1>b2>b3)
print("Price of b1 is equal to b2:",b1==b2)
print("Price of b1 is not equal to b2:",b1!=b2)

