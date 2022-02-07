from datetime import datetime

if __name__ == "__main__":
    date = datetime.now().strftime("%Y-%m-%d")
    print(f'今日の日付 : {date}')