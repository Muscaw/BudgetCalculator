# Budget calculator

This script allows a user to describe his budget on a year and displays a bar graph showing the repartition of payments.

## Example

```python
from budget import *
from month import *

calculator = BudgetCalculator()

taxes = YearlyPayment("Taxes", 300)
car = YearlyPayment("Car", 5000, MonthCoverage.allYearBut(DECEMBER))
travel = YearlyPayment("Travel", 1000, MonthCoverage.monthsFromTo(FEBRUARY, JULY))

calculator.add_payment(taxes, car, travel)
calculator.plot_monthly_amounts_due(3000) # Here, put your monthly salary. This will be used to show the free money.
```
