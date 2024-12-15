import random
import time

# Function to Generate DNA Strings
def generate_dna_strings():
    alphabet = ['A', 'C', 'G', 'T']
    str1 = ''.join(random.choices(alphabet, k=10))
    str2 = ''.join(random.choices(alphabet, k=10))
    return str1, str2

# Recursive Solution without Memoization
def lcs_recursive(X: str, Y: str) -> int:
    def helper(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if X[m - 1] == Y[n - 1]:
            return 1 + helper(m - 1, n - 1)
        else:
            return max(helper(m, n - 1), helper(m - 1, n))

    return helper(len(X), len(Y))

# Recursive Solution with Memoization
def lcs_memoization(X: str, Y: str) -> int:
    memo = {}

    def helper(m: int, n: int) -> int:
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0 or n == 0:
            return 0
        if X[m - 1] == Y[n - 1]:
            memo[(m, n)] = 1 + helper(m - 1, n - 1)
        else:
            memo[(m, n)] = max(helper(m, n - 1), helper(m - 1, n))
        return memo[(m, n)]

    return helper(len(X), len(Y))

# Dynamic Programming Solution (Bottom-Up)
def lcs_dynamic(X: str, Y: str) -> str:
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

# Generate Random DNA Strings
X, Y = generate_dna_strings()
print("Generated DNA String 1:", X)
print("Generated DNA String 2:", Y)

# Compare Solutions
start = time.time()
recursive_result = lcs_recursive(X, Y)
end = time.time()
print("Recursive LCS Length:", recursive_result, "| Time Taken:", end - start, "seconds")

start = time.time()
memo_result = lcs_memoization(X, Y)
end = time.time()
print("Memoization LCS Length:", memo_result, "| Time Taken:", end - start, "seconds")

start = time.time()
dynamic_result = lcs_dynamic(X, Y)
end = time.time()
print("Dynamic LCS:", dynamic_result, "| Time Taken:", end - start, "seconds")
