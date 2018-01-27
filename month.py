class MonthCoverage:

    def __init__(self, month):
        self._coverage = [month]

    def _sort_coverage(self):
        self._coverage.sort(key=lambda x: x.monthNumber)

    def stop(self):
        self._sort_coverage()
        return self

    @staticmethod
    def fromTo(fromMonth: Month, toMonth:Month):
        if fromMonth.monthNumber > toMonth.monthNumber:
            raise ValueError("fromMonth is after toMonth")

        mc = MonthCoverage.start(fromMonth)
        for i in range(fromMonth.monthNumber, toMonth.monthNumber):
            mc.add(MONTHS[i])

        return mc


    def add(self, month:Month):
        self._coverage.append(month)
        return self

    @staticmethod
    def start(month:Month):
        return MonthCoverage(month)

    @staticmethod
    def allYearBut(*months: int):
        currentCoverage = Month.ALL_YEAR
        for month in months:
            currentCoverage ^= month
        return currentCoverage

    @staticmethod
    def allTheseMonths(*months: Month):
        mc = MonthCoverage()
        for month in months:
            mc.add(month)
        return mc

    @staticmethod
    def monthsFromTo(fromMonth: int, toMonth: int) -> int:
        currentCoverage = fromMonth

        while fromMonth != toMonth:
            fromMonth = fromMonth << 1
            currentCoverage |= fromMonth
        return currentCoverage

    @staticmethod
    def getEncodedMonth(monthIndex: int) -> int:
        return 1 << monthIndex

class Month:

    def __init__(self, name: str, monthNumber:int):
        self._name = name
        self._bitsetPosition = 1 << monthNumber
        self._monthNumber = monthNumber

    @property
    def monthNumber(self) -> int:
        return self._monthNumber


JANUARY = Month("January", 1)
FEBRUARY = Month("February", 2)
MARCH = Month("March", 3)
APRIL = Month("April", 4)
MAY = Month("May", 5)
JUNE = Month("June", 6)
JULY = Month("July", 7)
AUGUST = Month("August", 8)
SEPTEMBER = Month("September", 9)
OCTOBER = Month("October", 10)
NOVEMBER = Month("November", 11)
DECEMBER = Month("December", 12)

MONTHS = [JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]