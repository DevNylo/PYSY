from turtle import left
import pyautogui
import time

pyautogui.moveTo(470, 95) # X
pyautogui.click(button='left') # CLOSE CAD
time.sleep(8)
pyautogui.moveTo(105, 601) # MOVE TO "PROFISSIONAL RESPONSÁVEL"
time.sleep(1)
pyautogui.click(button='left')
time.sleep(2)
pyautogui.press('esc') # CLOSE LOCATION
time.sleep(1)
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
pyautogui.write('11576593') # PHYSIOTHERAPIST MONICA
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
time.sleep(1)
pyautogui.moveTo(722, 776) # MOVE TO SAVE
pyautogui.click(button='left') # SAVE
time.sleep(7)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(2)
pyautogui.moveTo(1521, 782) # MOVE TO SAVE
pyautogui.click(button='left') # SAVE
time.sleep(3)
pyautogui.moveTo(692, 258) # RELATORIO
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(712, 319)
time.sleep(1)
pyautogui.click(button='left') #IMPRIMIR
pyautogui.moveTo(920, 548) # MOVE TO ERROR
time.sleep(3)
pyautogui.click(button='left') # REMOVE ERROR
pyautogui.moveTo(1213, 238) # MOVE TO PRESCRIÇÃO
pyautogui.click(button='left') # PRESCRIÇÃO
time.sleep(6)
pyautogui.moveTo(736, 313) # MOVE TO LIBERAR
pyautogui.click(button='left') # LIBERAR
pyautogui.moveTo(929, 541)
time.sleep(2)
pyautogui.click(button='left') # END










