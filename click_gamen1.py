#coding:utf-8

# コマンドプロンプトの画面のcmd.exeの部分をクリック。
# 最後に、ctrl-cを発生させる。

import pyautogui
import time

# Check version
# Python 3.6.4, 64bit on Win32 (Windows 10)
# pyautogui 0.9.51
# pyscreeze 0.1.26


# コマンドプロンプトの cmd.exeの部分をクリック
pyautogui.click('cmd.png')  # 存在しないとエラーが発生する。
#
print('test position',pyautogui.position())

# 現在位置から(100,100)だけ移動
pyautogui.move(100,100)
####「Enterキー」を押す
####pyautogui.press('enter')
# 「Ctrl+c」を押す
pyautogui.hotkey('ctrl', 'c')

