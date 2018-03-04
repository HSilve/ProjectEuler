# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def fibSum (upper):
  min_one = 2;
  min_two = 1;
  n = min_one + min_two;
  total = 2;
  while n < upper:
    if (n % 2 == 0):
      total += n;
    min_two = min_one;
    min_one = n;
    n = min_one + min_two;
  return total;

print(fibSum(4000000));
