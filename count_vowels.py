from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("strings", nargs="+")
    return parser.parse_args()


def vowels_check(args):
    vowels = set("aiueoAIUEO")
    count = 0
    for i, string in enumerate(args.strings, 1):
        vowel_number = sum(1 for c in string if c in vowels)
        count += vowel_number
        print(f"{i}つ目の文字列: \"{string}\"（母音数: {vowel_number}）")
    print(f"合計の母音数: {count}")


def main():
    args = parse_args()
    vowels_check(args)


if __name__ == "__main__":
    main()
