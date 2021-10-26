# python Ch22_FrontEnd_MemberSystem.py
# MongoDB link : sign up with MongoDB

# 1.Preprocessing : Prepared for Database-Connecti0n
from flask import *
import pymongo

# 1.1 連線網址 : 確認與MongoDB database連結的位置
client = pymongo.MongoClient(
    "mongodb+srv://root:<password>@mycluster.gpvb7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.member_system  # database name : member_system
print("Database-Server Connection Success!")

# 2.Initial Flask Server Program :
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = "Any string but secret"

# 3.Route(處理路由) :


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/member")
def member():
    return render_template("member.html")


# 4.Run the server :
app.run(port=3000)
