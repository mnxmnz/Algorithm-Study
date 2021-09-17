def solution(n, m):
    min = 0
    answer = []
    
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            min = i
            answer.append(min)
            break;

    max = min * (n // min) * (m // min)
    answer.append(max)

    return answer