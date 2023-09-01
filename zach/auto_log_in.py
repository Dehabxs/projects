
import pyautogui
import time
import pygetwindow as gw

pyautogui.click(30, 350)
pyautogui.click(30, 350)
time.sleep(1)
pyautogui.click(730, 650)
# Get the window by its title
window = gw.getWindowsWithTitle("google")[0]

# Get the position of the window
position = window.left, window.top
window.maximize()
# Print the window position
print("Window Position:", position)
time.sleep(1)
pyautogui.click(1700, 150              )
time.sleep(1.5)
pyautogui.click(1000, 690)
time.sleep(1)
pyautogui.write('zvann568', interval=0.25)
pyautogui.press('enter')
pyautogui.write('zac83874', interval=0.25)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.click(150, 200)
time.sleep(1)
pyautogui.click(150, 300)