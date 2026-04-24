def calculator(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    elif op=='%':
        return a%b
    else:
        return ("Invalid operator")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
op=input("Enter operator(+,-,*,/,%):")
result=calculator(a,b,op)
print("Result:",result)
