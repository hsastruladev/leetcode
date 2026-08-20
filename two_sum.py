def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in hashmap:
            return[hashmap[diff],i]

        hashmap[num] = i
    return[]

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
