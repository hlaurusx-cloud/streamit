import streamlit as st

st.title("웹 애플리케이션")

st.header(" 값 입력")
col1, col2 = st.columns(2)

with col1:
    A = st.number_input("숫자 A", value=5.0,  format="%.6f", step=1.0)
with col2:
    B = st.number_input("숫자 B", value=3.0,  format="%.6f",step=1.0)

# --- 第1项：两数相加 ---
st.header("두 값의 합")
if st.button("A + B"):
    sum = A + B
    st.success(f"A + B = {sum}")

# --- 第2项：A，B之间选择 ---
choice = st.selectbox("A 또는 B 중 선택하시오",options=[("A", A), ("B", B)],format_func=lambda x: f"{x[0]} = {x[1]}")

selected_value = choice[1]

# --- 第3项：从 1 到所选数字的总和 ---
if selected_value > 0:
    n= selected_value
    total = sum(range(1,n + 1))
    st.info(f"선택된 {n}까지의 합 = {total}")
