import requests
import os


WAKATIME_API_KEY = os.environ.get('WAKATIME_API_KEY')

response = requests.get(
    'https://wakatime.com/api/v1/users/xvnvdu/stats',
    headers={"Authorization": f"Bearer {WAKATIME_API_KEY}"},
).json()

editors = response['data']['editors']
languages = response['data']['languages']
operating_systems = response['data']['operating_systems']
total_time = response['data']['human_readable_total_including_other_language']
daily_average = response['data']['human_readable_daily_average_including_other_language']
