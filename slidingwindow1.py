def max_subarray_sum_size_k(nums,k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(0,len(nums)-k):
        current_sum -=nums[i]
        current_sum += nums[i+k]
        if(current_sum > max_sum):
            max_sum = current_sum
    return max_sum

print(max_subarray_sum_size_k([1,2,3,4,5],3))

