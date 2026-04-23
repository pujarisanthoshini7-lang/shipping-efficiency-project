import streamlit as st
import pandas as pd

# Data load
df = pd.read_csv("final_data.csv")

# Title
st.title("🚚 Shipping Efficiency Dashboard")

# State analysis
st.subheader("Average Lead Time by State")
st.bar_chart(df.groupby("State")["Lead Time"].mean())

# Ship mode analysis
st.subheader("Ship Mode Performance")
st.bar_chart(df.groupby("Ship Mode")["Lead Time"].mean())

# Raw data (optional)
if st.checkbox("Show Data"):
    st.write(df)
    state = st.selectbox("Select State", df["State"].unique())

filtered_df = df[df["State"] == state]

st.subheader("Filtered Data")
st.bar_chart(filtered_df.groupby("Ship Mode")["Lead Time"].mean())
st.metric("Avg Lead Time", round(df["Lead Time"].mean(), 2))
st.metric("Max Delay", df["Lead Time"].max())