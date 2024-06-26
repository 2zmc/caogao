import math
import matplotlib.pyplot as plt
import matplotlib
# 使用交互式后端
matplotlib.use('TkAgg')  # 你也可以试试其他后端比如 'QtAgg'
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


x = [0, 5]
y = [0, 0]
plt.plot(x, y)
plt.show()

