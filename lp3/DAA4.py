def knapsack_dp(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# Input from user
n = int(input("Enter the number of items: "))
weights = []
profits = []
print("Enter the weights of the items:")
for i in range(n):
    weight = int(input(f"Weight of item {i + 1}: "))
    weights.append(weight)

print("Enter the profits of the items:")
for i in range(n):
    profit = int(input(f"Profit of item {i + 1}: "))
    profits.append(profit)

capacity = int(input("Enter the knapsack capacity: "))

# Calculate maximum profit
max_profit = knapsack_dp(weights, profits, capacity)
print("Maximum profit achievable:", max_profit)
