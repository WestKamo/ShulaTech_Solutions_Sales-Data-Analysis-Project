from sales_analysis import SalesAnalyzer
import matplotlib.pyplot as plt

def main():
    # Initialize the SalesAnalyzer with the sample data
    analyzer = SalesAnalyzer('data/sample_sales_data.csv')
    
    # Test all the analysis functions
    print("\n=== Sales Analysis Results ===")
    
    # 1. Get sales summary
    summary = analyzer.get_sales_summary()
    print("\nSales Summary:")
    for key, value in summary.items():
        print(f"{key}: {value:,.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")
    
    # 2. Get best selling products
    print("\nTop 5 Best-Selling Products:")
    best_sellers = analyzer.get_best_selling_products()
    for product, quantity in best_sellers.items():
        print(f"{product}: {quantity:,.0f} units")
    
    # 3. Get monthly trends
    print("\nMonthly Sales Trends:")
    monthly_trends = analyzer.analyze_monthly_trends()
    print(monthly_trends)
    
    # 4. Create and save plots
    # Monthly trends plot
    plt.figure(1)
    analyzer.plot_monthly_trends()
    plt.savefig('monthly_trends.png')
    
    # Product distribution plot
    plt.figure(2)
    analyzer.plot_product_distribution()
    plt.savefig('product_distribution.png')
    
    print("\nPlots have been saved as 'monthly_trends.png' and 'product_distribution.png'")

if __name__ == "__main__":
    main()
