def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制排序轮数
    for i in range(n):
        # 内层循环进行相邻元素的比较并交换
        for j in range(0, n-i-1):
            # 如果当前元素大于下一个元素，则进行交换
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试冒泡排序
data = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(data))





def px(a):
    for i in range(len(a)):
        if len(a) <= 1:
            return a
        if i==len(a)-1:
            break
        elif a[i]>a[i+1]:
            b=a[i]
            a[i]=a[i+1]
            a[i+1]=b
    return px(a)


a=[1,68,10]
