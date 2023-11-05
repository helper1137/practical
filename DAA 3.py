def knapsack_greedy(max_weight, values, weights):
    n = len(values)
    items = list(zip(values, weights, range(n)))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # Sort by value-to-weight ratio

    total_value = 0
    knapsack = [0] * n

    for value, weight, index in items:
        if max_weight >= weight:
            knapsack[index] = 1
            total_value += value
            max_weight -= weight

    return total_value, knapsack

# Driver code
max_weight = 50
values = [60, 100, 120]
weights = [10, 20, 30]

best_value, selected_items = knapsack_greedy(max_weight, values, weights)
print("Best value:", best_value)
print("Selected items:", selected_items)



#method 2

def knapsack(max_weight, values, weights):
    n = len(values)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]

# Driver code
max_weight = 50
values = [60, 100, 120]
weights = [10, 20, 30]

best_value = knapsack(max_weight, values, weights)
print("Best value:", best_value)

#method 3

def knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    selected_items = []

    for weight, value in items:
        if capacity >= weight:
            total_value += value
            selected_items.append((weight, value))
            capacity -= weight

    return total_value, selected_items

# Example usage:
items = [(10, 60), (20, 100), (30, 120)]
knapsack_capacity = 50  # Change to the knapsack's capacity
max_value, selected_items = knapsack(items, knapsack_capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)

