# 选择排序
# 每次从未排序部分选择最小元素，放置到已排序部分的末尾
def selection_sort(arr):
    n = len(arr)
    for i in range(n):  # 使用索引i来表示未排序区间的第1个元素
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # 找到未排序区间的最小元素的索引min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 将未排序区间的最小元素放在未排序区间的第1个位置，即已排序区间的末尾
    return arr


# 插入排序
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n): 
        key = arr[i] # 使用索引i来表示未排序区间的第1个元素，即需要插入的元素
        j = i - 1
        while j >= 0 and key < arr[j]:  # 不断往前遍历，也就是在已排序区间中往前遍历
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key  # 将需要插入的这个元素插入到正确的位置
    return arr


# 合并排序
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 取中间并区分左子数组和右子数组
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)  # 分别递归排序左子数组和右子数组
        merge_sort(right)
        i = j = k = 0  # i、j、k分别表示左子数组索引、右子数组索引和原数组索引
        # 比较left[i]和right[j]，将较小值放入原数组arr[k]，并移动对应指针（i++或j++），直至某一子数组遍历完毕
        while i < len(left) and j < len(right):  
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 选择基准值
    # 按照基准值进行分区
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # 合并排序后的子数组
    return quick_sort(left) + middle + quick_sort(right)

# 快速排序，改善空间复杂度，递归法
def quick_sort_improve(arr):
    def partition(low, high):
        pivot = arr[low] # 选择基准值，即第一个元素
        i = high + 1 # 右指针，指向最后一个元素
        for j in range(high, low, -1):  # 从右向左遍历
            if arr[j] >= pivot: # 如果当前元素大于或者等于基准值，则将该元素与右指针指向的元素交换，并将右指针向左移动
                i -= 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i-1], arr[low] = arr[low], arr[i-1]  # 结束之后，放置pivot到正确的位置；即基准值左右分别为比基准值小和大的元素
        return i-1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi-1) # 递归排序左子数组和右子数组
            sort(pi+1, high)

    sort(0, len(arr)-1)
    return arr

# 快速排序，使用迭代法
def quick_sort_iter(arr):
    if not arr:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop() # 取出一个待排序的子数组范围
        if low < high:
            # 分区函数与递归法相同，使用指针原地分区
            pivot = arr[low]
            i = high + 1
            for j in range(high, low, -1):
                if arr[j] >= pivot:
                    i -= 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i-1], arr[low] = arr[low], arr[i-1]
            pi = i - 1
            # 注意栈的LIFO特性，先压入右子数组，确保左子数组优先被处理
            stack.append((pi + 1, high))
            stack.append((low, pi - 1))
    return arr



# 基数排序
def radix_sort(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num # 找到数组中的最大值，然后确定其位数

    # 处理负数（将所有数转换为非负数）
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num # 找到数组中的最小值
    offset = 0
    if min_num < 0:
        offset = -min_num
        arr = [num + offset for num in arr]
        max_num += offset  # 更新最大值

    # 基数排序主逻辑
    exp = 1
    while max_num // exp > 0:
        # 初始化10个链表
        buckets = [[] for _ in range(10)]
        # 按当前位的数值将元素放入对应链表中
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        # 按链表的顺序收集元素，覆盖原数组
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        # 处理下一位
        exp *= 10
    
    # 恢复负数（如果有）
    if offset != 0:
        arr = [num - offset for num in arr]
    
    return arr


# 希尔排序
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# 随机化快速排序
import random
random.seed(30)
def randomized_sort(arr):
    if not arr:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            # 随机选择基准值并交换到low位置
            pivot_idx = random.randint(low, high)
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
            # 分区逻辑与快速排序相同
            pivot = arr[low]
            i = high + 1
            for j in range(high, low, -1):
                if arr[j] >= pivot:
                    i -= 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i-1], arr[low] = arr[low], arr[i-1]
            pi = i - 1
            # 保持快速排序的栈操作顺序
            stack.append((pi + 1, high))
            stack.append((low, pi - 1))
    return arr