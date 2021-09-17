def solution(arr, divisor):
    count = 0
    answer = []

    for n in arr:
        if n % divisor == 0:
            answer.append(n)
            count += 1

    if count == 0:
        answer.append(-1)

    return sorted(answer)