ls=["张三","张三","李四","王五","张三","李四","赵六","李四","张三","王五","张三","王五","李四","李四","李四","赵六","张三","张三","李四","张三"]
ls_keys={}

for a in ls:
    if a in ls_keys:
        ls_keys[a]+=1
    else:
        ls_keys[a]=1
for a1 in ls_keys.items():
    print(a1)
