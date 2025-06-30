from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("string", nargs="+")
    return parser.parse_args()


def display_result(args):
    for i, s in enumerate(args.string, 1):
        print(f"{i}つ目の文字列: \"{s}\"（長さ: {len(s)}）")
    print(f"合計の長さ: {sum(len(s) for s in args.string)}")


def main():
    args = parse_args()
    display_result(args)


if __name__ == "__main__":
    main()
