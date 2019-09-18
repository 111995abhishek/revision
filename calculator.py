def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("enter choice:")
print("1. add")
print("2. sub")
print("3. multiply")
print("4. divide")

choice=int(input("enter choice"))

if choice=='1':
    print("result of addition is: ",add(num1,num2))
elif choice=='2':
    print("result of substraction is",substract(num1,num2))
elif choice=='3':
    print("result of multiplication is",multiply(num1,num2))
elif choice=='4':
    print("result of division is",divide(num1,num2))
else:
    print("invalid input")
