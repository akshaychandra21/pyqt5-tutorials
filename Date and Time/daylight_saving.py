# The example checks if the datetime is in the daylight saving time.
from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()

# The timeZoneAbbreviation() method returns the
# time zone abbreviation for the datetime.
print("Time zone: {0}".format(now.timeZoneAbbreviation()))

# The isDaylightTime() returns if the datetime falls in daylight saving time.
if now.isDaylightTime():
    print("The current date falls into DST time")
else:
    print("The current date does not fall into DST time")

'''
Output:
Time zone: India Standard Time
The current date does not fall into DST time
'''