import requests
import time

# Flask 后端地址
抢票网址 = "http://127.0.0.1:5000/qiang"

# 设置你的用户名
用户名 = "cjh"

尝试次数 = 0

while True:
    尝试次数 += 1
    try:
        response = requests.post(抢票网址, json={"name": 用户名})
        if response.status_code == 200:
            message = response.json()["message"]
            print(f"第 {尝试次数} 次尝试：{message}")

            if "抢到票" in message:
                print("🎉 成功抢到票，程序结束。")
                break
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"请求出错：{e}")

    time.sleep(0.5)  