import pandas as pd
import matplotlib.pyplot as plt
import sys

# Allow UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Read the data
data = pd.read_csv("data.csv")

# Basic stats
total_sales = data["sales"].sum()
average_sales = data["sales"].mean()
max_sales = data["sales"].max()
min_sales = data["sales"].min()

# Print results
print("📊 SALES ANALYSIS")
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Highest Sale: {max_sales}")
print(f"Lowest Sale: {min_sales}")

# Plot sales trend
plt.figure(figsize=(8, 5))
plt.plot(data["date"], data["sales"], marker='o', color='blue', label="Daily Sales")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and show chart
plt.savefig("sales_chart.png")
plt.show()
