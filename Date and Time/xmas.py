# The example calculates the number of days passed from the last XMas and the number of days until the next XMas.
from PyQt5.QtCore import QDate

xmas1 = QDate(2017, 12, 24)
xmas2 = QDate(2018, 12, 24)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last XMas".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next XMas".format(nofdays))

'''
Output:
291 days have passed since last XMas
There are 74 days until next XMas
'''