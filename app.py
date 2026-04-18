import streamlit as st
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AAPL Stock Analysis", layout="wide")
st.title("AAPL  Historical Stock Analysis ")

@st.cache_data(ttl=3600)
def load_data():
    data = ak.stock_us_daily(symbol="AAPL", adjust="")
    data["date"] = pd.to_datetime(data["date"])
    data["year"] = data["date"].dt.year
    data["month"] = data["date"].dt.month
    data["Daily_Return"] = data["close"].pct_change()
    return data

data = load_data()

years = sorted(data["year"].unique())
year = st.selectbox("Select Year", years, index=len(years)-1)
month = st.slider("Select Month", 1, 12, 4)

df = data[(data["year"] == year) & (data["month"] == month)]

if df.empty:
    st.warning(f"No data available for {year}-{month:02d}")
else:
    st.subheader(f"Stock Price Trend: {year}-{month:02d}")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7))

    ax1.plot(df["date"], df["close"], color="#0072b2", linewidth=2)
    ax1.set_title("AAPL Closing Price Trend")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Closing Price (USD)")
    ax1.grid(alpha=0.3)

    ret = df["Daily_Return"].dropna()
    ax2.hist(ret, bins=25, alpha=0.7, color="#cc79a7")
    ax2.set_title("Daily Return Distribution")
    ax2.set_xlabel("Daily Return")
    ax2.set_ylabel("Frequency")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Stock Analysis Metrics")
    st.write(f"**Latest Closing Price**: ${df['close'].iloc[-1]:.2f}")
    st.write(f"**Average Daily Return**: {ret.mean():.6f}")
    st.write(f"**Volatility (Std Dev)**: {ret.std():.6f}")
