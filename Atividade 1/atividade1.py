#CONVERTENDO PARA PYTHON

def two_sums (nums, target):

    value_to_index = {} 

    for i, nums in enumerate(nums):
        value_to_index[num] = i

    for i, num in enumerate(nums):
        complement = target - num

        if complement in value_to_index and value_to_index[complement] != i:
            return [i, value_to_index[complement]]

    return -1
