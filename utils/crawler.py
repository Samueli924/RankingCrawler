import json

import requests

from loguru import logger
from bs4 import BeautifulSoup

from utils.globalvar import *


class TopUniverisities:
    def __init__(self):
        pass

    @staticmethod
    def get_soup(url):
        """
        Get Beautifulsoup4 based bs4 node
        :param url: link
        :return: Beautifulsoup node
        """
        __resp = requests.get(url, headers=HEADERS)
        __soup = BeautifulSoup(__resp.text, "lxml")
        return __soup

    @staticmethod
    def get_json(url):
        """
        Get JSON based data
        :param url: link
        :return: JSON format data
        """
        __resp = requests.get(url, headers=HEADERS)
        return __resp.json()

    @staticmethod
    def get_resp(url):
        """
        get Requests based resp
        :return: resp node
        """
        return requests.get(url, headers=HEADERS)

    @staticmethod
    def get_rank_links(_method: str, _year: int = None):
        """
        Get all relative links for ranking
        :param _method: two options( overall / subject )
        :param _year: range from (2020 - 2022/2023)
        :return:
        """
        if _method == "overall":
            return [[f"Overall Ranking({_year})",
                    f"https://www.topuniversities.com/university-rankings/world-university-rankings/{_year}"]]
        elif _method == "subject":
            return list(map(
                lambda x: [fs(str(x.text)), str("https://www.topuniversities.com") + str(x.attrs["href"])],
                sum(list(map(lambda x: x.find_all("a"),
                    TopUniverisities.get_soup(f"https://www.topuniversities.com/subject-rankings/{_year}").find_all(
                    "div", attrs={"class": "select-subj"}))), [])))
        else:
            return [["", ""]]

    @staticmethod
    def get_txt_file_name(_url):
        """
        Get the Final JSON file node_id
        :param _url: link
        :return:
        """
        _resp = requests.get(_url, headers=HEADERS)
        _soup = BeautifulSoup(_resp.text, "lxml")
        return _soup.find("article").attrs["data-history-node-id"]

    @staticmethod
    def get_rank_json_data(_node_id, _file_name):
        data = TopUniverisities.get_json(
            f"https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/{_node_id}.txt")["data"]
        with open(f"{Topuniversities_raw_path}{_file_name}.json", "w") as f:
            json.dump(data, f)
        return data

    @staticmethod
    def start_crawl(_method: str = None, _year: str = None):
        """
        Middle-ware. Used to start crawl job
        :param _method: two options( overall / subject )
        :param _year: target year
        :return:
        """
        ret = list()
        for name, link in TopUniverisities.get_rank_links(_method=_method, _year=_year):
            logger.info(f"TopUniversities开始读取: {name}")
            _node_id = TopUniverisities.get_txt_file_name(link)
            ret.append(TopUniverisities.get_rank_json_data(_node_id, name))
        return ret

    @staticmethod
    def start(_method: str = None, _year: str = None):
        if _method == ("overall" or "subject") and _year:
            return TopUniverisities.start_crawl(_method=_method, _year=_year)
        elif _method == "overall" and (not _year):
            return TopUniverisities.start_crawl(_method=_method, _year="2023")
        elif _method == "subject" and (not _year):
            return TopUniverisities.start_crawl(_method=_method, _year="2022")
        elif not _method:
            ret = list()
            ret.append(TopUniverisities.start_crawl(_method="overall", _year="2023"))
            ret.append(TopUniverisities.start_crawl(_method="subject", _year="2022"))
            return ret
        else:
            logger.error("Wrong Typo")
            return []
