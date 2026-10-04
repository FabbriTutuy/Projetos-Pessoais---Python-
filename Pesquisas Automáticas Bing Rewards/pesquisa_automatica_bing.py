import pyautogui
from time import sleep
from pesquisas_temas import *
import random

# Sistema de pesquisa automática do bing rewards
# ***Esse código funcionará apenas na máquina que ele foi programada***

pyautogui.PAUSE = 0.5

# 1 - Entrando no Edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
sleep(1.5)
# 1.1 - Acessando o perfil correto
pyautogui.click(x=1548, y=60)
pyautogui.click(x=1344, y=398)
sleep(0.5)

# 2 - Pesquisando
pyautogui.click(x=594, y=55)

for pesquisa in range (0,5):

    # 2.1 - Primeira pesquisa
    pyautogui.write(random.choice(pesquisas), interval=0.08)
    pyautogui.press("enter")
    sleep(3.5)

    # 2.2 - Abrindo uma nova guia e fechando a última guia
    pyautogui.hotkey("ctrl","t")
    pyautogui.click(x=261, y=19)
    pyautogui.click(x=452, y=58)
