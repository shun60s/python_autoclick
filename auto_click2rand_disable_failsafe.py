#coding:utf-8


#
# (ix, iy)の位置にマウスカーソルを移動して、
# 30秒から120秒の間ランダムににクリックする
#

import pyautogui
import time
import random

# Python 3.6.4 on windows 10
# pyautogui 0.9.51
# pyscreeze 0.1.26

# if 1, disable pyautogui fail-safe
if 1:
    print('pyautogui fail safe is off')
    pyautogui.FAILSAFE=False

# (ix, iy)の位置にマウスカーソルを移動
ix=5
iy=5
pyautogui.moveTo(ix,iy)

# クリック
pyautogui.click()

#
print('test position',pyautogui.position())


# 30秒から120秒の間にランダムにクリック
# 途中終了するときは、コマンドプロンプトの画面でenterを連打したあとctrl-cを押してｙで終了
t_all=0
for i in range(9999):
    #
    #time.sleep(60)
    t0=random.randint(30,120)
    time.sleep(t0)
    t_all += t0
    pyautogui.moveTo(ix,iy)
    pyautogui.click()
    print ( int(t_all / 60), ':', t_all%60)  # 経過時間を表示
