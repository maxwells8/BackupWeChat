from ahk import AHK
from ahk import keys
from PIL import ImageGrab
import win32api
import win32con

# 微信好友和群的总数
friends_total = 500

find_wechat = False
autohotkey_path = 'AutoHotkey\\AutoHotkeyU64.exe'
ahk = AHK(executable_path=autohotkey_path)


def select_wechat():
    global find_wechat
    wins = list(ahk.windows())
    wechat_class_name = bytes('WeChatMainWndForPC', encoding='gbk')
    for win in iter(wins):
        if win.class_name == wechat_class_name:
            win.activate()
            win.maximize()
            find_wechat = True
            # 定位到好友菜单
            win.click(50, 216)
            # 定位到好友列表
            win.click(230, 200)
            # 滚动到最顶
            ahk.key_press('Home')
            break

    if not find_wechat:
        win32api.MessageBox(0, "没有找到微信客户端，请打开并登录！", "没有找到微信客户端", win32con.MB_ICONWARNING)
        exit()


def savefile(name: str):
    snapshot = ImageGrab.grab()
    save_path = "Backup\\" + name + ".png"
    snapshot.save(save_path)


def save_friend_to_file():
    for i in range(friends_total):
        savefile(str(i))
        ahk.key_press(keys.KEYS.DOWN)


if __name__ == "__main__":
    select_wechat()
    save_friend_to_file()
    exit()
