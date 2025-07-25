# Cloud Server Cost Calculator

cost_per_hour = 0.51

# Cost calculations
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

print("Cost per day: $", round(cost_per_day, 2))
print("Cost per week: $", round(cost_per_week, 2))
print("Cost per month: $", round(cost_per_month, 2))

# Budget-based days calculation
budget = 918
days_operable = budget / cost_per_day
print("With $918, you can operate the server for", int(days_operable), "days")
