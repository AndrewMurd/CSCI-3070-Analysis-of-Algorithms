"""
Andrew Murdoch
100707816

This program counts the minimum number of operations (insert, remove, replace) needed to convert one string into another using dynamic programming (Minimum Edit Distance).
"""


# The cost of insert, remove and replace is one
def minEditDistance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D array to store results of sub problems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    # Fill dp with results in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If the first string is empty insert all characters from second string
            if i == 0:
                dp[i][j] = j
            # If the second string is empty insert all characters from first string
            elif j == 0:
                dp[i][j] = i
            # If last character of both strings are the same, ignore and do not perform any operation
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # If character is different, find minimum of all possibilities (insert, remove, replace)
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


# Print minEditDistance output
def printMED(str1, str2):
    print("The MED between string", "\"" + str1 + "\"", "and", "\"" + str2 + "\"", "is", minEditDistance(str1, str2))


# Driver code
string1 = "spoof"
string2 = "stool"
string3 = "podiatrist"
string4 = "pediatrician"
string5 = "blaming"
string6 = "conning"

printMED(string1, string2)
printMED(string3, string4)
printMED(string5, string6)
