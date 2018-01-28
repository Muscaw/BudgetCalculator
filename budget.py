from typing import List
import plotly.offline as py
from plotly.graph_objs import *
from month import *


class MonthlyPayment:
    def __init__(self, name: str, monthly_fee:float, months:MonthCoverage=MonthCoverage.allYear(), percentage=1.0):
        self._name = name
        self._monthly_fee = monthly_fee
        self._payable_months = months
        self._percentage = percentage

    @property
    def payable_months(self):
        return self._payable_months

    @property
    def monthly_fee(self):
        return self._monthly_fee
    
    @property
    def name(self):
        return self._name

class YearlyPayment(MonthlyPayment):

    def __init__(self, name: str, yearly_fee:float, months:MonthCoverage=MonthCoverage.allYear()):
        numberOfMonths = months.size()
        super(YearlyPayment, self).__init__(name, yearly_fee / numberOfMonths, months)


class BudgetCalculator:

    @property
    def payments(self) -> List[MonthlyPayment]:
        return self.__payments

    def __init__(self):
        self.__payments = list()

    def add_payment(self, *monthlyPayments):
        self.payments.extend(monthlyPayments)

    def monthly_amounts(self):
        amounts = list()
        for month in range(0,12):
            monthlySum = 0
            for payment in self.payments:
                if (int(payment.payable_months) & Month.getEncodedMonth(month)) > 0:
                    monthlySum += payment.monthly_fee
            amounts.append(monthlySum)
        return amounts

    def print_monthly_amounts(self):
        amounts = self.monthly_amounts()
        for i in range(0, 12):
            print(Month.months_string[i])
            print("-----")
            print(amounts[i])
            print()

    def plot_monthly_amounts_due(self, full_salary):

        months_string = [x.name for x in MONTHS]
        bars = list()
        monthly_amounts = [0 for _ in range(0,12)]
        for payment in self.payments:
            months_due = list()
            for i in range(0,12):
                if payment.payable_months.covers(MONTHS[i]):
                    months_due.append(payment.monthly_fee)
                    monthly_amounts[i] = monthly_amounts[i] + payment.monthly_fee
                else:
                    months_due.append(0)
            bars.append(
                Bar(x=months_string,
                        y=months_due,
                    name=payment.name)
            )

        bars.append(
            Bar(x=months_string,
                y=[full_salary - x for x in monthly_amounts],
                name="Free money")
        )

        layout = Layout(
            barmode='stack',
            shapes=[
                {
                    'type': 'line',
                    'x0': 0,
                    'y0': full_salary,
                    'x1': 11,
                    'y1': full_salary
                }
            ]
        )

        fig = Figure(data=bars, layout=layout)
        py.plot(fig, filename="Due payments.html")
