Apple Stock Analysis Tool | ACC102 Track4

Student ID: 2469051  
Name: Yunfei Zhao

This is an interactive stock analysis dashboard built with Python. It allows users to explore Apple Inc. (AAPL) historical stock prices, visualize monthly trends, and analyze daily return distributions through dynamic year and month filters.

# Project Overview
The tool provides a clear, interactive way to examine AAPL stock performance from 1984 to present. You can select any year and month within the dataset to view customized price charts, return distributions, and key risk-return metrics.

# Data Information
- Data Provider: AkShare
- Stock Symbol: AAPL (Apple Inc.)
- Time Period: 1984.1-present
- Data Included: Daily Open, High, Low, Close Prices, Trading Volume

# Core Features
1. Interactive Year & Month Filtering  
   - Dropdown selection for any year (1984-present）and month  
   - Charts and metrics update dynamically based on user input

2. Monthly Stock Price Trend Visualization
   - Line chart showing daily closing prices for the selected month  
   - Clear labels, grid lines, and formatting for readability

3. Daily Return Distribution Analysis  
   - Histogram of daily returns to visualize the frequency and spread of price changes

4. Key Financial Metrics
   - Latest closing price (of the selected month)  
   - Average daily return  
   - Daily volatility (standard deviation of returns, as a risk indicator)

# How to Run
Install required packages
- pip install akshare pandas numpy matplotlib ipywidgets

Run the interactive analysis
- python your_script_name.py


# When you select a year and month (e.g., 2026-04), the dashboard will display:
-  A line chart of closing prices over the month
-  A histogram of daily returns
-  A summary of key statistics including the latest price, average daily return, and volatility
