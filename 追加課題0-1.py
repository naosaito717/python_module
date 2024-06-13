# Input例
numbers = [1,2,3,4,6,7,8,0]
def solution(numbers):
    total = 0
    for num in range(10):
        if num in numbers:
            continue
        else:
            total += num
    return(total)

print(solution(numbers))




