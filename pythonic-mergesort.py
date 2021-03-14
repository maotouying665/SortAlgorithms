# 更具有python风格的归并排序代码，具有更强的可读性
# 分裂和归并
# 切片操作可读性强，但是会增加时间复杂度，不必要
# 使用了多一倍的存储空间用于归并，特大的数据集要注意一下
def mergesort(list):
    if len(list)>1:
        left=list[:len(list)//2]
        right=list[len(list)//2:]
        left=mergesort(left)
        right=mergesort(right)
        list=merge(left,right)
    return list
def merge(left,right):
    merged=[]
    while left and right:
        if left[0]<right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged
alist=[3,66,2,1,67,88,76,55,35,67]
print(mergesort(alist))