""" 
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
"""

def validator(nums):
    
    i = 0
    while i < len(nums) :
        x = 0
        while x < len(nums):
            if x != i:
                if nums[i] == nums[x]:
                    return True
        
            x += 1

        i += 1
    
    return False


nums = [1, 5, 8, 60, 20, 1, 7, 10]

print(validator(nums))

