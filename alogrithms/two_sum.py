def twosum(nums: list, target: int) -> List[int]:
    nums = [(v, i) for i, v in enumerate(nums)]
    nums.sort()
    begin, end = 0, len(nums) - 1 
    
    while(begin < end):
        if nums[begin][0] + nums[end][0] == target:
            return [nums[begin][1], nums[end][1]]
            break
        elif nums[begin][0] + nums[end][0] < target:
            begin += 1
        else:
            end -= 1
        