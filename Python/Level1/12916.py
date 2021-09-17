def solution(s):
    pcnt = 0
    ycnt = 0
    
    for text in s.lower():
        if text == 'p':
            pcnt += 1
        elif text == 'y':
            ycnt += 1
    
    if pcnt == ycnt:
        return True
    else:
        return False