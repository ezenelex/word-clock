import time

localTime = time.localtime()
year = localTime.tm_year
month = localTime.tm_mon
day = localTime.tm_mday
hour24 = localTime.tm_hour
minute = localTime.tm_min
second = localTime.tm_sec
yday = localTime.tm_yday

minute5 = round(minute/5)
if minute5 == 12:
    minute5 = 0

if hour24 > 12:
    hour12 = hour24 - 12
elif hour24 == 0:
    hour12 = 12
else:
    hour12 = hour24

print("Year: " + str(year) + " Month: " + str(month) + " Day: " + str(day) + " Hour: " + str(hour24))