#codeforces-71A
#way too long words
n = int(input())
for i in range(0, n):
  string = str(input())
  s = len(string)
  if s > 10:
    print(string[0], end='')
    print(s-2, end='')
    print(string[s-1])
  else:
    print(string)  