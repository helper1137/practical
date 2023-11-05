# Structure for an item which stores weight and corresponding value of the item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Comparison function to sort items according to profit/weight ratio
def cmp(a, b):
    ratio_a = a.profit / a.weight
    ratio_b = b.profit / b.weight
    return ratio_a > ratio_b

# Main greedy function to solve the problem
def fractionalKnapsack(W, arr):
    # Sorting items based on the profit/weight ratio
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)
    final_value = 0.0

    for i in range(len(arr)):
        if arr[i].weight <= W:
            final_value += arr[i].profit
            W -= arr[i].weight
        else:
            final_value += (arr[i].profit / arr[i].weight) * W
            break

    return final_value

# Driver code
W = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
N = len(arr)

# Function call
print("Maximum value that can be obtained:", fractionalKnapsack(W, arr))

#method 2

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    max_value = 0
    knapsack = []

    for item in items:
        if capacity >= item[0]:
            knapsack.append(item)
            capacity -= item[0]
            max_value += item[1]
        else:
            fraction = capacity / item[0]
            knapsack.append((item[0] * fraction, item[1] * fraction))
            max_value += item[1] * fraction
            break

    return max_value, knapsack

# Example usage:
items = [(10, 60), (20, 100), (30, 120)]
knapsack_capacity = 50  # Change to the knapsack's capacity
max_value, selected_items = fractional_knapsack(items, knapsack_capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
