import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Углы поворота
alpha = -np.arccos(1/8)
beta = -np.arccos(np.sqrt(7)/4)
gamma = 0  # Угол поворота вокруг оси Oz равен 0

# Матрицы поворота
Rx = np.array([[1, 0, 0],
               [0, np.cos(alpha), -np.sin(alpha)],
               [0, np.sin(alpha), np.cos(alpha)]])

Ry = np.array([[np.cos(beta), 0, np.sin(beta)],
               [0, 1, 0],
               [-np.sin(beta), 0, np.cos(beta)]])

Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0],
               [np.sin(gamma), np.cos(gamma), 0],
               [0, 0, 1]])

# Комбинированная матрица поворота
R = np.dot(Rz, np.dot(Ry, Rx))

# Вершины тетраэдра
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

# Преобразование вершин
transformed_vertices = np.dot(vertices, R.T)

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Оси
axes = np.array([[0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1]])
transformed_axes = np.dot(axes[:, 3:], R.T)
for i in range(len(axes)):
    ax.quiver(*axes[i, :3], *transformed_axes[i], arrow_length_ratio=0.1)

# Тетраэдр
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)]
for edge in edges:
    ax.plot3D(*zip(*transformed_vertices[[edge[0], edge[1]]]), color="b")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
