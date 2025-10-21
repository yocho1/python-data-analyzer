import pandas as pd
import sys

# Allow UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

data = pd.read_csv("data.csv")

total_sales = data["sales"].sum()
average_sales = data["sales"].mean()
max_sales = data["sales"].max()
min_sales = data["sales"].min()

print("📊 SALES ANALYSIS")
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Highest Sale: {max_sales}")
print(f"Lowest Sale: {min_sales}")
print("Analysis complete! ✅")
