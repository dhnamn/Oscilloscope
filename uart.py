import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Khởi tạo kết nối UART
ser = serial.Serial('/dev/ttyUSB0', 9600)  
import pandas as pd

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
    
    return line,

ani = FuncAnimation(fig, update, frames=range(1000), blit=False, interval=50)
plt.show()
