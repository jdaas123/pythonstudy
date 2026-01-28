#!/usr/bin/python3
# author : jdaas
# 2025-04-08
n,k = map(int,input().split())
dp = [0] * (n+1)
dp[0] = 1
for i in range(1,k+1):
    dp[i] = i+1

for j in range(k+1,n+1):
    dp[j] = dp[j-1] + dp[j - k - 1]

print((dp[n])%1000000007)