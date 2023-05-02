##codeforces-1353B
#Two Arrays And Swaps
test = int(input())
result = []
for i in range(test):
  arr1 = list(map(int,input().split()))
  n = arr1[0]
  k = arr1[-1]
  a = sorted(list(map(int,input().split())))
  b = sorted(list(map(int,input().split())), reverse = True)
  for i in range(k):
    c = a[i]
    if(a[i] < b[i]):
      a[i] = b[i]
      b[i] = c
  result.append(sum(a))
for i in result:
  print(i)      

