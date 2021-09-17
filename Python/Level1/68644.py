def solution(numbers):
    answer = []
    length = len(numbers)

    for i in range(length):
        for j in range(i + 1, length):
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)

    return sorted(answer)