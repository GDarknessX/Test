import serial

# 打开串口连接
ser = serial.Serial('COM3', 9600)  # 请根据您的串口号和波特率进行设置

# 从串口读取数据
def read_data():
    while True:
        data = ser.readline().decode().strip()
        if data:
            return data

# 向串口写入数据
def write_data(data):
    ser.write(data.encode())

# Streamlit 应用
import streamlit as st

st.title("Arduino 通信示例")

if st.button("发送数据到 Arduino"):
    write_data("Hello from Streamlit!")
    st.success("数据已发送")

received_data = read_data()
st.write("从 Arduino 接收到的数据:", received_data)

