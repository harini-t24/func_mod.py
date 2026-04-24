def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(fibonacci(i),end=" ")
