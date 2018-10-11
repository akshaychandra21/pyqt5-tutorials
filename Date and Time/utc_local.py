# The example determines the current universal and local date and time.
from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

# We get the universal time with the toUTC() method from the date time object.
print("Local datetime: ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

# The offsetFromUtc() gives the difference between universal time and local time in seconds.
print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))

'''
Output:
Local datetime:  2018-10-11T21:18:14
Universal datetime:  2018-10-11T15:48:14Z
The offset from UTC is: 19800 seconds
'''