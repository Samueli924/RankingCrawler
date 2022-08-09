import requests
import json
import rich
from utils.rank_sql import MYSQL
from difflib import SequenceMatcher


def similarity(str_a: str, str_b: str):
    return SequenceMatcher(None, str_a, str_b).ratio()


def get_url(page):
    return f"https://www.usnews.com/education/best-global-universities/search?format=json&page={page}"


def get_json(url):
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.0.0 Safari/537.36"}
    return requests.get(url, headers=HEADERS).json()["items"]


if __name__ == '__main__':
    mysql = MYSQL()
    schools = mysql.get_school_refer()
    exist_schools = list(map(lambda x: schools[x], schools))
    start = 39
    for page in range(1, 202):
        if page < start:
            continue
        print(f"开始页面{page}/201")
        raw = get_json(get_url(page))
        for school in raw:
            school_name = school["name"]
            school_rank = school["ranks"][0]["value"]
            most_five = list()
            for exist_school in exist_schools:
                most_five.append([exist_school, similarity(exist_school, school_name)])
            most_five.sort(key=lambda x: x[1], reverse=True)
            if most_five[0][1] < 0.8:
                # print(f"{school_name}最匹配的学校是: ")
                # for index, item in enumerate(list(map(lambda x: x[0], most_five[:11]))):
                #     print(f"{index + 1}、 {item}")
                # num = int(input("输入最合适的一个学校序号")) - 1
                # if num == -1:
                #     continue
                # elif num == 998:
                #     best = str(input("请输入学校名")).lstrip().rstrip()
                # else:
                #     best = most_five[num][0]
                continue
            else:
                best = most_five[0][0]
            school_uid = mysql.get_school_id(best.replace("'", "''"))
            if not school_uid:
                print("出错，跳过")
            else:
                mysql.add_record("usnews_2022", (school_uid, school_rank, ""))