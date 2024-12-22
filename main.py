class IOString():
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("enter String :  ")
    def print_String(self):
            print("result is :", self.str1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()
class Employee:
     def __init__(self):
          print('employee created')
     def __del__(self):
          print("Destructor called")
def create_obj():
     print('making object...')
     obj = Employee()
     print('function end...')
     return obj
print('Calling Create_obj() function...')
obj = create_obj()
print('Program end')