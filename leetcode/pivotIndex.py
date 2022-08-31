def pivotIndex(nums):
    l,r,pivot = 0, sum(nums) - nums[0] , 0
    while l != r and pivot < len(nums)-1:
        pivot += 1
        r -= nums[pivot]
        l += nums[pivot-1]
    return pivot if l == r else -1
sample = [1,2,3]
print(pivotIndex(sample))