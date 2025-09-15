import streamlit as st

st.title("🔢 简易计算器：两数相加 + 选择累加功能")

st.header("输入")
col1, col2 = st.columns(2)

with col1:
    A = st.number_input("输入数字 A", value=5.0, format="%.6f", step=1.0)
with col2:
    B = st.number_input("输入数字 B", value=3.0, format="%.6f", step=1.0)

# --- 第一项：两数相加 ---
st.header("两数相加")
if st.button("计算 A + B"):
    sum_ab = A + B
    st.success(f"A + B = {sum_ab}")
