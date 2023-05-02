#codeforces-1343B
#Balanced array
test = int(input())
for i in range(test):
  n = int(input())
  sum1 = 0
  sum2 = 0
  if(n % 4 != 0):
    print("No")
  else:
    print("Yes")
    j = 2
    while(j <= n):
      print(j, end=" ") 
      j += 2
      sum1 += j
    k = 1  
    while(k < n-2):
      print(k, end=" ")
      k += 2
      sum2 += k
    print(sum1 - sum2 - 2)     
