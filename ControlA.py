import requests
import streamlit as st

st.title('Arduino Remote Control')

# 创建按钮来控制开关状态
on_button = st.button('Turn On')
off_button = st.button('Turn Off')

# 根据按钮状态发送请求到 Flask Web 服务
if on_button:
    response = requests.post('http://127.0.0.1:5000/control', data='on')
    st.write(response.text)
elif off_button:
    response = requests.post('http://127.0.0.1:5000/control', data='off')
    st.write(response.text)

