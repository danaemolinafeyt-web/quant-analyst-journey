# Week 1 - Intern Task
# Calculating dialy stock returns for multiple stocks

# Stock data - (stock name, old price, new price)

stocks = [
    ("AAPL", 150, 153),
    ("GOOGL", 2800, 2750),
    ("TSLA", 200, 215),
]

# Calculate and print returns for each stock

for name, old_price, new_price in stocks:
    daily_returns = (new_price - old_price) / old_price * 100
    print(f"{name}: {daily_returns:.2f}%")