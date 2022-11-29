# 请输入一个整数，作为一维向量的长度
n = eval(input("输入一个整数："))
# 请输入n个整数，以英文逗号隔开
x = input('x请输入n个整数用英文逗号隔开：')
# 请输入n个整数，以英文逗号隔开
y = input('y请输入n个整数用英文逗号隔开：')

list_x = x.split(",")
list_y = y.split(",")

sum = 0
for i in range(n):
    sum += eval(list_x[i] + "*" + list_y[i])

print("x 和 y 的内积是：{}".format(sum))