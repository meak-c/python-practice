import math
import random
from util.stats_tools import average, max_diff

# 問題6
random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print(f"平均: {average(random_numbers):.2f}")
print(f"最大値と最小値の差: {max_diff(random_numbers)}")

# 問題7
for _ in range(5):
    radius = random.randint(1, 10)
    print(f"面積: {math.pi * radius ** 2:.2f}, 円周: {2 * math.pi * radius:.2f}")

# 問題8
total = 100
over50_counter = 0
for _ in range(total):
    rand = random.gauss(50, 10)
    print(rand)
    if rand >= 50:
        over50_counter += 1

rate = (over50_counter / total) * 100
print(f"50以上のデータは {over50_counter} 個, 全体の {rate:.2f}%")

# 問題9
dice_result = {}
repeat_count = 1000
for _ in range(repeat_count):
    rand = random.randint(1, 6)
    dice_result[rand] = dice_result.get(rand, 0) + 1

sorted_dice_result = dict(sorted(dice_result.items()))

print("各目の出現回数と出現割合")
for pip, count in sorted_dice_result.items():
    rate = (count / repeat_count) * 100
    print(f"{pip}: {count}回, 出現割合: {rate:.2f}%")

mode_pip = max(sorted_dice_result.items(), key=lambda x: x[1])[0]
print(f"最も多く出た目は {mode_pip}")

# 問題10
people = ["Alice", "Bob", "Carol", "Dave", "Eve"]

choiced_person = [random.choice(people) for _ in range(2)]
sampled_person = random.sample(people, 2)

print(choiced_person)
print(sampled_person)
