from pynput import keyboard

word = ""

def on_press(key):
    global word
    print(key)
    if key == keyboard.Key.space:
        word = ""

    elif key == keyboard.Key.backspace:
        word = word[:-1]
    elif hasattr(key, 'char'):
        word += key.char
        print('a',word)

    if word == "teste":
        print('rolou')   

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
