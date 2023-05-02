#codeforces 158-A
#next round
n, k = map(int, input().split())
counter = 0
a = list(map(int, input().split()))
for i in range(0,n):
    if(a[i] >= a[k-1] and a[i] > 0):
        counter = counter + 1
print(counter)    
