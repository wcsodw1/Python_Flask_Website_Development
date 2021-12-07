# python MemberRegister.py
# MongoDB link : sign up with MongoDB

# 1.Preprocessing : Prepared for Database-Connecti0n
from typing import Collection
from flask import *
import pymongo

# 1.1 連線網址 : 確認與MongoDB database連結的位置
client = pymongo.MongoClient(
    "mongodb+srv://wcsodw1:<password>@davidcluster.8dgjk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.member  # database name : member_system
collection = db.david

print("Database-Server Connection Success!")
# ===========================================


# 2.Initial Flask Server Program :
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = "Any string but secret"
# =======================================

# 3.Route(處理路由) :


@app.route("/")
def index():
    return render_template("Register.html")


@app.route("/member")
def member():
    return render_template("member.html")

# 設計彈性訊息設定!
# 設計客製化訊息 : /error?msg=

# (!) Set the error route(設定錯誤訊息連結網址)


@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤, 請聯繫客服")
    return render_template("error.html", message=message)


# ========================================
# 3.2 (!!)Set up Sign-Up Route(建立註冊路由) :


@app.route("/signup", methods=["POST"])
def signup():
    # 1.從前端接受訊息 :
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    #print(name, email, password)
    # 2.設定與資料庫互動的集合名稱 :
    collection = db.user

    # 3.把料放進資料庫, 完成註冊
    collection.insert_one({
        "nickname": name,
        "email": email,
        "password": password
    })
    # return "Done!"


''''''
# 4.Run the server :
app.run(port=1500)
