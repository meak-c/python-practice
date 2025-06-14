from datetime import date, datetime
import re


def get_date() -> date:
    while True:
        date_str = input("予定日を入力してください (例: 2025-01-01): ")
        if not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
            print("形式が正しくありません。再入力してください。")
            continue
        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            return target_date
        except ValueError:
            print("存在しない日付です。再入力してください。")


def calculate_date_diff(target_date: date) -> int:
    today = date.today()
    date_diff = (target_date - today).days
    return date_diff


def display_date_diff(date_diff: int) -> None:
    print(f"あと {date_diff} 日です!")


def main():
    target_date = get_date()
    date_diff = calculate_date_diff(target_date)
    display_date_diff(date_diff)


main()
