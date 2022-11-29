txt='''To be successful in a job interview or in almost any interview situation, the applicants houlddemonstrate certain personal and professional qualities.
　　Most likely, the first and often a lasting impression of a person is determined by the clotheshe wears. The job applicant should take care to appear well-groomed and modestly dressed, avoiding the extremes of too pompous or too casual attire .
 succeed in the typical personnel interview.'''
word_a=set()
word2=txt.replace(',',' ').replace('.',' ').replace('?',' ').replace('!',' ')#替换文本中的标点符号
li=word2.split()#split()函数是对字符串进行分割成列表
for i in li:
    word_a.add(i)#遍历字符串添加到集合中利用合集不能有相同元素存在消除

a1=list(word_a)#创建列表
a1.sort(reverse=True)#排序列表
c1=a1[:5:]#索引
for n in c1:
    print(f'单词：{n}\n长度：{len(n)}\n')
    
    
    

