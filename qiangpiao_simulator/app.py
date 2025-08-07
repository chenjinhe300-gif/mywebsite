from flask import Flask, render_template, jsonify, request
import threading

app = Flask(__name__)

票数 = 1
锁 = threading.Lock()
抢票成功者 = None  # 新增：记录抢票成功的人

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/qiang", methods=["POST"])
def 抢票():
    global 票数, 抢票成功者
    data = request.get_json()
    name = data.get("name", "匿名用户")

    with 锁:
        if 票数 > 0:
            票数 -= 1
            抢票成功者 = name
            return jsonify({"message": f"🎉 恭喜 {name} 抢到票！"})
        else:
            return jsonify({"message": f"票已抢光 😢（{抢票成功者} 抢到了）"})

if __name__ == "__main__":
    app.run(debug=True)