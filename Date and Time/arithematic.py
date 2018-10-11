# The example determines the current datetime and add or subtract days, seconds, months, and years.
from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Today:", now.toString(Qt.ISODate))
print("Adding 12 days: {0}".format(now.addDays(12).toString(Qt.ISODate)))
print("Subtracting 22 days: {0}".format(now.addDays(-22).toString(Qt.ISODate)))

print("Adding 50 seconds: {0}".format(now.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 months: {0}".format(now.addMonths(3).toString(Qt.ISODate)))
print("Adding 12 years: {0}".format(now.addYears(12).toString(Qt.ISODate)))

'''
Output:
Today: 2018-10-11T21:19:44
Adding 12 days: 2018-10-23T21:19:44
Subtracting 22 days: 2018-09-19T21:19:44
Adding 50 seconds: 2018-10-11T21:20:34
Adding 3 months: 2019-01-11T21:19:44
Adding 12 years: 2030-10-11T21:19:44
'''