import requests
from bs4 import BeautifulSoup

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36"}

Topuniversities_raw_path = "saves/topuniversities/"

TimesRanking_raw_path = "saves/timesranking"

TimesRanking_dict = {
    "2022": "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2022_0__e7070f0c2581be5fe6ab6392da206b36.json",
    "2021": "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2021_0__fa224219a267a5b9c4287386a97c70ea.json",
    "2020": "https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2020_0__24cc3874b05eea134ee2716dbf93f11a.json",
}


def fs(text: str):
    return text.replace("\n", "").replace("\r", "").replace("\t", "").lstrip().rstrip()


def get_soup(url):
    """
    Get Beautifulsoup4 based bs4 node
    :param url: link
    :return: Beautifulsoup node
    """
    __resp = requests.get(url, headers=HEADERS)
    __soup = BeautifulSoup(__resp.text, "lxml")
    return __soup


def get_json(url):
    """
    Get JSON based data
    :param url: link
    :return: JSON format data
    """
    __resp = requests.get(url, headers=HEADERS)
    return __resp.json()


def get_resp(url):
    """
    get Requests based resp
    :return: resp node
    """
    return requests.get(url, headers=HEADERS)