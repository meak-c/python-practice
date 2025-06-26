from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # 🔧 GUIバックエンドを強制指定


# --- 初期設定 ---
G = 1.0          # 万有引力定数
M = 10.0         # 中心天体の質量
m = 1.0          # 惑星の質量（使わないが記述）

# 初期位置と速度
pos = np.array([1.0, 0.0])
vel = np.array([0.0, 2.5])  # 円軌道に相当する速度
dt = 0.01
positions = [pos.copy()]    # 座標履歴リスト

# --- 物理演算の更新 ---


def update():
    global pos, vel
    r = np.linalg.norm(pos)
    acc = -G * M * pos / r**3
    vel += acc * dt
    pos += vel * dt
    positions.append(pos.copy())


# --- 描画設定 ---
fig, ax = plt.subplots()
planet, = ax.plot([], [], 'bo')              # 惑星
trail, = ax.plot([], [], 'b-', lw=0.5)       # 軌跡
star, = ax.plot(0, 0, 'yo', markersize=10)   # 恒星（原点固定）


def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    return planet, trail


def animate(i):
    update()
    planet.set_data(*positions[-1])
    trail.set_data(*zip(*positions))
    return planet, trail


# --- アニメーション構築 ---
ani = FuncAnimation(
    fig, animate, init_func=init,
    frames=1000, interval=20, blit=False
)

plt.title("2-body Gravity Simulation")
plt.show()
