#Leetcode MaxProfit I
# O(n)

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(prices):

        maxSoFar = 0
        minSoFar = float("inf")

        for num in prices:

            if num < minSoFar:

                minSoFar = num

            elif num - minSoFar > maxSoFar:

                maxSoFar = num - minSoFar

        return maxSoFar

(Solution.maxProfit([1,2,3,-1, -4]))