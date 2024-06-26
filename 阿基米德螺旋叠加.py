import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 使用交互式后端
matplotlib.use('TkAgg')  # 你也可以试试其他后端比如 'QtAgg'
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


# 画一个n*n的线段
def n_n(n1, n2):
    X_y = [n1, n2]
    print(X_y)
    return np.array(X_y)


# x y 函数计算两个点之间的距离
def x_y(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)) ** 2 + (y2 - y1) ** 2
    return distance


def draw_x_y(points):
    plt.figure()
    x_vals, y_vals = zip(*points)  # 解压点列表到 x 和 y 值
    plt.plot(x_vals, y_vals, marker='o', label="点")
    plt.title("螺旋图")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def main():
    point1 = (0, 0)
    point2 = (5, 5)
    long = x_y(point1, point2)
    draw_x_y(point2)


if __name__ == "__main__":
    main()
