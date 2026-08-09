"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Approach:
        -Use a greedy approach by tracking the minimum stock price so far.
        -For each price, calculate the profit if sold on that day and
        -update the maximum profit accordingly."""
        
        min_price = float('inf')
        max_profit = 0

        for price in prices:
           min_price = min(min_price, price)
           max_profit = max(max_profit, price - min_price)
        return max_profit

without built-in functions ->

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

