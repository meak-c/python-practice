import math
import random

# 問題1
nums = [3, 5, 8, 10, 15]
sqrt_ceil_nums = [math.ceil(math.sqrt(num)) for num in nums]
print(sqrt_ceil_nums)

# 問題2
total = 0
for _ in range(3):
    total += random.randint(1, 6)
print(total)

# 問題3
players = ["みーく", "さくら", "たけし", "あい", "りく"]
random.shuffle(players)
print(players)

# 問題4
for _ in range(10):
    print(random.gauss(100, 15))

# 問題5
names = ["みーく", "りん", "ゆう", "ひろ", "けい"]
print(f"今日のラッキーさん: {random.choice(names)}")
