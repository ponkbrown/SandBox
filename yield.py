def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstny(n):
    num = 0
    while num < n:
        yield num
        num += 1

