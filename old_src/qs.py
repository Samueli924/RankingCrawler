import re
import time

import requests
import rich

# QS大学全球排名

# def get_school():
#     mysql = MYSQL()
#     qs_list = ["https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3794821.txt"]
#     # url_qs_2020 = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/914824.txt"
#     # url_qs_2021 = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/2057712.txt"
#     # url_qs_2022 = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3740566.txt"
#     # url_qs_2023 = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3816281.txt"
#     for i in range(3794815, 3794845):
#         print(f"start {i}")
#         qs_school = f"https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/{i}.txt"
#         raw_school = requests.get(qs_school, headers=HEADERS).json()
#         # school_uid, school_name, school_region, school_country, school_city, school_logo, school_profile
#         all_school = len(raw_school["data"])
#         count = 1
#         for school in raw_school["data"]:
#             # 上传学校基础信息
#             if mysql.get_school_name(school["nid"]) is None:
#                 school_name = re.findall("<a.*?>(.*?)</a>", school["title"])[0]
#                 school_logo = str("https://www.topuniversities.com") + str(school["logo"])
#                 school_profile = str("https://www.topuniversities.com") + str(re.findall("<a href=\"(.*?)\" class", school["title"])[0])
#                 mysql.add_school((school["nid"], school_name, school["region"], school["country"], school["city"], school_logo, school_profile))
#                 print(f"{count}/{all_school}: {school_name}信息上传成功")
#
#             count += 1

        # 上传学校排名信息
        # add_record("qs_2020", (school["nid"], school["rank_display"], school["score"]))
        # print(f"{count}/{all_school}信息上传成功")
        # count += 1


# def get_qs_subject():
#     data = [['Accounting and Finance', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/accounting-finance'], ['Agriculture & Forestry', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/agriculture-forestry'], ['Anatomy & Physiology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/anatomy-physiology'], ['Anthropology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/anthropology'], ['Archaeology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/archaeology'], ['Architecture & Built Environment', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/architecture-built-environment'], ['Art & Design', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/art-design'], ['Biological Sciences', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/biological-sciences'], ['Business & Management Studies', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/business-management-studies'], ['Chemistry', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/chemistry'], ['Classics & Ancient History', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/classics-ancient-history'], ['Communication and Media Studies', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/communication-media-studies'], ['Computer Science and Information Systems', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/computer-science-information-systems'], ['Dentistry', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/dentistry'], ['Development Studies', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/development-studies'], ['Earth and Marine Sciences', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/earth-marine-sciences'], ['Economics and Econometrics', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/economics-econometrics'], ['Education and Training', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/education-training'], ['Engineering - Chemical', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/chemical-engineering'], ['Engineering - Civil and Structural', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/civil-structural-engineering'], ['Engineering - Electrical and Electronic', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/electrical-electronic-engineering'], ['Engineering - Mechanical', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/mechanical-aeronautical-manufacturing-engineering'], ['Engineering - Mineral & Mining', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/mineral-mining-engineering'], ['Engineering - Petroleum', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/engineering-petroleum'], ['English Language and Literature', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/english-language-literature'], ['Environmental Sciences', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/environmental-sciences'], ['Geography', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/geography'], ['Geology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/geology'], ['Geophysics', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/geophysics'], ['History', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/history'], ['Hospitality & Leisure Management', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/hospitality-leisure-management'], ['Law and Legal Studies', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/law-legal-studies'], ['Library & Information Management', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/library-information-management'], ['Linguistics', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/linguistics'], ['Materials Sciences', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/materials-sciences'], ['Mathematics', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/mathematics'], ['Medicine', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/medicine'], ['Modern Languages', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/modern-languages'], ['Nursing', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/nursing'], ['Performing Arts', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/performing-arts'], ['Pharmacy & Pharmacology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/pharmacy-pharmacology'], ['Philosophy', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/philosophy'], ['Physics & Astronomy', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/physics-astronomy'], ['Politics', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/politics'], ['Psychology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/psychology'], ['Social Policy & Administration', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/social-policy-administration'], ['Sociology', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/sociology'], ['Sports-Related Subjects', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/sports-related-subjects'], ['Statistics and Operational Research', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/statistics-operational-research'], ['Theology, Divinity & Religious Studies', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/theology-divinity-religious-studies'], ['Veterinary Science', 'https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/veterinary-science']]
#     count = 1
#     for subject_name, subject_link in data:
#         print(f"thread1: subject{count}/{len(data)}: {subject_name}")
#         subject_id = get_subject_id(subject_name)
#         resp = requests.get(subject_link, headers=HEADERS)
#         soup = BeautifulSoup(resp.text, "lxml")
#         nid = soup.find("article")
#         if "Coming Soon" in soup.find("title").text:
#             continue
#         nid = nid.attrs["data-history-node-id"]
#         ranks = requests.get(f"https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/{nid}.txt", headers=HEADERS).json()["data"]
#         # school_uid, school_ranking, school_score, subject_id
#         for rank in ranks:
#             add_subject_record("qs_subject_2021", (rank["nid"], rank["rank_display"], rank["score"], subject_id))
#         count += 1


if __name__ == '__main__':
    get_school()