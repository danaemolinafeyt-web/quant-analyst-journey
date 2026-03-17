# Week 1 - Intern task
# Calculating daily stock returns

# Stock prices
old_price = 150
new_price = 153

# Calculate return

daily_return = (new_price - old_price) / old_price * 100

# Print results

print(f"Old Price: ${old_price}")
print(f"New Price: ${new_price}")
print(f"Daily Return: {daily_return:.2f}%")

# f"..." is called an f-string - it lets you put variables directly inside text cleanly.
# :.2f means round to 2 decimal places.