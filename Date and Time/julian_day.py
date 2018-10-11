'''Julian day refers to a continuous count of days since the beginning of the Julian Period.
It is used primarily by astronomers.
It should not be confused with the Julian calendar. The Julian Period started in 4713 BC.
The Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC.'''

# In the example, we compute the Gregorian date and the Julian day for today.
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

# The Julian day is returned with the toJulianDay() method.
print("Gregorian date for today: ", now.toString(Qt.ISODate))
print("Julian day for today: ", now.toJulianDay())

'''
Output:
Gregorian date for today:  2018-10-11
Julian day for today:  2458403
'''