#twosum problem
#given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#solve - given array nums = [3,4, 7,9] and target = 7 , output = [0,1]
#explanation num[0] = 3
#            num[1] = 4
#            3+4 = 7 
# so the anser is [0, 1]

nums = [3, 4, 6, 8]
target = 10

def two_sum(num, target):
    seen={}

    for i in range(len(num)):
        needed = target - num[i]

              
        if needed in seen:
            return[seen[needed],i]

        seen[num[i]]= i

    return []

nums = [3, 4, 6, 8]
target = 10
result = two_sum(nums, target)

print(result)  # Output: [0, 2] because nums[0] + nums[2] = 3 + 6 = 10