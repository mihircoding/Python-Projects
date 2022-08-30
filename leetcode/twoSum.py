def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return list([i,j])
sample = [3,2,4]
print(twoSum(sample,6))
