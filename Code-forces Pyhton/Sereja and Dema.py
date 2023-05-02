#codeforces-381A
#sereja And deema 
test = int(input())

arr=[int(x) for x in input().split()]
sereja = 0
deema = 0
left = 0
right = test-1
state = 'sereja'
while(left <= right):
  if(state == 'sereja'):
     if(arr[left] > arr[right]):
      sereja += arr[left]
      left += 1
     else:
      sereja += arr[right]
      right -= 1
     state = 'deema'  
  else:
     if(arr[left] > arr[right]):
      deema += arr[left]
      left += 1
     else:
      deema += arr[right]
      right -= 1 
     state = 'sereja' 

print(f"{sereja} {deema}")

