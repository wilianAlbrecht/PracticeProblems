"""
    Given an integer array nums of length n, 
    you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
"""
nums = []
while True:
    try:
        nums.append(int(input("type a random number and a letter to exit ")))
    except ValueError:
        break

ans = nums
for i in range(len(nums)):
    ans.append(nums[i])

print(ans)