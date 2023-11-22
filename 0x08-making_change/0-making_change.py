#!/usr/bin/env python3
"""
Coin Change Problem Solver

This script provides a function to determine the fewest number of coins
needed to meet a given amount total, given a list of coin denominations.

Usage:
    makeChange(coins, total)

Parameters:
    coins (list): List of coin values.
    total (int): Target amount to make change for.

Returns:
    int: The fewest number of coins needed to meet the total.
         Returns -1 if the total cannot be met by any combination of coins.

Example:
    >>> makeChange([1, 2, 25], 37)
    7
    >>> makeChange([1256, 54, 48, 16, 102], 1453)
    -1
"""
import sys


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given
    amount total.

    Args:
        coins (list): List of coin values.
        total (int): Target amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any combination
             of coins.
    """
    n = len(coins)
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0

    for amt in range(1, total + 1):
        temp = sys.maxsize
        for c in range(n):
            if coins[c] <= amt:
                temp_amt = dp[amt - coins[c]] + 1
                if temp_amt < temp:
                    temp = temp_amt
                    dp[amt] = temp

    return dp[total] if dp[total] != sys.maxsize else -1


"""
# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))   # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1
"""
