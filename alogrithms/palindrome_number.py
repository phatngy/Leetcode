def isPalindrome(x: int) -> bool:
    # not convert int -> string
    if x < 0:
        return False
    elif x == 0:
        return True
    elif x%10 == 0:
        return False
    else:
        y = int(str(x)[::-1])
    if y != x:
        return False
    else:
        return True
        
isPalindrome(121)
