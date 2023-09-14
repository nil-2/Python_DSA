class solution(object):
    def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i
            
input_list = [1,2,8,12,15]
target = int(input('enter target :'))
ob1 = solution()
print(ob1.twoSum(input_list, target))