import requests
import json
from difflib import SequenceMatcher
import rich
from utils.rank_sql import MYSQL


def similarity(str_a: str, str_b: str):
    return SequenceMatcher(None, str_a, str_b).ratio()


mysql = MYSQL()
with open("temp/temp.json", "r") as f:
    times = json.loads(f.read())["data"]

schools = mysql.get_school_refer()
exist_schools = list(map(lambda x: schools[x], schools))
start = 644
for index, time_school in enumerate(times):
    if index < start:
        continue
    print(f"读取{index + 1}/{len(times)}所学校")
    most_five = list()
    for school in exist_schools:
        most_five.append([school, similarity(school.split("-")[0].split("(")[0], time_school["name"])])
    most_five.sort(key=lambda x: x[1], reverse=True)
    if most_five[0][1] < 0.8:
        # print(f"{time_school['name']}最匹配的学校是: ")
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
        mysql.add_record("times_2022", (school_uid, time_school["rank"], ""))
