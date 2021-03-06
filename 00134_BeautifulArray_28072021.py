"""
In this problem we have n = 1000, which is too big to use dfs/backtracking, so we need to find some pattern. We need to
avoid structures like i < k < j with nums[i] + nums[j] = 2 * nums[k], which means that nums[i] and nums[j] has the same
parity: they are both odd or even. This lead us to the following idea: let us split all numbers into 2 groups: all odd
numbers and then all even numbers.
[ odd numbers ] [ even numbers ]

Then if i, j, k lies in two different groups, we are OK, we will hever have forbidden pattern. Also, if we look at odd
numbers, imagine n = 12, then we have [1, 3, 5, 7, 9, 11] and if we divide each number by 2 and subtract 1 we have
[0, 1, 2, 3, 4, 5]. Also when we did this transformation, if we did not have forbidden pattern, we still do not have it!
So, what we need to do is to run function recursively for odd and even numbers and concatenate them.

Complexity

From the first sight, time complexity is O(n log n), because we have recursion C(n) = C(n//2) + C((n+1)//2), which lead
to O(n log n). However it can be shown that it is O(n). Imagine case n = 105, then we have 105 -> (52, 53) ->
(26, 26, 27, 27) -> (13, 13, 13, 13, 14, 14, 14, 14) and if we use memoisation, no need to solve problem each time for
13, we can do it only once. On each level we will have at most two values in our recursion tree. Space complexity is
O(n).
"""

class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        def dfs(N):
            if N == 1: return (1,)
            t1 = dfs((N + 1) // 2)
            t2 = dfs(N // 2)
            return tuple(i * 2 - 1 for i in t1) + tuple(i * 2 for i in t2)

        return dfs(n)

obj = Solution()
print(obj.beautifulArray(20))
#https://leetcode.com/problems/beautiful-array/