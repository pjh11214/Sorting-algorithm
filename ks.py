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








import random

# 方法1: 生成指定范围内的随机整数列表
def generate_random_integers(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

# 示例：生成5个范围在1到10之间的随机整数
random_integers = generate_random_integers(7, 1, 1000)
print("随机整数列表:", random_integers)





a=[1,235]
shunxu=">"
def kp(a,shunxu):
    if len(a)<=1:
        return a
    else:
        j=a[0]
        xiao=[x for x in a if x<j]
        dengyu=[x for x in a if x==j]
        da=[x for x in a if x>j]
        if shunxu == "<":
            return kp(xiao,shunxu)+dengyu+kp(da,shunxu)
        elif shunxu == ">":
            return kp(da,shunxu)+dengyu+kp(xiao,shunxu)


print(kp(random_integers,shunxu))




