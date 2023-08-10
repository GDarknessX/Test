import serial
import streamlit as st

# 打开串口
ser = serial.Serial('COM3', 9600)

# 创建Streamlit应用程序
st.title('Arduino Remote Control')

# 创建按钮来控制开关状态
on_button = st.button('Turn On')
off_button = st.button('Turn Off')

# 根据按钮状态发送指令到Arduino
if on_button:
    ser.write(b'1')
    st.write('LED is ON')
elif off_button:
    ser.write(b'0')
    st.write('LED is OFF')
