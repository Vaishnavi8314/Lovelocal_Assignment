def number(nums):
    n = len(nums)
    condition = n // 3
    freq_map = {}
    result = set()
    for x in nums:
        freq_map[x] = freq_map.get(x, 0) + 1
    for x, count in freq_map.items():
        if count > condition:
            result.add(x)
    return list(result)
user_input = input("nums =  ")
nums = list(map(int, user_input.strip('[]').split(',')))
output = number(nums)
print(output)
