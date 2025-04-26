import datetime

time_now = datetime.datetime.now()
timestamp = time_now.timestamp()
print("Seconds since January 1, 1970:",
        "{:,f}".format(timestamp),
        "or {:,.2e}".format(timestamp))
print(time_now.strftime('%b %d %Y'))
