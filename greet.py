from sys import argv, exit

if len(argv) != 3:
    exit("名前と年齢の合計2つの引数を入力してください（例: python greet.py Alice 22）")

name = argv[1]
try:
    age = int(argv[2])
except ValueError:
    exit("年齢は整数で入力してください")

print(f"こんにちは、{name}さん（{age}歳）！")
