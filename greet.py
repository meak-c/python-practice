from sys import argv, exit


def parse_argv():
    if len(argv) != 3:
        exit("名前と年齢の合計2つの引数を入力してください（例: python greet.py Alice 22）")

    name = argv[1]
    try:
        age = int(argv[2])
    except ValueError:
        exit("年齢は整数で入力してください")

    if age < 0 or age > 130:
        exit("正しい年齢を入力してください")

    return name, age


def greet(name, age):
    print(f"こんにちは、{name}さん（{age}歳）！")


def main():
    name, age = parse_argv()
    greet(name, age)


if __name__ == "__main__":
    main()
