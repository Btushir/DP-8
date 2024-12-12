"""
Brute force: form all the sub array and check if they meet the req.
TC: O(n^2)

Approach2: DP: with each incoming element we check if by adding it to ans it is valid.
[1,2,3,4,5] till 4 the count is 2. For the incoming element 5 the count will increase by 1. Thus, repeated sub-problems.
TC: O(n)
Note: Optimization of nested iterations could happen because of (1) sliding window (2) 2 pointers (3) binary search
(4) hashing with a running sum (5) DP if repeated subproblem.
Note: recursion is not always O(2^n). It could be O(n) as well.
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        # traverse the array, the loop will end at len(nums)-2, since 
        # j is i+2 and we are making group of 3. 
        for i in range(len(nums) - 2):
            temp = []
            for j in range(i + 2, len(nums)):
                # i idx could also be used
                if nums[j - 1] - nums[j - 2] == nums[j] - nums[j - 1]:
                    ans += 1
                else:
                    break

        return ans


class Solution_extra_space:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        dp = [0 for _ in range(len(nums))]
        total = 0

        for i in range(2, len(nums)):

            # check validity of the incoming number
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                print("hi")
                dp[i] = dp[i - 1] + 1

            else:
                dp[i] = 0

            total += dp[i]

        return total


class Solution_no_space:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        total = 0
        prev = 0
        for i in range(2, len(nums)):
            # check validity of the incoming number
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr = prev + 1

            else:
                curr = 0

            total += curr
            prev = curr

        return total






