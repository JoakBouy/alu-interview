#!/usr/bin/python3
'''Minimum Operations'''

def minOperations(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = i     # Paste i-1 times
        for j in range(1, i):
            dp[i] = min(dp[i], dp[j] + (i-j))  # Copy All + Paste i-j times

    if dp[n] == 0:
        return 0
    return dp[n]