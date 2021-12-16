def sqrt():
    x=int(input())
    b=x 
    for i in range(10):
        x=0.5*(x+b/x)
    print("Square root of the number:",x)
sqrt()