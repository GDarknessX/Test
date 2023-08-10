import streamlit as st
import serial

st.title("Arduino 通信示例")

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

if st.button("发送数据到 Arduino"):
    write_data("Hello from Streamlit!")
    st.success("数据已发送")

received_data = read_data()
st.write("从 Arduino 接收到的数据:", received_data)
在此示例中，我们首先导入了 streamlit 和 serial 模块。然后，我们创建了一个简单的 Streamlit 应用，它允许您通过点击按钮将数据发送到 Arduino，并显示从 Arduino 接收到的数据。

请注意，在上述示例中，您需要根据您的实际情况修改串口号（如 'COM3'）和波特率（如 9600）。确保您已经连接了 Arduino 并配置好了串口通信。






