import streamlit as st
import pandas as pd
from sales_analysis import SalesAnalyzer
import plotly.express as px

st.set_page_config(page_title="Sales Data Analysis", layout="wide")

st.title("Sales Data Analysis Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your sales data CSV file", type="csv")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_sales_data.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Initialize analyzer
    analyzer = SalesAnalyzer("temp_sales_data.csv")
    
    # Get sales summary
    summary = analyzer.get_sales_summary()
    
    # Display metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Revenue", f"${summary['Total Revenue']:,.2f}")
    with col2:
        st.metric("Total Orders", f"{summary['Total Orders']:,}")
    with col3:
        st.metric("Average Order Value", f"${summary['Average Order Value']:,.2f}")
    with col4:
        st.metric("Best Selling Product", summary['Best Selling Product'])
    
    # Monthly Trends
    st.subheader("Monthly Sales Trends")
    monthly_trends = analyzer.analyze_monthly_trends()
    fig = px.line(x=monthly_trends.index.astype(str), y=monthly_trends.values,
                  labels={'x': 'Month', 'y': 'Revenue'},
                  title='Monthly Sales Trends')
    st.plotly_chart(fig, use_container_width=True)
    
    # Best Selling Products
    st.subheader("Top 5 Best-Selling Products")
    best_selling = analyzer.get_best_selling_products()
    fig = px.bar(x=best_selling.index, y=best_selling.values,
                 labels={'x': 'Product', 'y': 'Quantity Sold'},
                 title='Top 5 Best-Selling Products')
    st.plotly_chart(fig, use_container_width=True)
    
    # Product Sales Distribution
    st.subheader("Product Sales Distribution")
    product_sales = analyzer.df.groupby('Product')['Revenue'].sum()
    fig = px.pie(values=product_sales.values, names=product_sales.index,
                 title='Product Sales Distribution')
    st.plotly_chart(fig, use_container_width=True)
    
else:
    st.info("Please upload a sales data CSV file to begin the analysis.")
    st.markdown("""
    Expected CSV format:
    - Date: Date of sale (YYYY-MM-DD)
    - Product: Product name
    - Quantity: Number of units sold
    - Revenue: Total revenue from sale
    """)
