import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AAPL Historical Stock Analysis", layout="wide")
st.title("AAPL Historical Stock Analysis Tool (1984–Present)")

@st.cache_data
def load_data():
    data = pd.read_csv("aapl_data.csv", parse_dates=["date"])
    data = data.set_index("date")
    return data

data = load_data()

st.subheader("Stock Data Preview")
st.dataframe(data.tail(10))

st.subheader("Price Trend Chart")
min_date = data.index.min()
max_date = data.index.max()

start_date = st.date_input("Start Date", min_date)
end_date = st.date_input("End Date", max_date)

filtered = data[(data.index >= pd.Timestamp(start_date)) &
                (data.index <= pd.Timestamp(end_date))]

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(filtered.index, filtered["close"], label="Close Price", color="#1f77b4")
ax.set_title("AAPL Close Price Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price (USD)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Latest Close", f"${data['close'].iloc[-1]:.2f}")
col2.metric("Highest Price", f"${data['close'].max():.2f}")
col3.metric("Lowest Price", f"${data['close'].min():.2f}")

st.success("✅ App runs successfully with local data!")
