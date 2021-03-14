# 快速排序 
# 分裂函数partition
def quicksort(list):
    if len(list)>1:
        left=1
        right=len(list)-1
        right=partition(list,left,right)
        list[:right]=quicksort(list[:right])
        list[right+1:]=quicksort(list[right+1:])
    return list
def partition(list,left,right):
    mid=list[0]
    done=False
    while not done:
        while list[left]<mid and left<len(list)-1:
            left+=1
        while list[right]>mid and right>=1:
            right-=1
        if left>=right:
            done=True
        else:
            temp=list[left]
            list[left]=list[right]
            list[right]=temp    
    tmp=list[right]
    list[right]=mid
    list[0]=tmp
    return right
alist=[3,66,2,1,67,88,76,55,35,67,43,99,6,0]
print(quicksort(alist))