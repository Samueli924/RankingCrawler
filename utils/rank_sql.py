from config.basic_config import *
import mysql.connector


class MYSQL:
    def __init__(self):
        self.myDB = mysql.connector.connect(host=hostname, user=username, password=password, database=database, buffered=True)
        self.myCursor = self.myDB.cursor()

    def add_school(self, val):
        sql = "INSERT INTO school (school_uid, school_name, school_region, school_country, school_city, school_logo, school_profile) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.myCursor.execute(sql, val)
        self.myDB.commit()

    def add_record(self, table, val):
        sql = "INSERT INTO " + table + " (school_uid, school_ranking, school_score) VALUES (%s, %s, %s)"
        self.myCursor.execute(sql, val)
        self.myDB.commit()

    def add_subject(self, val):
        sql = "INSERT INTO subject (subject_name) VALUES (%s)"
        self.myCursor.execute(sql, val)
        self.myDB.commit()

    def add_subject_record(self, table, val):
        sql = "INSERT INTO " + table + " (school_uid, school_ranking, school_score, subject_id) VALUES (%s, %s, %s, %s)"
        self.myCursor.execute(sql, val)
        self.myDB.commit()

    def get_subject_id(self, name):
        sql = f"select subject_id from subject where subject_name = '{name}'"
        self.myCursor.execute(sql)
        return self.myCursor.fetchone()[0]

    def get_all_subjects(self):
        sql = f"select * from subject"
        self.myCursor.execute(sql)
        return self.myCursor.fetchall()

    def fussy_search_school(self, key):
        sql = f"select school_name from school where school_name like '%{key}%'"
        self.myCursor.execute(sql)
        return self.myCursor.fetchall()

    def get_school_id(self, key):
        sql = f"select school_uid from school where school_name = '{key}'"
        self.myCursor.execute(sql)
        return self.myCursor.fetchone()[0]

    def get_school_name(self, key):
        self.myCursor.execute(f"select school_name from school where school_uid = '{key}'")
        return self.myCursor.fetchone()

    def get_school_refer(self):
        self.myCursor.execute(f"select school_uid, school_name from school")
        school_refer = dict()
        for uid, name in self.myCursor.fetchall():
            school_refer[uid] = name
        return school_refer

    def exact_search_school(self, key):
        self.myCursor.execute(f"select school_ranking from qs_2023 where school_uid = '{key}'")
        try:
            qs_2023 = self.myCursor.fetchone()[0]
        except:
            qs_2023 = "None"
        self.myCursor.execute(f"select school_ranking from times_2022 where school_uid = '{key}'")
        try:
            times_2022 = self.myCursor.fetchone()[0]
        except:
            times_2022 = "None"
        self.myCursor.execute(f"select school_ranking from usnews_2022 where school_uid = '{key}'")
        try:
            usnews_2022 = self.myCursor.fetchone()[0]
        except:
            usnews_2022 = "None"
        self.myCursor.execute(f"select school_ranking, subject_id from qs_subject_2022 where school_uid = '{key}'")
        qs_subject_2022 = self.myCursor.fetchall()
        subject_ranking = list()
        for subject in qs_subject_2022:
            self.myCursor.execute(f"select subject_name from subject where subject_id = '{subject[1]}'")
            subject_ranking.append([self.myCursor.fetchone()[0], subject[0]])
        return {"all_rank": {"QS 2023 Ranking": qs_2023, "Times 2022 Ranking": times_2022, "USNEWS 2022 Ranking": usnews_2022}, "subject_rank": subject_ranking}

    def exact_search_subject(self, key):
        self.myCursor.execute(f"select school_uid, school_ranking from qs_subject_2022 where subject_id='{key}'")
        subject_rank = self.myCursor.fetchall()
        return subject_rank
