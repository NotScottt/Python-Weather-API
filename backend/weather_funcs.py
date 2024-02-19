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
    infos_list = get_all_infos()

    items = []
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
                "intTempLo": loTemp[i][:-2],   
            }

            json_list.update(infos_list[i])
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



def liste_abbrechen(original_liste, schrittweite):
    resultierende_liste = []
    teil_liste = []

    for i, element in enumerate(original_liste, start=1):
        teil_liste.append(element)
        if i % schrittweite == 0:
            resultierende_liste.append(teil_liste)
            teil_liste = []

    if teil_liste:
        resultierende_liste.append(teil_liste)
    return resultierende_liste


def liste_in_dict(liste):
    ergebnis = []

    for eintrag in liste:
        eintrag_dict = {}
        for element in eintrag:
            key, value = element.split(': ')
            eintrag_dict[key] = value
        ergebnis.append(eintrag_dict)

    return ergebnis


def get_all_infos():
    span_elements = doc.select('div.more-details span')
    span_list = []

    for span in span_elements:
        span_list.append(span.text)
    
    result_list = liste_abbrechen(span_list, 8)
    list_dict = liste_in_dict(result_list)
    return list_dict


# for hourItem in doc.find_all('div',  attrs={'class': 'hourly'})