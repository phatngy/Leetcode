def reverse(x) -> int:
    
    s = 1 if x >= 0 else -1 
    x = int(str(abs(x))[::-1]) * s
    return x if x > -2**31 and x <= 2**31-1 else 0



