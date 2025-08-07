import joblib

# 加载你训练好的模型
model = joblib.load("sentiment_model.pkl")

print("✅ 模型已加载。现在你可以输入英文句子进行情绪判断。")
print("输入 q 可退出。\n")

while True:
    user_input = input("📝 请输入一句英文影评：\n> ")
    if user_input.lower() == "q":
        print("👋 退出程序。")
        break

    # 使用模型预测
    prediction = model.predict([user_input])[0]

    # 输出结果
    if prediction == 1:
        print("🟢 情绪判断：积极 😄\n")
    else:
        print("🔴 情绪判断：消极 😞\n")