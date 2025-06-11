nums = [3, 1, 4, 1, 5]
total = 0
for num in nums:
    total += num
    print(total)
    
data = ["A", "B", "C", "D", "E"]
for i, char in enumerate(data):
    if i % 2 == 0:
        print(f"even : {char}")
    else:
        print(f"odd : {char}")
        
count_Fizz = 0
count_Buzz = 0
count_FizzBuzz = 0

for i in range(1, 51):
    if i % 15 == 0:
        count_FizzBuzz += 1
        print("FizzBuzz")
    elif i % 3 == 0:
        count_Fizz += 1
        print("Fizz")
    elif i % 5 == 0:
        count_Buzz += 1
        print("Buzz")
    else:
        print(i)
        
print(f"Fizzは {count_Fizz} 回出力された")
print(f"Buzzは {count_Buzz} 回出力された")
print(f"FizzBuzzは {count_FizzBuzz} 回出力された")