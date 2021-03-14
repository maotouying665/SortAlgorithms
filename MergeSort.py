# 归并排序，体现分治的思想
# 分裂和归并
# 切片操作可读性强，但是会增加时间复杂度，不必要
# 使用了多一倍的存储空间用于归并，特大的数据集要注意一下
def mergesort(list):
    if len(list)>1:
        left=list[:len(list)//2]  # python的切片操作
        right=list[len(list)//2:]
        left=mergesort(left)
        right=mergesort(right)
        list=merge(left,right)
    return list
def merge(l,r):
    i=0
    j=0
    list=[]
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            list.append(l[i])
            i+=1
        else:
            list.append(r[j])
            j+=1
    if i<len(l):
        t=i
        while t<len(l):
            list.append(l[t])
            t+=1
    else:
        t=j
        while t<len(r):
            list.append(r[t])
            t+=1
    return list
alist=[3,66,2,1,67,88,76,55,35,67]
print(mergesort(alist))