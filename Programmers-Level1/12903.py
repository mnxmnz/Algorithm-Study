def solution(s):
    result = []
    length = int(len(s) / 2)

    if len(s) % 2 == 0:
        result.append(s[length - 1])
        result.append(s[length])
    else:
        result.append(s[length])

    answer = ''.join(result)

    return answer