from collections import Counter   
from collections import Counter
import statistics
colors = [
    "GREEN", "YELLOW", "BROWN", "BLUE", "PINK", "ORANGE", "CREAM", "RED", "WHITE", "BLACK"
]

data = [
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM",
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    "ASH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE",
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED",
    "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE",
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM",
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED",
    "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"
]


"""To determine the mean color, \
    we need to calculate the average of all the colors.\
    First, we need to convert the  string of colors into a list of individual colors:"""

color_counts = Counter(data)
total_count = sum(color_counts.values())
mean_color = max(color_counts, key=color_counts.get)
print("Mean color:", mean_color)


"""To find the color that was mostly worn throughout the week,\
    we can again count the frequency of each color and find the one with the highest count"""

most_worn_color = max(color_counts, key=color_counts.get)
print("Most worn color:", most_worn_color)



"""To find the median color, we first need to sort the list of colors and then find the middle element."""

sorted_colors = sorted(colors, key=lambda x: color_counts[x], reverse=True)
n = len(sorted_colors)
if n % 2 == 0:
    median_color = sorted_colors[n // 2 - 1]
else:
    median_color = sorted_colors[n // 2]
print("Median color:", median_color)

# To get the variance of the colors, we can use the variance function in the statistics module
variance = statistics.variance(color_counts.values())
print("The variance of the colors is:", variance)


# Recursive searching algorithm to search for a number entered by user """

def recursive_search(lst, x):
    if not lst:
        return False
    elif lst[0] == x:
        return True
    else:
        return recursive_search(lst[1:], x)

# Program to generate random 4-digit numbers of 0s and 1s and convert to base 10

import random

# Generate a random 4-digit number of 0s and 1s
num_str = ''.join(random.choices(['0', '1'], k=4))

# Convert the number to base 10
num_dec = int(num_str, 2)

print(num_str, num_dec)


# Program to sum the first 50 Fibonacci number

def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for i in range(n):
        total += a
        a, b = b, a+b
    return total

print(fibonacci_sum(50))
