from math import sqrt


def get_integer():
    try:
        n = int(input("2以上の整数を入力してください: "))
        assert n >= 2, "2以上の整数を入力してください"
    except ValueError:
        print("入力は2以上の整数に限ります。")
        return
    else:
        return n


def is_prime(n: int):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True


def find_upper_prime(n: int):
    m = n
    while True:
        if not is_prime(n):
            n += 1
            continue
        return (n, abs(n - m))


def find_lower_prime(n: int):
    m = n
    while n >= 2:
        if not is_prime(n):
            n -= 1
            continue
        return (n, abs(n - m))


def compare_two_prime(larger, smaller):
    lprime, ldistance = larger
    sprime, sdistance = smaller

    if ldistance <= sdistance:
        return lprime
    return sprime


def main():
    n = get_integer()
    result = compare_two_prime(find_upper_prime(n), find_lower_prime(n))
    print(f"{n} に最も近い素数は {result} です。")


if __name__ == "__main__":
    main()
