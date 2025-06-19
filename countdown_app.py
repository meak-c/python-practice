from datetime import date, datetime
import re
import sys


def get_input_date() -> date:
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}$")

    while True:
        date_str = input("予定日を入力してください（例: 2025-01-01）: ").strip()

        if not pattern.fullmatch(date_str):
            print("入力形式が正しくありません。例: 2025-01-01")
            continue

        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("存在しない日付です。再入力してください。")


def calculate_days_left(target: date) -> int:
    return (target - date.today()).days


def display_result_message(days_left: int) -> None:
    match days_left:
        case d if d < 0:
            print("その日はもう過ぎています！”")
        case 0:
            print("今日は予定日です！")
        case _:
            print(f"あと {days_left} 日です！")


def main() -> None:
    try:
        target_date = get_input_date()
        days_left = calculate_days_left(target_date)
        display_result_message(days_left)
    except KeyboardInterrupt:
        print("\n処理が中断されました。")
        sys.exit(0)


if __name__ == "__main__":
    main()
