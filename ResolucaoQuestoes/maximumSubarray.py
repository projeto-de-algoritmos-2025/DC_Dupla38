from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)

            cross_max = maxCrossingSum(nums, left, mid, right)

            return max(left_max, right_max, cross_max)

        def maxCrossingSum(arr, left, mid, right):
            left_sum = float('-inf')
            curr = 0
            for i in range(mid, left - 1, -1):
                curr += arr[i]
                left_sum = max(left_sum, curr)

            right_sum = float('-inf')
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += arr[i]
                right_sum = max(right_sum, curr)

            return left_sum + right_sum

        return helper(0, len(nums) - 1)