
#Input: nums = [2, 7, 11, 15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums: list[int], target: int) -> list[int]:
    # [2,7,11,15]
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

print(twoSum([2, 7, 11, 15], 22))
print(twoSum([3, 2, 4], 6))