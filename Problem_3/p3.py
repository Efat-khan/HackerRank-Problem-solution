
def largest_prime_factor(n):
  """Return the largest prime factor of n."""
  while n%2 == 0:
    largest_prime_factor = 2;
    n //= 2;
    
  factor = 3;
  while factor * factor <= n:
    while n % factor == 0:
      largest_prime_factor = factor
      n//= factor
    factor +=2
  if n>2:
    largest_prime_factor = n
  return largest_prime_factor
t=int(input())
for i in range(0,t):
  n=int(input())
  print(largest_prime_factor(n))

