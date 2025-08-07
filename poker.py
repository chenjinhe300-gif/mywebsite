import tkinter as tk
import random

# 设置牌面与数值（带花色）
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_values = {rank: i + 1 for i, rank in enumerate(ranks)}  # A=1, K=13
deck = [f"{rank}{suit}" for suit in suits for rank in ranks]

# 初始化牌
player_cards = random.sample(deck, 5)
robot_cards = random.sample([card for card in deck if card not in player_cards], 5)

player_score = 0
robot_score = 0
round_num = 1

# 设置主窗口
root = tk.Tk()
root.title("♠️扑克牌对战♠️")
root.geometry("800x600")
root.configure(bg="#1e1e1e")  # 深色背景

# 标题
title = tk.Label(root, text="♠️ 终极扑克牌对战 ♣️", font=("Helvetica", 26, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=20)

# 状态栏
status_var = tk.StringVar()
status_var.set("点击一张你的牌开始对战")
status = tk.Label(root, textvariable=status_var, font=("Helvetica", 14), bg="#1e1e1e", fg="lightgreen")
status.pack()

# 分数栏
score_var = tk.StringVar()
score_var.set("得分 - 你: 0  机器人: 0")
score = tk.Label(root, textvariable=score_var, font=("Helvetica", 16), bg="#1e1e1e", fg="orange")
score.pack(pady=10)

# 玩家牌按钮区域
player_frame = tk.Frame(root, bg="#1e1e1e")
player_frame.pack(pady=30)

card_buttons = {}

def card_value(card_str):
    rank = card_str[:-1]
    return card_values[rank]

def play_round(card):
    global player_score, robot_score, round_num

    if card not in player_cards:
        return

    robot_card = random.choice(robot_cards)
    player_cards.remove(card)
    robot_cards.remove(robot_card)

    p_val = card_value(card)
    r_val = card_value(robot_card)

    if p_val > r_val:
        result = "✅ 你赢了这回合！"
        player_score += 1
    elif p_val < r_val:
        result = "❌ 机器人赢了这回合。"
        robot_score += 1
    else:
        result = "🤝 平局！"

    status_var.set(f"第 {round_num} 回合：你出 {card}，机器人出 {robot_card}\n{result}")
    score_var.set(f"得分 - 你: {player_score}  机器人: {robot_score}")

    # 移除该按钮
    card_buttons[card].destroy()
    del card_buttons[card]

    round_num += 1

    if round_num > 5:
        end_game()

def end_game():
    for btn in card_buttons.values():
        btn.config(state="disabled")

    if player_score > robot_score:
        final = "🏆 恭喜你赢得了整场比赛！"
    elif player_score < robot_score:
        final = "💀 很遗憾，机器人赢了。"
    else:
        final = "🤝 最终平局！"

    status_var.set(status_var.get() + f"\n\n🎉 游戏结束！{final}")

def render_cards():
    for card in player_cards:
        btn = tk.Button(player_frame, text=card, font=("Courier", 18, "bold"),
                        width=4, height=2, bg="#ffffff", fg="#000000",
                        relief="raised", bd=4,
                        command=lambda c=card: play_round(c))
        btn.pack(side="left", padx=10)
        card_buttons[card] = btn

# 渲染初始手牌
render_cards()

# 启动主循环
root.mainloop()