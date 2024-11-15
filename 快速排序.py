def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
        left = [x for x in arr if x < pivot]  # 小于基准的元素
        middle = [x for x in arr if x == pivot]  # 等于基准的元素
        right = [x for x in arr if x > pivot]  # 大于基准的元素
        return quicksort(left) + middle + quicksort(right)  # 递归排序并合并

# 示例使用
array = [10, 5, 2, 3, 8, 6, 7, 4, 9, 1]
sorted_array = quicksort(array)
print(sorted_array)

