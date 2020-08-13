def x(n):
    if n == 1:
        return 1
    return n*x(n-1)
    
print(x(5))

