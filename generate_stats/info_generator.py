from datetime import datetime


today = datetime.now().strftime("%d %B %Y")

def get_time_range():
    return f'From: 18 September 2024 — To: {today}\n'

def get_total_time(data):
    return f'Total Time: {data}\n'

def get_daily_average(data):
    return f'Daily Average Coding: {data}\n'
