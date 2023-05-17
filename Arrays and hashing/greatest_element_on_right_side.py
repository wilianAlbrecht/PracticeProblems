"""
    Given an array arr, 
    replace every element in that array with the greatest element among the elements to its right, 
    and replace the last element with -1.

    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
    Explanation: 
    - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    - index 5 --> there are no elements to the right of index 5, so we put -1.
"""

nums = []
while True:
    try:
        nums.append(int(input("type a random number and a letter to exit ")))
    except ValueError:
        break

res = []
i = 0
while i < len(nums):
    y = i + 1

    if y == len(nums):
        break
    else:
        greatest = nums[y]

    while y < len(nums):
        
        if nums[y] > greatest:
            greatest = nums[y]
        y += 1
    
    res.append(greatest)

    if greatest == -1:
        break
    else:
        i += 1

res.append(-1)

print(res)