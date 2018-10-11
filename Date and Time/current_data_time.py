# The example prints the current date, date and time, and time in various formats.
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

# The currentDate() method returns the current date.
now = QDate.currentDate()

# The date is printed in two different formats by passing
# the values Qt.ISODate and Qt.DefaultLocaleLongDate to the toString() method.
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

# The currentDateTime() returns the current date and time.
datetime = QDateTime.currentDateTime()
print(datetime.toString())

# Finally, the currentTime() method returns the current time.
time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))

'''
Output:
2018-10-11
11 October 2018
Thu Oct 11 21:17:56 2018
21:17:56
'''

