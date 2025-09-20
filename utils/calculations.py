def calculate_scenario(revenue, expenses, marketing, hiring_cost, price_increase):
    adjusted_revenue = revenue * (1 + price_increase / 100)
    total_expenses = expenses + marketing + hiring_cost
    profit = adjusted_revenue - total_expenses
    return adjusted_revenue, total_expenses, profit

def calculate_runway(cash, total_expenses, adjusted_revenue):
    monthly_burn = max(0, total_expenses - adjusted_revenue)
    runway = cash / monthly_burn if monthly_burn > 0 else float("inf")
    return runway
