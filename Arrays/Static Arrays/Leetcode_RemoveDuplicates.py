def removeDuplicates(nums):
    if len(nums) != 0:
      l = 1 # Set left pointer to 1
      for r in range (1, len(nums)):
          if nums[r] != nums[r - 1]:
              nums[l] = nums[r]
              l += 1
      return l
    else: 
       return 0
