n = 12
def solution(n):
    for num in range(1,1000000):
        if n%num == 1:
            break
    return(num)

print(solution(n))

 

