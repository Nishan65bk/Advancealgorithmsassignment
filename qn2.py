def max_points(tile_multipliers):
    values = [1] + tile_multipliers + [1]
    n = len(values)

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    dp[left][k] + values[left] * values[k] * values[right] + dp[k][right]
                )

    print("Time Complexity: O(n^3)")
    return dp[0][n - 1]


# Example usage
tiles = [1, 5]
print(max_points(tiles))
