import keyboard as key
import time

def wait(int):
    time.sleep(int)

def botstart():
    key.press_and_release('win')
    wait(1)
    key.write('whatsapp')
    wait(1)
    key.press_and_release('enter')
    wait(10)
    key.press_and_release('down')
    wait(1)
    key.press_and_release('enter')
    wait(1)
    amt = 30
    while amt > 0:
        key.write('Test Text')
        key.press_and_release('enter')
        wait(0.5)
        amt -= 1
    

botstart()