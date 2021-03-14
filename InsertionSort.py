# 插入排序
# 移动和插入
def insertsort(list):
    for index in range(1, len(list)):
        a=list[index]
        i=index
        while i>=1:
            if a<list[i-1]:
                list[i]=list[i-1]
            else:
                break
            i-=1    
        list[i]=a
    return list
alist=[3,66,2,1,67,88,76,55,35,67,43]
print(insertsort(alist))




