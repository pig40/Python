number1=[]

def numbers(*rags):
    sum=0
    for i in rags:
        for b in i:
            sum=sum+b
    print(sum)
number1=[]
for a in range(1,101):
    if a % 2==0:
        number1.append(a)
numbers(number1)