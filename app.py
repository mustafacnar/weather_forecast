import requests
from bs4 import BeautifulSoup
from pprint import pprint

weather_forecast_xml = "https://www.mgm.gov.tr/FTPDATA/analiz/sonSOA.xml"


def weather_forecast():
    weather_forecast_data = requests.get(weather_forecast_xml)
    soup = BeautifulSoup(weather_forecast_data.content, "lxml", from_encoding="utf-8")
    city_data = soup.find_all("sehirler")
    data_dict = dict()

    for index in city_data:
        data_list = dict()
        data_list["date"] = soup.find("tarih").text
        data_list['degree'] = index.select_one("mak").text
        data_list['status'] = index.select_one("durum").text
        data_dict[index.select_one("ili").text] = data_list
    pprint(data_dict)
    return data_dict


weather_forecast()
