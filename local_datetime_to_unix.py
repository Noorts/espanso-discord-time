import os
from datetime import datetime

date_time_raw = os.environ['ESPANSO_FORM1_NAME']
date_time = datetime.strptime(date_time_raw, '%d-%m-%Y %H:%M')

print(int(datetime.timestamp(date_time)))