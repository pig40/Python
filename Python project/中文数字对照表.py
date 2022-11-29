numbers = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
number=input("输入一个数字:")
for i in number:
    print(numbers[int(i)],end="")

