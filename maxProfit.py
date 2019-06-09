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

    def multipleTransaction(prices):
        if not prices or len(prices) is 1:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return(profit)


(Solution.maxProfit([1,2,3,-1, -4]))
(Solution.multipleTransaction([1,2,3,-1, -4,1,3]))