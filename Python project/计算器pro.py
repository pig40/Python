def add1(x,y):
    return x+y
def add2(x,y):
    return x-y
def add3(x,y):
    return x*y
def add4(x,y):
    return x/y
num=input("请输入:")
if "+" in num:
    a=num.split("+")
    x=float(a[0])
    y=float(a[1])
    print(add1(x,y))
if "-" in num:
    a=num.split("-")
    x=float(a[0])
    y=float(a[1])
    print(add2(x,y))
if "*" in num:
    a=num.split("*")
    x=float(a[0])
    y=float(a[1])
    print(add3(x,y))
if "/" in num:
    a=num.split("/")
    x=float(a[0])
    y=float(a[1])
    print(add4(x,y))