def add1(x,y):
    return x+y
def add2(x,y):
    return x-y
def add3(x,y):
    return x*y
def add4(x,y):
    return x/y
x=float(input("请输入第一个数:"))
y=float(input("请输入第二个数:"))
z=input("""请输入运算方式 1.加法 2.减法 3.乘法 4.除法:
""")
if z=="1":
    print(f"{x}+{y}={add1(x,y)}")
elif z=="2":
     print(f"{x}-{y}={add2(x,y)}")
elif z=="3":
     print(f"{x}*{y}={add3(x,y)}")
elif z=="4":
     print(f"{x}/{y}={add4(x,y)}")
else:
    print("输入错误，请输入运算方式")


