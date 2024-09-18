# Program that searches the current location time
import time
# find out the current date
here_time = time.localtime()
# Shapes it to the format weekday-day-month-year-hour-minutes
formated_time = time.strftime("%A, %d de %B de %Y, %H:%M", here_time)
print(formated_time)