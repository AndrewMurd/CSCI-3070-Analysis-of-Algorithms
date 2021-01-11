"""
Andrew Murdoch
100707816

This program solves the fractional knap sack problem using a greedy algorithm.
"""
import operator


# Item holds info about the item
class Item:
    def __init__(self, wt, val, index):
        self.wt = wt
        self.val = val
        self.cost = val // wt
        self.index = index


# Solves problem using greedy algorithm
# Returns maximal value possible in knapsack and array of percentages of each item used
def fractionalKnapSack(weights, values, capacity):
    items = []
    # Create array of items using inputted weights and values
    for j in range(len(weights)):
        items.append(Item(weights[j], values[j], j))

    items.sort(key=operator.attrgetter('cost'), reverse=True)  # Sort items by highest value to weight ratio (cost).

    maximalValue = 0
    fractions = [0] * len(values)  # Initialize the output array that holds fractions of items
    # Loop through each item
    for i in items:
        currentWt = int(i.wt)
        currentVal = int(i.val)
        if capacity - currentWt >= 0:  # If the current item's weight does not exceed the remaining capacity
            fractions[i.index] = 1  # Set fraction index to 1 since we used 1 whole item
            capacity -= currentWt  # Update remaining capacity
            maximalValue += currentVal  # Update maximalValue

        else:  # If current item's weight does exceed remaining weight capacity
            fraction = capacity / currentWt  # Get the fraction of item used
            fractions[i.index] = fraction
            maximalValue += currentVal * fraction   # Update maximal value in sack
            capacity = int(capacity - currentWt * fraction)  # Update capacity
            break

    return maximalValue, fractions


# Driver Code
weights = [10, 80, 20, 30]
values = [60, 80, 100, 120]
capacity = 50

maxValue, fractions = fractionalKnapSack(weights, values, capacity)
for i in range(len(fractions)):
    print("Fraction of Item " + str(i + 1) + ": ", fractions[i])
print("The maximum value of items that can be carried:", maxValue)
