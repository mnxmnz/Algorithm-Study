def solution(arr):
    answer = []
    
    if len(arr) == 1:
        return [-1]
    
    num = arr[0]
    
    for text in arr[1:]:
        if text < num:
            num = text
            
    for text in arr:
        if text != num:
            answer.append(text)
            
    return answer