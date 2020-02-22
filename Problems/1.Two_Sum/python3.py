class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    if nums == None or len(nums) < 2:
      return []
    
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]
    return []
