from matplotlib import pyplot as plt
import numpy as np


def scatter_plot():
    """
    scatter plot
    """
    # 打开交互模式
    plt.ion()

    # 循环
    for index in range(50):
        # 清除原有图像
        # plt.cla()

        # 设定标题等
        plt.title("动态散点图")
        plt.grid(True)

        # 生成测试数据
        point_count = 5
        x_index = np.random.random(point_count)
        y_index = np.random.random(point_count)

        # 设置相关参数
        color_list = np.random.random(point_count)
        scale_list = np.random.random(point_count) * 100

        # 画散点图
        plt.scatter(x_index, y_index, s=scale_list, c=color_list, marker="o")

        # 暂停
        plt.pause(0.2)

    # 关闭交互模式
    plt.ioff()

    # 显示图形
    plt.show()
    return


scatter_plot()
