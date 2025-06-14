from datetime import date, datetime, timedelta
import time

# 問題1
today = date.today()
print(f"今日の日付: {today.strftime('%Y年%m月%d日')}")

# 問題2
now = datetime.now()
print(f"現在の時刻: {now.strftime('%H時%M分%S秒')}")

# 問題3
today_dt = date.today()
after_10_days = today_dt + timedelta(days=10)
print(f"10日後は {after_10_days.strftime('%Y-%m-%d')} です")

# 問題4
time.sleep(5)
print("処理完了！")

# 問題5
date_dt = datetime(2024, 12, 25, 18, 30, 0)
print(date_dt.strftime('%Y年%m月%d日 %H時%M分%S秒'))

# 問題6
data_parse = datetime.strptime("2025-07-01 14:45:00", "%Y-%m-%d %H:%M:%S")
print(data_parse.strftime('%Y年%m月%d日 %H時%M分%S秒'))

# 問題7
print(time.time())
print(time.localtime())
