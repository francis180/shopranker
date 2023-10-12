import sched
import time
from datetime import datetime, timedelta
import os
import sys
import django
import requests
from dotenv import load_dotenv
import time

load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopranks.settings")
django.setup()
from authorization.models import User

REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
# Create a scheduler
scheduler = sched.scheduler(time.time, time.sleep)

# Calculate the time until 00:00
now = datetime.now()
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
if now >= midnight:
    midnight += timedelta(days=1)
delay = (midnight - now).total_seconds()

# Define a function to be scheduled
def refresh_data():
    print("Refreshing data at: " + str(datetime.now()))
    for user in User.objects.all():
        groups = user.group_set.all()
        for group in groups:
            domains = group.domain_set.all()
            for domain in domains:
                keywords = domain.keyword_set.all()
                for keyword in keywords:
                    response = requests.get(
                        "http://localhost:8000/keywords/refresh_keyword?domain="
                        + domain.domain_url
                        + "&keyword="
                        + keyword.keyword
                        + "&location="
                        + domain.location_abbr
                        + "&user="
                        + user.username
                        + "&bearer="
                        + REFRESH_TOKEN
                    )
    
    # Schedule the task to run again at the next midnight
    scheduler.enter(delay, 1, refresh_data, ())

if __name__ == '__main__':
    time.sleep(120)
    refresh_data()

    # Start the scheduler
    scheduler.run()
