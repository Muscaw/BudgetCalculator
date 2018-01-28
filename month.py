
class Month:

    def __init__(self, name: str, monthNumber:int):
        self._name = name
        self._bitsetPosition = 1 << monthNumber
        self._monthNumber = monthNumber

    def __eq__(self, other):
        return self.name == other.name and self.monthNumber == other.monthNumber

    @property
    def name(self):
        return self._name

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


class MonthCoverage:

    def __init__(self, month=None):
        if month is None:
            self._coverage = []
        else:
            self._coverage = [month]

    def _sort_coverage(self):
        self._coverage.sort(key=lambda x: x.monthNumber)

    def stop(self):
        self._sort_coverage()
        return self

    def add(self, month:Month):
        self._coverage.append(month)
        return self

    def remove(self, month:Month):
        self._coverage.remove(month)

    def size(self) -> int:
        return len(self._coverage)

    def covers(self, month: Month) -> bool:
        for coveredMonth in self.months:
            if coveredMonth == month:
                return True
        return False

    @property
    def months(self):
        return self._coverage

    @staticmethod
    def fromTo(fromMonth: Month, toMonth: Month):
        if fromMonth.monthNumber > toMonth.monthNumber:
            raise ValueError("fromMonth is after toMonth")

        mc = MonthCoverage.start(fromMonth)
        for i in range(fromMonth.monthNumber, toMonth.monthNumber):
            mc.add(MONTHS[i])

        return mc

    @staticmethod
    def start(month:Month):
        return MonthCoverage(month)

    @staticmethod
    def allYearBut(monthCoverage):
        currentCoverage = MonthCoverage.allYear()
        for month in monthCoverage.months:
            currentCoverage.remove(month)
        return currentCoverage

    @staticmethod
    def allTheseMonths(*months: Month):
        mc = MonthCoverage()
        for month in months:
            mc.add(month)
        return mc

    @staticmethod
    def allYear():
        currentCoverage = MonthCoverage()
        for month in MONTHS:
            currentCoverage.add(month)
        return currentCoverage

    @staticmethod
    def monthsFromTo(fromMonth: Month, toMonth: Month):
        currentCoverage = MonthCoverage()

        for i in range(fromMonth.monthNumber - 1, toMonth.monthNumber):
            currentCoverage.add(MONTHS[i])

        return currentCoverage

    @staticmethod
    def getEncodedMonth(monthIndex: int) -> int:
        return 1 << monthIndex
