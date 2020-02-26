from typing import List

def binarySearch(nums: List[int], target: int, left: int, right: int):
  if nums[left] == target:
    return left
  if nums[right] == target:
    return right
  if nums[left] > target or nums[right] < target or right - left < 2:
    return None

  middle = (right + left) // 2 # floor
  if nums[middle] == target:
    return middle
  elif nums[middle] < target:
    return binarySearch(nums, target, middle + 1, right - 1)
  else:
    return binarySearch(nums, target, left + 1, middle - 1)


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    size = 0 if nums == None else len(nums)
    if size < 2:
      return []
    
    # 1. sort
    sorted = nums.copy()
    sorted.sort()
    for i in range(size - 1):
      # 2. find if exist with binary search(ln complexity)
      complement = target - sorted[i]
      found = binarySearch(sorted, complement, i + 1, size - 1)
      if found != None:
        # 3. existed, get index in the original list
        values = [sorted[i], complement]
        # use array to store result to avoid same values interference
        result = []
        for j in range(size):
          if nums[j] in values:
            result.append(j)
            values.remove(nums[j])
            if len(values) == 0:
              return result
    return []

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
