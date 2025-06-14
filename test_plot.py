import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

plt.plot(x, y)
plt.title("日本語タイトルのテスト")
plt.xlabel("横軸")
plt.ylabel("縦軸")

plt.show()
