shares = 10
share_price = 150
new_share_price = 175

investment_cost = shares * share_price
current_value = shares * new_share_price
profit = current_value - investment_cost
percentage_return = (profit / investment_cost) * 100

print("Investment Cost: $", investment_cost)
print("Current Investment Value: $", current_value)
print("Profit or Loss: $", profit)
print("Percentage Return:", round(percentage_return, 2), "%")