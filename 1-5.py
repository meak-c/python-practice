total = 0
add_number = 1
while True:
    total += add_number
    if total > 100:
        print(f"最後の加えた数値は {add_number}")
        break
    add_number += 1
    
while True:
    char = str(input("文字列を入力してください : "))
    if char == "end":
        break
    elif not char:
        continue
    else:
        print(f"入力値 : {char}")
        
num = 1
while num <= 100:
    if num % 3 != 0 and num % 5 != 0:
        print(num)
        num += 1
    else:
        num += 1
        continue
    
n = int(input("正整数値を入力してください : "))
sum = 0
add_num = 1

while True:
    if add_num % 3 == 0:
        add_num += 1
        continue
    sum += add_num
    if sum > n:
        print(f"最後に加えた数値 : {add_num}")
        print(f"合計 : {sum}")
        break
    add_num += 1
    
