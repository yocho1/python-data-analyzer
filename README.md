# 📊 Python Data Analyzer

A simple yet powerful **data analysis tool** built in Python that reads CSV files, calculates key statistics, and visualizes trends using Matplotlib.

---

## 🚀 Features

✅ Reads structured data from `.csv` files  
✅ Calculates:
- Total Sales  
- Average Sales  
- Highest & Lowest Sales  

✅ Displays a **clear summary in the console**  
✅ Generates a **beautiful line chart** to visualize trends  
✅ Saves chart as `sales_chart.png`

---

## 🧠 How It Works

1. The program loads your `data.csv` file using **Pandas**.  
2. It computes sales statistics using built-in functions.  
3. It then plots a **line graph** using **Matplotlib**, showing sales over time.  
4. The chart is saved automatically and also displayed.

---

## 🧩 Example

**Input (`data.csv`):**
```csv
date,sales
2025-10-01,200
2025-10-02,450
2025-10-03,300

**Output (Console):**

📊 SALES ANALYSIS
Total Sales: 950
Average Sales: 316.67
Highest Sale: 450
Lowest Sale: 200

⚙️ Installation & Usage

1️⃣ Clone the repository
git clone https://github.com/yocho1/python-data-analyzer.git
cd python-data-analyzer

2️⃣ Install dependencies
pip install pandas matplotlib

3️⃣ Run the analyzer
python analyzer.py

🧰 Requirements

Python 3.8+
pandas
matplotlib

