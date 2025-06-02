# This is to show the algorithms of question 17
# Also, 'test_parentheses_match.ipynb' is to test these algorithms


# 栈结构
class Stack:
    def __init__(self):
        self.items = []  # 使用列表存储栈元素

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # 入栈操作

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()  # 出栈操作

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]  # 返回栈顶元素

    def size(self):
        return len(self.items)  # 返回栈的大小
    

# 判断最少需要添加多少括号的函数，输入一个括号序列
def min_add_parentheses(s):
    stack = Stack()
    add_left = 0  # 记录需要添加的左括号数量
    
    for c in s: # 遍历括号序列中的所有括号
        if c in '({[':  # 遇到左括号，直接入栈
            stack.push(c)
        else:  # 遇到右括号
            if not stack.is_empty() and ((c == ')' and stack.peek() == '(') or 
                          (c == '}' and stack.peek() == '{') or 
                          (c == ']' and stack.peek() == '[')):
                stack.pop()  # 栈顶左括号匹配，弹出栈
            else:
                add_left += 1  # 无匹配左括号，需添加add_left
    
    add_right = stack.size()  # 剩余左括号需要右括号匹配
    return add_left + add_right




# 构建添加最少括号后的合法序列
# 这部分与题目关系不大，只是为了测试代码而写的代码
# 即题目是需要我设计算法判断最小需要添加几次括号，而以下的代码是为了展示添加括号后的结果
# 因此没有特别去计较算法复杂度

def build_valid_sequence(s):

    # 第一遍遍历：确定每个右括号前需要添加的左括号
    insert_left = [0] * (len(s) + 1)  # insert_left[i] 表示在位置i之前需要插入的左括号数，为0或者1
    stack = Stack()
    
    for i, c in enumerate(s): # 获得索引i和字符c
        if c in '({[':
            stack.push(c)
        else:
            if not stack.is_empty() and ((c == ')' and stack.peek() == '(') or 
                          (c == '}' and stack.peek() == '{') or 
                          (c == ']' and stack.peek() == '[')):
                stack.pop()  # 栈顶左括号匹配，弹出栈
            else:
                # 不匹配，记录此处需要添加的左括号
                insert_left[i] += 1
    
    # 第二遍遍历：构建最终的合法序列
    result = []
    for i, c in enumerate(s):
        # 添加当前位置需要的左括号
        result.extend(get_matching_left(c) * insert_left[i])
        result.append(c)
    
    # 添加所有剩余的右括号（与栈中剩余的左括号一一匹配）
    while not stack.is_empty():
        left = stack.pop()
        result.append(get_matching_right(left))
    
    return ''.join(result)


# 获取与右括号匹配的左括号
def get_matching_left(right):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return pairs.get(right, '')

# 获取与左括号匹配的右括号
def get_matching_right(left):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    return pairs.get(left, '')

