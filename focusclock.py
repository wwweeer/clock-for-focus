import time
import winsound

def focus_timer(duration):
    print("专注模式开始！")
    time.sleep(duration * 60)  # 将分钟转换为秒
    frequency = 2500  # 发出的声音频率
    duration = 2000  # 发出声音的持续时间（以毫秒为单位）
    winsound.Beep(frequency, duration)
    print("专注时间到！")

if __name__ == "__main__":
    minutes = int(input("请输入专注时间（分钟）："))
    focus_timer(minutes)
