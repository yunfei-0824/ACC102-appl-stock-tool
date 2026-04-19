import streamlit as st
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("AAPL Historical Stock Analysis")

data = ak.stock_us_daily(symbol="AAPL", adjust="")
data["date"] = pd.to_datetime(data["date"])
data["year"] = data["date"].dt.year
data["month"] = data["date"].dt.month
data["Daily_Return"] = data["close"].pct_change()

years = sorted(data["year"].unique())

year = st.selectbox("Select Year", years, index=len(years)-1)
month = st.slider("Select Month", min_value=1, max_value=12, value=4, step=1)

df = data[(data["year"] == year) & (data["month"] == month)].copy()

if df.empty:
    st.warning(f"No data available for {year}-{month:02d}")
else:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7))

    ax1.plot(df["date"], df["close"], linewidth=2, color='#0072b2')
    ax1.set_title(f'AAPL Stock Price Trend - {year}-{month:02d}')
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Closing Price (USD)")
    ax1.grid(alpha=0.3)

    ret = df["Daily_Return"].dropna()
    ax2.hist(ret, bins=25, alpha=0.7, color='#cc79a7')
    ax2.set_title('Daily Return Distribution')
    ax2.set_xlabel("Daily Return")
    ax2.set_ylabel("Frequency")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("### ====== AAPL Stock Analysis ======")
    st.write(f"Period: {year}-{month:02d}")
    st.write(f"Latest Closing Price: {round(df['close'].iloc[-1], 2)} USD")
    st.write(f"Average Daily Return: {round(ret.mean(), 6)}")
    st.write(f"Volatility (Std): {round(ret.std(), 6)}")
