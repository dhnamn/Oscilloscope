from turtle import delay
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Khởi tạo kết nối UART
ser = serial.Serial(
    port='COM8',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

# Thiết lập đồ thị
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], lw=2)

# Khởi tạo giới hạn ban đầu cho trục x
ax.set_xlim(0, 20)
ax.set_ylim(0, 3.3)

def update(frame):
    # Đọc dữ liệu từ UART
    data = ser.readline().decode('utf-8').rstrip() 
    # data(0 -> 4096) tương ứng điện áp (0 -> 3.3V)
    y = float(data) / 4096 * 3.3  
    xdata.append(frame)
    ydata.append(y)
    line.set_data(xdata, ydata)
    # Cập nhật giới hạn trục x để cuộn trục
    ax.set_xlim(frame-20, frame+1)
    delay(50)
    return line,

ani = FuncAnimation(fig, update, frames=range(1000), blit=False, interval=50)
plt.show()
