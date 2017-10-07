# find valid categories and sort them based on date

import sys
    
def valid(year_month, start, end):
    start_year, start_month = start.split("-")
    end_year, end_month = end.split("-")
    year, month = year_month.split("-")
    start_year, start_month = int(start_year), int(start_month)
    end_year, end_month = int(end_year), int(end_month)
    year, month = int(year), int(month)
    if year == start_year and month >= start_month:
        return True
    if year == end_year and month < end_month:
        return True
    if year > start_year and year < end_year:
        return True
    return False

sys.stdin = open("sample.txt")
data = sys.stdin.readlines()
start_date, end_date = data[0].split(",")
calendar = {}
for i in range(2, len(data)): 
    time, category, value = data[i].split(",")
    year_month = time[:-3]
    if valid(year_month, start_date, end_date):
        category = category[1:]
        if year_month in calendar:
            category_dict = calendar[year_month]
            if category in category_dict:
                category_dict[category] += int(value)
            else:
                category_dict[category] = int(value)
        else:
            calendar[year_month] = {category: int(value)}
for time in sorted(calendar.keys(), reverse = True):
    categories = sorted(calendar[time].keys())
    result = time
    for category in categories:
        result = result + ", " + category + ", " + str(calendar[time][category])
    print result
