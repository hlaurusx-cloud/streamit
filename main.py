import streamlit as st

st.title("AI Demo with Streamlit")
name = st.text_input("请输入你的名字")
if st.button("打招呼"):
    st.write(f"你好，{name}！这是一个Streamlit示例。")
