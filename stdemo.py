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