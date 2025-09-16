import streamlit as st

st.title("웹 애플리케이션")

st.header(" 값 입력")
col1, col2 = st.columns(2)

with col1:
    A = st.number_input("숫자 A", value=5.0,  format="%.6f", step=1.0)
with col2:
    B = st.number_input("숫자 B", value=3.0,  format="%.6f",step=1.0)

# --- 第一项：两数相加 ---
st.header("두 값이 더하기")
if st.button("A + B"):
    sum = A + B
    st.success(f"A + B = {sum}")
