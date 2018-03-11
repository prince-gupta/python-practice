import time
import calendar

tick = time.time()

print tick

localtime = time.localtime(time.time())

print localtime

localtime_in_readable_format = time.asctime(time.localtime(time.time()))

print localtime_in_readable_format

cal = calendar.month(2018, 1)

print cal
