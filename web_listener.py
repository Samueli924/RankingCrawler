import json
from flask import Flask, render_template, request
from utils.rank_sql import MYSQL

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "Samueli924"


@app.route("/", methods=["GET"])
def rank():
    return render_template("rank.html")


@app.route("/fussySearch", methods=["GET"])
def fussy_search():
    mysql = MYSQL()
    key = request.args.get("key")
    ret = mysql.fussy_search_school(key)
    return {"code": 200, "data": list(map(lambda x: x[0], ret))}


@app.route("/exactSearch", methods=["GET"])
def exact_search_college():
    mysql = MYSQL()
    key = str(request.args.get("key")).lstrip().rstrip()
    school_id = mysql.get_school_id(key)
    ret = mysql.exact_search_school(school_id)
    return {'code': 200, "data": ret}


@app.route("/getAllSubjects", methods=["GET"])
def get_all_subjects_flask():
    mysql = MYSQL()
    return {"code": 200, "data": mysql.get_all_subjects()}


@app.route("/subjectSearch", methods=["GET"])
def subject_search():
    mysql = MYSQL()
    school_refer = mysql.get_school_refer()
    subject_rank = mysql.exact_search_subject(str(request.args.get("key")).lstrip().rstrip())
    # print(school_refer)
    ret_data = list(map(lambda x: [school_refer[str(x[0])] if str(x[0]) in school_refer else "Unknown", x[1]], subject_rank))
    return {"code": 200, "data": ret_data}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
