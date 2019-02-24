# app/robo_advisor.py
#REFERENCE: used Prof. Rossetti's screencast

import requests
import json
from datetime import datetime


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response)) # <class 'requests.models.Response'>
# print(response.status_code) #>200
# print(response.text)
# TODO: write some Python code here to produce the desired functionality...

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#breakpoint()


print("-----------------------")
print("STOCK SYMBOL: AMZN")
print("-----------------------")
print("REQUESTING STOCK MARKET DATA...")
#Referenced datetime documentation: https://docs.python.org/3/library/datetime.html
#Referenced datetime strftime behavior documentation: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print("REQUEST AT: ", datetime.now().strftime('%m-%d-%Y %H:%M:%S'))
print("-----------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $1000.00")
print("RECENT HIGH: $1,222.00")
print("RECENT LOW: $999.00")
print("-----------------------")
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print("-----------------------")
print("HAPPY INVESTING!")
print("-----------------------")


# ... etc.
