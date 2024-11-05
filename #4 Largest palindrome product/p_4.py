
def largest_palindrome_less_than_N(N):
  max_palindrome = -1

  for i in range(999,99,-1):
    for j in range(i,99,-1):
      product=i*j

      if product<max_palindrome:
        break
      if product<N and str(product) == str(product)[::-1]:
        max_palindrome=product
  return max_palindrome


T = int(input())

for _ in range(T):
  N = int(input())
  print(largest_palindrome_less_than_N(N))