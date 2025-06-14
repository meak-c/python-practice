import numpy as np
import time

N = 16384  # ここが限界チャレンジサイズ！

A = np.random.rand(N, N)
B = np.random.rand(N, N)

start = time.time()
C = np.dot(A, B)
end = time.time()

print(f"処理時間: {end - start:.2f} 秒")
