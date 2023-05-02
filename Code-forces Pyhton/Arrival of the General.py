#codeforces-144A
#Arrival of the general
soldier = int(input())
heights = list(map(int, input().split()))
maxvalue = 0
maxindex = 0
minvalue = 101
minindex = 0
for i in range(0, soldier):
  if(heights[i] > maxvalue):
    maxindex = i
    maxvalue = heights[i]
  if(heights[i] <= minvalue):
    minindex = i
    minvalue = heights[i] 
if(maxindex > minindex):
  print((maxindex - 1) + (soldier - minindex) - 1) 
else:
  print((maxindex - 1) + (soldier - minindex)) 
