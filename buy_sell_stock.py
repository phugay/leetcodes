# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

from itertools import permutations, combinations

class Solution(object):
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        #descending 
        des_prices = sorted(prices, reverse=True)
        #ascending
        asc_prices = sorted(prices)
        
        #empty case
        if len(prices) == 0: 
            return 0 
        
        #descending case
        if prices == des_prices:
            return 0
        
        #ascending case
        elif prices == asc_prices:
            profit = prices[len(prices)-1]-prices[0]
            return profit
        
        #all kinds of combos
        else:
            minimum = 99999 # represent minimum price so far
            profit = 0
            local_profit = 0
            for price in prices:
                if price > minimum:
                    diff = price - minimum
                    local_profit = max(diff, local_profit)
                    if diff < local_profit:
                        minimum = price
                        profit+=local_profit
                        local_profit = 0
                elif price <= minimum:
                    minimum = price
                    profit += local_profit
                    local_profit = 0
            profit += local_profit
            return profit