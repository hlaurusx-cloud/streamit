# app.py
import streamlit as st

st.set_page_config(page_title="加法与累加器演示", page_icon="🔢", layout="centered")

st.title("🔢 简易计算器：两数相加 + 选择累加功能")

st.markdown(
    """
请按顺序操作：
1. 在左侧或下方输入两个数字 A 和 B（支持整数或小数）。
2. 点击「计算 A + B」查看结果。
3. 在“选择一个数字”下拉框中选择 A 或 B，点击「累加到选定数」查看从 1 累加到该数的和（当选择值为非正整数时，会给出说明）。
"""
)

# --- 输入区 ---
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

# --- 第二项：选择一个数字并累加到该数 ---
st.header("选择一个数字并累加到该数")

# 在 selectbox 中把当前 A,B 值展示为选项，标签更清晰
option = st.selectbox("选择一个数字（将累加从 1 到该数）", options=[f"A = {A}", f"B = {B}"])

if st.button("累加到选定数"):
    # 从选项解析出数值
    try:
        chosen_value = float(option.split("=")[1].strip())
    except Exception:
        st.error("无法识别选项中的数字。")
        chosen_value = None

    if chosen_value is None:
        pass
    else:
        # 如果是整数且 >= 1，使用等差数列公式；如果是小数或负数，按定义处理并说明
        if chosen_value.is_integer() and chosen_value >= 1:
            n = int(chosen_value)
            # 使用等差数列求和公式
            total = n * (n + 1) // 2
            st.success(f"从 1 累加到 {n} 的和为：{total}")
        elif chosen_value > 0 and not chosen_value.is_integer():
            # 对于正的小数，例如 5.7，我们说明并采用累加到 floor(n)
            import math
            n = math.floor(chosen_value)
            total = n * (n + 1) // 2
            st.info(
                f"你选择的数是正小数 {chosen_value}。按题意通常累加整数项，这里向下取整为 {n} 并计算：1 到 {n} 的和 = {total}。"
            )
        elif chosen_value == 0:
            st.info("你选择的值为 0。按从 1 到 0 的含义，累加结果视为 0（没有正整数项）。")
        else:
            # 负数或其他情况，给出说明并按数学定义累加（例如从 n 到 1）
            n = int(chosen_value)
            if n < 1:
                st.warning(
                    f"你选择的数是 {chosen_value}（非正整数）。题目通常期待正整数累加。"
                    " 如果确实需要累加负数或0，请说明题意。"
                )

# --- 说明和使用示例 ---
st.markdown("---")
st.subheader("说明 / 注意事项")
st.markdown(
    """
- `number_input` 支持整数和小数；为了题目常见要求（“所有数相加”通常指从 1 到某个正整数），我们对非正整数和小数做了友好提示与处理说明。  
- 若你需要严格按 **从 A 到 B（包含负数）** 的累加，请告诉我，我可以修改为支持任意区间累加（并展示计算过程）。  
"""
)
