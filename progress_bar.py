import time
import sys

def progress_bar(seconds, callback_function, total=20, bar_style="◼︎"):
    """
    通用进度条函数

    参数:
    - seconds: 每进一格的时间（秒）
    - callback_function: 进度条完成后调用的回调函数
    - total: 进度条总长度,默认20
    - bar_style: 进度条样式，用于自定义进度条形状，例如"◼︎"

    返回:
    - None
    """
    for i in range(1, total + 1):
        percent = int((i / total) * 100)
        bar = bar_style * i + ' ' * (total - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(seconds)
    print()  # 换行
    callback_function()  # 执行回调

# 示例 callback function 1
def done_message():
    print("✅ 进度完成！任务已成功执行。")

# 示例 callback function 2
def next_task():
    print("🔁 正在启动下一个任务...")

# 示例调用1
print("开始第一个进度条：")
progress_bar(seconds=0.2, callback_function=done_message)