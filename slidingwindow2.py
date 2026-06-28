def max_subarray_product_size_k(nums, k):
    current_product = 1
    for i in range(0,k):
        current_product *= nums[i]
        
    max_product = current_product
    for i in range(0 , len(nums) - k):
        current_product //= nums[i]  
        current_product *= nums[i+k]
        max_product = max(max_product, current_product)
    return max_product

print(max_subarray_product_size_k([1,2,3,4,5,4,2,6],2))   
    