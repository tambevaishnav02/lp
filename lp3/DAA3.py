def fractional_knapsack(weights, profits, capacity):
    items = sorted([(profits[i] / weights[i], weights[i], profits[i]) for i in range(len(weights))], reverse=True)
    total_profit = 0
    for ratio, weight, profit in items:
        if capacity >= weight:
            # Take the whole item
            capacity -= weight
            total_profit += profit
        else:
            # Take the fraction of the remaining capacity
            total_profit += profit * (capacity / weight)
            break
    return total_profit
n = int(input("Enter the number of items: "))
weights = []
profits = []

print("Enter the weights of the items:")
for i in range(n):
    weight = float(input(f"Weight of item {i + 1}: "))
    weights.append(weight)

print("Enter the profits of the items:")
for i in range(n):
    profit = float(input(f"Profit of item {i + 1}: "))
    profits.append(profit)

capacity = float(input("Enter the knapsack capacity: "))
# Calculate maximum profit
max_profit = fractional_knapsack(weights, profits, capacity)
print("Maximum profit achievable:", max_profit)
