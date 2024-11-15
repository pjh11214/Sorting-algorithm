#计数排序
def counting_sort(arr):
    k = max(arr) + 1
    count = [0] * k
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# 测试代码
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("计数排序结果:", arr)