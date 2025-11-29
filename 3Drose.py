import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# 定义参数范围
u = np.linspace(0, 2*np.pi, 200)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)

# 更复杂的玫瑰方程
# 使用多个正弦和余弦函数组合创建花瓣形状
k = 5  # 花瓣数量
r = 0.8 * (np.sin(k*u)**2 * np.cos(k*v)**2 + 0.5)
x = r * np.sin(u) * np.cos(v)
y = r * np.sin(u) * np.sin(v)
z = r * np.cos(u)

# 添加一些随机噪声使表面更自然
np.random.seed(42)
noise = 0.05 * np.random.randn(*x.shape)
x += noise
y += noise
z += noise

# 绘制3D曲面
surface = ax.plot_surface(x, y, z, cmap='RdPu', linewidth=0, 
                          antialiased=True, alpha=0.9, rstride=1, cstride=1)

# 添加颜色条
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

# 设置坐标轴
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('复杂3D玫瑰', fontsize=16)

# 设置视角
ax.view_init(elev=25, azim=45)

# 美化图形
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# 显示图形
plt.tight_layout()
plt.show()