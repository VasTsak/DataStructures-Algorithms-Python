"""
Coin Change

You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

As an example:

Input: coins = [1, 2, 3], amount = 6
Output: 2
Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use 3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.

Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1

Base Cases:
  # when Amount == 0: F(Amount) = 0
  # when Amount < 0: F(Amount) =  float('inf')
"""

def coin_change(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}

    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0

        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]

    res = return_change(amount)

    # return -1 when no change found
    return -1 if res == float('inf') else res

def test_function(test_case):
  arr = test_case[0]
  amount = test_case[1]
  solution = test_case[2]
  output = coin_change(arr, amount)
  if output == solution:
      print("Pass")
  else:
      print("Fail")

  arr = [1,2,5]
  amount = 11
  solution = 3
  test_case = [arr, amount, solution]
  test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
