import random
num_b=[]
num_a=int(input('请输入调查学生数量：'))
while True:
    num=random.randint(1,1000)
    num_b.append(num)
    if num_a==len(num_b):
        num_b.sort(reverse=True)
        print('随机学号如下：')
        for b in num_b:
            print(f'{b}',end=" ")
        break