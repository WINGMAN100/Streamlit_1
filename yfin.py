pip install yfinance 
pip install plotly 
import yfinance as yf
import streamlit as st
import plotly.express as px

st.title("Stock chart")

# Getting inputs from the sidebar
ticker = st.sidebar.text_input("Ticker", value="AAPL")  # Set a default ticker for testing
sd = st.sidebar.date_input("Start Date")
ed = st.sidebar.date_input("End Date")

# Convert the dates to string format (YYYY-MM-DD)
sd_str = sd.strftime('%Y-%m-%d')
ed_str = ed.strftime('%Y-%m-%d')

# Download the data from yfinance
if ticker:  # Check if a ticker is provided
    data = yf.download(ticker, start=sd_str, end=ed_str)

    if not data.empty:
        st.write(f"Showing stock data for {ticker}")
        st.write(data)

        # Plot the stock prices
        fig = px.line(data, x=data.index, y='Close', title=f"{ticker} Closing Prices")
        st.plotly_chart(fig)
    else:
        st.write("No data available for the given dates.")
else:
    st.write("Please enter a valid ticker symbol.")
