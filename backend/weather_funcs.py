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


def get_element(className, elementNum):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_=className)
    ]
    if elementNum == None:
        return items
    else:
        return items[elementNum]


def return_days(**kwargs):
    when=kwargs.get("when", None)
    asJson = kwargs.get("asJson", False)

    days = get_element("time", None)
    temp = get_element("hiTemp", None)
    info = get_element("summary", None)
    loTemp = get_element("loTemp", None)
    
    
    items = []
    json_items = {}

    if asJson == True:
        for i in range(0, 8):
            new_date = today + timedelta(days=i)
            format = "%d.%m.%Y"
            result = new_date.strftime(format)

            json_list = {
                "day": days[i],
                "temp": temp[i],
                "condition": info[i],
                "date": result,
                "loTemp": loTemp[i],
                "intTempHi": temp[i][:-2],
                "intTempLo": loTemp[i][:-2]
            }
            items.append(json_list)
    else:
        for i in range(0, 8):
            new_date = today + timedelta(days=i)
            format = "%d.%m.%Y"
            result = new_date.strftime(format)

            day_temp_info_result = [days[i], temp[i], info[i], result, loTemp[i]]
            items.append(day_temp_info_result)

    if when == None:
        return items
    else:
        return [items[when]]