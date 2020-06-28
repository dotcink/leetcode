# The idea of Hashmap is inspired from leetcode hint.
#
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    size = 0 if nums == None else len(nums)
    if size < 2:
      return []
    
    value_to_index = {}
    for i in range(size):
      num = nums[i]
      complement = target - num
      found = value_to_index.get(complement)
      if found != None:
        return [found, i]
      value_to_index[num] = i
    return []

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))