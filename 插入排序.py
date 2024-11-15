def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 将 arr[j] 大于 key 的所有元素向右移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 测试代码
arr = [5, 2, 9, 1, 5, 6]
insertion_sort(arr)
print(arr)  # 输出: [1, 2, 5, 5, 6, 9]