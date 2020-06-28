# complexity: n^2

from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    size = 0 if nums == None else len(nums)
    if size < 2:
      return []
    
    for i in range(size - 1):
      complement = target - nums[i]
      try:
        return [i, nums[i + 1:].index(complement) + i + 1]
      except:
        pass
    return []

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))