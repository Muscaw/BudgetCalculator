from typing import List
import plotly.offline as py
from plotly.graph_objs import *
from month import *


class MonthlyPayment:
    def __init__(self, name: str, monthly_fee:float, months:int=Month.ALL_YEAR):
        self.name = name
        self.monthly_fee = monthly_fee
        self.payable_months = months

class YearlyPayment(MonthlyPayment):

    def __init__(self, name: str, yearly_fee:float, months:int=Month.ALL_YEAR):
        numberOfMonths = sum(1 for x in range(0,12) if (Month.getEncodedMonth(x) & months) > 0)
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
        bars = list()
        monthly_amounts = [0 for _ in range(0,12)]
        for payment in self.payments:
            months_due = list()
            for i in range(0,12):
                if (int(payment.payable_months) & Month.getEncodedMonth(i)) > 0:
                    months_due.append(payment.monthly_fee)
                    monthly_amounts[i] = monthly_amounts[i] + payment.monthly_fee
                else:
                    months_due.append(0)
            bars.append(
                Bar(x=Month.months_string,
                        y=months_due,
                    name=payment.name)
            )

        bars.append(
            Bar(x=Month.months_string,
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
