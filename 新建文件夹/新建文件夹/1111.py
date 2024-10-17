import tkinter as tk
import time
import winsound
import os

def countdown(count):
    # 更新标签显示的时间
    label['text'] = count
    if count > 0:
        # 每隔300毫秒（0.3秒）调⽤⼀次countdown函数
        root.after(300, countdown, count-1)
    else:
        # 获取当前脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 拼接wav文件的完整路径
        sound_path = os.path.join(current_dir, "dog_bark.wav")
        # 播放狗叫声音效
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)

def start_timer():
    countdown(10)

# 创建主窗⼝
root = tk.Tk()
root.title("古典时钟计时器")

# 创建标签来显示倒计时
label = tk.Label(root, font=('Helvetica', 48), text="")
label.pack()

# 创建开始按钮
start_button = tk.Button(root, text="开始", command=start_timer)
start_button.pack()

# 运⾏主循环
root.mainloop()
