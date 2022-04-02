import datetime
import time

today  = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
previous_date = datetime.datetime.today() - datetime.timedelta(days=1)

print('yesterday: {}'.format(previous_date.strftime("%Y-%m-%dT%H:%M:%S")))
