def solution(phone_number):
    first = ''.join("*" * (len(phone_number) - 4))
    last = phone_number[-4:]
    return first + last