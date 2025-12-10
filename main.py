class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email
        
    def set_password(self, password):
        self.__password = password
        
user = User('Юрий', 'user123@gmail.com', 'Password1234')
print(f'User name: {user.get_name()}')
print(f'User email: {user.get_email()}')
print(f'User password: {user.get_password()}')

user.set_name('Иван')
print(f'New user name: {user.get_name()}')                   


class Shape:
    def __init__(self):
        pass
    
    def calculate_area():
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
         return 3.14 * self.radius * self.radius   
        
class Rectangle(Shape):
    def __init__(self, width, height):
       self.width = width
       self.height = height 
       
    def calculate_area(self):
           return self.width * self.height
        
class Triangle(Shape):
    def __init__(self, height, base):
       self.height = height
       self.base = base 
       
    def calculate_area(self):
       return self.height * self.base / 2
   

circle = Circle(4)
print(f'circle area: {circle.calculate_area()}')

rectangle = Rectangle(3,8)
print(f'rectangle area: {rectangle.calculate_area()}')

triangle = Triangle(4,9)
print(f'triangle area: {triangle.calculate_area()}')     