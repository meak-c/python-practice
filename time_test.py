import numpy as np
from scipy.optimize import curve_fit
import time

# モデル関数：指数減衰


def model_func(x, a, b, c):
    return a * np.exp(-b * x) + c


# 疑似データ生成
x_data = np.linspace(0, 10, 1_000_000)
y_data = model_func(x_data, 2.5, 1.3, 0.5)
y_data += 0.1 * np.random.normal(size=len(x_data))  # ノイズ追加

# 最適化実行
start = time.time()
popt, pcov = curve_fit(model_func, x_data, y_data, p0=(1.0, 1.0, 1.0))
end = time.time()

print(f"非線形最適化（指数モデル, 100万点）: {end - start:.3f} 秒")
print(f"最適パラメータ: a={popt[0]:.3f}, b={popt[1]:.3f}, c={popt[2]:.3f}")
