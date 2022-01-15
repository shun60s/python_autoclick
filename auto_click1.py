#coding:utf-8


#
# (10, 10)の位置にマウスカーソルを移動して、
# 60秒毎にマウスのクリック相当を発生させる。
#

import pyautogui
import time

# Check version
# Python 3.6.4, 64bit on Win32 (Windows 10)
# pyautogui 0.9.51
# pyscreeze 0.1.26


# (10, 10)の位置にマウスカーソルを移動
ix=10
iy=10
pyautogui.moveTo(ix,iy)

# 最初のクリック
pyautogui.click()

#　クリック位置を表示
print('test position',pyautogui.position())


# 60秒毎にクリック。　120回で 4時間継続する。
# 途中終了するときは、コマンドプロンプトの画面でenterを連打したあとctrl-cを押してｙで終了。
for i in range(120):
    time.sleep(60)
    pyautogui.moveTo(ix,iy)
    pyautogui.click()
    print (i)