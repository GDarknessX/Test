import requests
import streamlit as st

st.title('请先检测脉搏')

# 创建按钮来控制开关状态
on_button = st.button('开始')
off_button = st.button('停止')

# 根据按钮状态发送请求到 Flask Web 服务
if on_button:
    response = requests.post('http://127.0.0.1:5000/control', data='on')
    st.write(response.text)
elif off_button:
    response = requests.post('http://127.0.0.1:5000/control', data='off')
    st.write(response.text)

