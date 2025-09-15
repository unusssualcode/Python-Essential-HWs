# task1
#
# def reversed_generator(list):
#     for i in range(len(list) - 1, -1, -1):
#         yield list[i]
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for num in reversed_generator(nums):
#     print(num)

# task2

# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# squares=[x**2 for x in numbers if x % 2 == 0]
# print(squares)


# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# squares=[]
#
# for num in numbers:
#     if num%2==0:
#         squares.append(num**2)
#
# print(squares)

# task3

def prime_nums(n):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5)+1):
            if k % i == 0:
                return False
        return True
    count = 0
    num=2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

for ns in prime_nums(10):
    print(ns)


