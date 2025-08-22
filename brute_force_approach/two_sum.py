# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        first_val_index = 0
        second_val_index = 0
        for i, num in enumerate(nums): # type: ignore
            new_target = target - num
            for j, val in enumerate(nums[i+1:], start = i+1):
                if val == new_target:
                    first_val_index = i
                    second_val_index = j
        return [first_val_index, second_val_index]

obj = Solution()
test = obj.twoSum([3,3], 6)
print(test)