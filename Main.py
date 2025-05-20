class MyClass:
    def __init__(self, value):
        self.__privateVar = value
    def __priVMeth(self):
        print("This is a private method.")
    def hello(self):
        print(f"The value of privateVar is: {self.__privateVar}")
    def callPrivateMethod(self):
        self.__priVMeth
value = int(input("Enter an integer value:"))
obj = MyClass(value)
obj.hello()
obj.callPrivateMethod()