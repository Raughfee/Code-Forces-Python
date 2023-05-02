#codeforces-271A
#A beautiful year
year = int(input()) + 1
while True:
    unique_numbers_in_year = set(str(year))
    if len(unique_numbers_in_year) == 4:
        print(year)
        break
    else:
        year += 1