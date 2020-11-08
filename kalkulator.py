def calculator(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op =='*':
        return a*b
    elif op == '/':
        return a/b
    return 0

if __name__=="__main__":
    c=calculator(1, 2, '+')
    print(c)
    d=calculator(10, 200, '-')
    print(d)
    e=calculator(3, 5, '*')
    print(e)
    print(type(e))
    f=calculator(50, 2, '/')
    print(f)
    print(type(f))
