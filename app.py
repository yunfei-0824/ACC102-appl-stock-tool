import streamlit as st
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AAPL Stock Analysis", layout="wide")
st.title("📊 Apple (AAPL) Stock Price Analysis Tool")

@st.cache_data(show_spinner="正在加载股票数据...")
def load_data():
    try:
        data = ak.stock_us_daily(symbol="AAPL", adjust="")
        data = data[(data["date"] >= "2024-01-01") & (data["date"] <= "2026-04-16")]
        data = data.set_index("date")
        data["Daily Return"] = data["close"].pct_change()
        if not data.empty and len(data) > 1:
            return data
        else:
            st.error("❌ 获取数据为空，请检查网络")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ 数据获取异常: {str(e)}")
        return pd.DataFrame()

data = load_data()

if data.empty:
    st.stop()

st.subheader("📋 最新股票数据")
st.dataframe(data.tail(10))

st.subheader("📈 股价趋势（2024-2026）")
fig1, ax1 = plt.subplots(figsize=(12,5))
ax1.plot(data.index, data["close"], label="AAPL 收盘价", color="#1f77b4", linewidth=2)
ax1.set_title("Apple Stock Price Trend (2024-2026)")
ax1.set_xlabel("日期")
ax1.set_ylabel("收盘价 (USD)")
ax1.legend()
ax1.grid(alpha=0.3)
st.pyplot(fig1)

st.subheader("📊 日收益率分布")
fig2, ax2 = plt.subplots(figsize=(12,3))
ax2.hist(data["Daily Return"].dropna(), bins=50, color="#ff7f0e", alpha=0.7, edgecolor="black")
ax2.set_title("Daily Return Distribution")
ax2.set_xlabel("日收益率")
ax2.set_ylabel("频次")
ax2.grid(alpha=0.3)
st.pyplot(fig2)

st.subheader("📌 核心指标")
latest_close = round(data["close"].iloc[-1], 2)
avg_daily_return = round(data["Daily Return"].mean(), 4)
volatility = round(data["Daily Return"].std(), 4)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="最新收盘价", value=f"{latest_close} USD")
with col2:
    st.metric(label="平均日收益率", value=f"{avg_daily_return}")
with col3:
    st.metric(label="日波动率", value=f"{volatility}")

st.info("💡 提示：波动率越高，代表股票价格波动越大，投资风险越高。")