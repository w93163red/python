from calendar import isleap
from datetime import date

TUESDAY = 1
for year in xrange(1006, 2006, 10):
    t = date(year, 1, 27)
    if isleap(year) and t.weekday() == TUESDAY:
        print t.isoformat()
        

