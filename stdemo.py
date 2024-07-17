import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import datetime
from datetime import timedelta

st.title("💬 Chatbot")
# 創建文字輸入框
user_input = st.text_input("請輸入一些文字:")

# 顯示使用者輸入的內容
st.write("你輸入的內容是:", user_input)


# 創建一個按鈕
if st.button('點擊我有驚喜'):
    # 按下按鈕後彈出彩帶
    st.balloons()

# 設置應用的標題
st.title("簡單計算機")

# 創建兩個數字輸入框
num1 = st.number_input("輸入第一個數字", format="%.2f")
num2 = st.number_input("輸入第二個數字", format="%.2f")

# 創建操作選擇框
operation = st.selectbox("選擇操作", ["加法", "減法", "乘法", "除法"])

# 計算結果
result = None
if operation == "加法":
    result = num1 + num2
elif operation == "減法":
    result = num1 - num2
elif operation == "乘法":
    result = num1 * num2
elif operation == "除法":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("除數不能為零")

# 顯示結果
if result is not None:
    st.write(f"結果：{result}")

# 添加一個按鈕來觸發計算
if st.button("計算"):
    st.balloons()  # 添加彩帶效果