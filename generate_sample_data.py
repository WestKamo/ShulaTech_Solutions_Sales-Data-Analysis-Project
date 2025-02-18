import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
prices = {'Laptop': 1200, 'Smartphone': 800, 'Tablet': 500, 'Headphones': 200, 'Smartwatch': 300}

# Create empty lists to store data
all_dates = []
all_products = []
all_quantities = []
all_revenues = []

# Generate random sales data
for date in dates:
    # Generate 1-5 sales per day
    num_sales = np.random.randint(1, 6)
    for _ in range(num_sales):
        product = np.random.choice(products)
        quantity = np.random.randint(1, 4)
        revenue = prices[product] * quantity
        
        all_dates.append(date)
        all_products.append(product)
        all_quantities.append(quantity)
        all_revenues.append(revenue)

# Create DataFrame
df = pd.DataFrame({
    'Date': all_dates,
    'Product': all_products,
    'Quantity': all_quantities,
    'Revenue': all_revenues
})

# Save to CSV
df.to_csv('data/sample_sales_data.csv', index=False)
print("Sample data generated and saved to 'data/sample_sales_data.csv'")
