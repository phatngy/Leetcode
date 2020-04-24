def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    max_curr = length_curr = start = 0

    for i, val in enumerate(s):
        if val in d and d[val] >= start:
            max_curr = max(length_curr, max_curr)
            start = d[val] + 1
            d[val] = i
            length_curr = i + 1 - start
            
        else:
            d[val] = i    
            length_curr  += 1
    return max(max_curr, length_curr)


lengthOfLongestSubstring(" ")

