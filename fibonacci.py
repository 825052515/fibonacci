def fibonacci(n):
    """计算斐波那契数列的前n项"""
    sequence = [0, 1]  # 初始化数列，前两项为0和1

    if n <= 2:
        return sequence[:n]  # 如果n小于等于2，直接返回相应的项

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]  # 计算下一项
        sequence.append(next_number)  # 将下一项添加到数列中

    return sequence

# 示例用法
num_terms = 10
fib_sequence = fibonacci(num_terms)
print("斐波那契数列的前{}项：".format(num_terms))
print(fib_sequence)
