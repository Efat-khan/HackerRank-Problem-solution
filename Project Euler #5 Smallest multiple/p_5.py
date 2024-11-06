def function():
  i=1
  N=int(input())
  while i:
    for j in range(1,N+1):
      # print(i,j)
      # print(i%j)
      if(i%j !=0): 
        break
    if(j==N and i%j ==0):
      print(i)
      break
    i+=1

T=int(input())
while T:
  function()
  T-=1

