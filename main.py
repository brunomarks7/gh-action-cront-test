import datetime
import os
import time

import messagebird
from dotenv import load_dotenv

load_dotenv()

today = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
previous_date = datetime.datetime.today() - datetime.timedelta(days=1)

MESSAGEBIRD_KEY = os.environ.get('MESSAGEBIRD_KEY')

client = messagebird.Client(str(MESSAGEBIRD_KEY))

message = client.message_create(
    '+5513991389355',
    '+5513991389355',
    'Esse é o SMS da meia noite. Ontem:' + str(previous_date)
)

print(message)
