class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            point1 = nums[i]
            point2 = target - point1

            for j in range(len(nums)):
                if nums[j] == point2 and i != j:
                    return [i,j]
            