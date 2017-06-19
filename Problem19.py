from datetime import date

result = 0
for year in range(1901,2001):
    for month in range(1,13):
        if date(year,month,1).weekday() == 6:
            result += 1
print(result)
