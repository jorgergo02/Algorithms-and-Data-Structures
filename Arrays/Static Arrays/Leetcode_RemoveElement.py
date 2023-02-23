def removeElement(nums, val):
    l = 0
    for r in range(0, len(nums)):
      if nums[r] != val:
        nums[l] = nums[r]
        l += 1
    return l


def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)