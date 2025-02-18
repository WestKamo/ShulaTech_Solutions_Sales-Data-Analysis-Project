import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

class SalesAnalyzer:
    def __init__(self, data_path):
        """Initialize the SalesAnalyzer with the path to the sales data."""
        self.df = pd.read_csv(data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        
    def calculate_total_revenue(self):
        """Calculate the total revenue from all sales."""
        return self.df['Revenue'].sum()
    
    def get_best_selling_products(self, top_n=5):
        """Get the top N best-selling products by quantity sold."""
        return self.df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(top_n)
    
    def analyze_monthly_trends(self):
        """Analyze monthly sales trends."""
        monthly_sales = self.df.groupby(self.df['Date'].dt.to_period('M'))['Revenue'].sum()
        return monthly_sales
    
    def plot_monthly_trends(self):
        """Plot monthly sales trends using Seaborn."""
        plt.figure(figsize=(12, 6))
        monthly_sales = self.analyze_monthly_trends()
        
        sns.set_style("whitegrid")
        sns.lineplot(data=monthly_sales)
        plt.title('Monthly Sales Trends')
        plt.xlabel('Month')
        plt.ylabel('Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt
    
    def plot_product_distribution(self):
        """Create a pie chart of product sales distribution."""
        plt.figure(figsize=(10, 10))
        product_sales = self.df.groupby('Product')['Revenue'].sum()
        plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%')
        plt.title('Product Sales Distribution')
        plt.axis('equal')
        return plt
    
    def get_sales_summary(self):
        """Generate a summary of key sales metrics."""
        summary = {
            'Total Revenue': self.calculate_total_revenue(),
            'Total Orders': len(self.df),
            'Average Order Value': self.df['Revenue'].mean(),
            'Best Selling Product': self.get_best_selling_products(1).index[0]
        }
        return summary
