a = int(input("整数を入力してください : "))
b = int(input("整数を入力してください : "))
c = int(input("整数を入力してください : "))

if a == b == c:
    print("全て等しい")
elif a == b or b == c or c == a:
    print("2つが等しい")
else:
    print("全て異なる")
    
n = int(input("整数を入力してください : "))

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
    
is_holiday = input("休日ですか？ y/n : ") == "y"
is_rainy = input("雨ですか？ y/n : ") == "y"
 
if is_holiday is True and is_rainy is False:
    print("ピクニックに行く")
elif is_holiday is True and is_rainy is True:
    print("家で映画を見る")
elif is_holiday is False and is_rainy is False:
    print("仕事へ行く")
elif is_holiday is False and is_rainy is True:
    print("在宅勤務する")