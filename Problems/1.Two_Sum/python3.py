class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    size = 0 if nums == None else len(nums)
    if size < 2:
      return []
    
    for i in range(size - 1):
      for j in range(i + 1, size):
        if nums[i] + nums[j] == target:
          return [i, j]
    return []
