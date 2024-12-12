"""
THis problem is revision of the paint house, minimum falling path and pascale triangle.
Todo: do it with tabulation
"""


class Solution_brute_force_void_based:
    def helper(self, triangle, r, c, currPath):
        # base
        if r >= len(triangle):
            self.ans = min(self.ans, currPath)
            return

            # logic
        currPath += triangle[r][c]
        self.helper(triangle, r + 1, c, currPath)

        self.helper(triangle, r + 1, c + 1, currPath)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.ans = float("inf")
        self.helper(triangle, 0, 0, 0)
        return self.ans


class Solution_brute_force_return_based:
    def helper(self, triangle, r, c, currPath):
        # base
        if r >= len(triangle):
            return 0

        # logic
        # currPath += triangle[r][c]
        left = self.helper(triangle, r + 1, c, currPath)

        right = self.helper(triangle, r + 1, c + 1, currPath)

        return min(left, right) + triangle[r][c]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # memo =
        self.ans = float("inf")
        return self.helper(triangle, 0, 0, 0)
        # return self.ans


class Solution_memo:
    def helper(self, triangle, r, c, memo):
        # base
        if r >= len(triangle):
            return 0

        # logic
        if memo[r][c] != float("inf"):
            return memo[r][c]
        left = self.helper(triangle, r + 1, c, memo)

        right = self.helper(triangle, r + 1, c + 1, memo)

        memo[r][c] = min(left, right) + triangle[r][c]
        return min(left, right) + triangle[r][c]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # take number of cols and rows equal
        m = len(triangle)
        memo = [[float("inf") for _ in range(m)] for _ in range(m)]
        print(memo)
        self.ans = float("inf")
        return self.helper(triangle, 0, 0, memo)
        # return self.ans

