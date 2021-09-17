def solution(a, b):
    weekday = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    sum = 0
    
    for i in range(a-1):
        sum += month[i]
    
    sum += b
    
    num = sum % 7
    
    return weekday[num]