# 在插入排序的基础上改变增量，从n//2到1，逐步减小，
# 因为插入排序时，原本的序列越有序效率越高，时间复杂度越低
def shellsort(list):
    m=len(list)
    while m>1:
        m=m//2
        list=gapinsertsort(list,m)
    return list
def gapinsertsort(list,n):
    for q in range(n):
        for index in range(q+n,len(list),n):
            a=list[index]
            i=index
            while i>=n:
                if a<list[i-n]:
                    list[i]=list[i-n]
                else:
                    break
                i-=n
            list[i]=a
    return list
alist=[3,66,2,1,67,88,76,55,35,67,43]
print(shellsort(alist))