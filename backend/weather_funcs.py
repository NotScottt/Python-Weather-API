import requests
from bs4 import BeautifulSoup
import schedule
from datetime import datetime, timedelta

r = requests.get("https://forecast7.com/de/50d9811d03/erfurt/")
doc = BeautifulSoup(r.content, 'html.parser')
today = datetime.now()


def get_current_temp():
    items = [
        item.get_text(strip=True) for item in doc.find(class_="current-conditions")
    ]
    return items[1]

def getConditionNow():
    items = [
        item.get_text(strip=True) for item in doc.find(class_="current-conditions")
    ]
    return items[3]

def return_days(**kwargs):
    when=kwargs.get("when", None)
    asJson = kwargs.get("asJson", False)

    days = get_day(None)
    temp = get_temp(None) 
    info = get_info(None)

    
    items = []
    json_items = {}

    if asJson == True:
        print("hello")
        for i in range(0, 8):
            new_date = today + timedelta(days=i)
            format = "%d.%m.%Y"
            result = new_date.strftime(format)

            json_list = {
                "day": days[i],
                "temp": temp[i],
                "condition": info[i],
                "date": result
            }
            items.append(json_list)
    else:
        for i in range(0, 8):
            new_date = today + timedelta(days=i)
            format = "%d.%m.%Y"
            result = new_date.strftime(format)

            day_temp_info_result = [days[i], temp[i], info[i], result]
            items.append(day_temp_info_result)
            # day_temp_info_result = {days[i], temp[i], info[i], result}
            # items.append(day_temp_info_result)

    # items = [str(x) for x in items]

    if when == None:
        return items
    else:
        return [items[when]]



def get_day(num):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="time")
    ]
    if num == None:
        return items
    else:
        return items[num]
    
def get_temp(num):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="hiTemp")
    ]
    if num == None:
        return items
    else:
        return items[num]
    
def get_info(num):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="summary")
    ]
    if num == None:
        return items
    else:
        return items[num]

# print(return_days(asJson=True))