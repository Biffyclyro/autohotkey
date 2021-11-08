from pynput import keyboard

word = ""

def on_press(key):
    global word
    print(key)
    if key == keyboard.Key.space:
        word = ""

    elif key == keyboard.backspace:
        word.pop()
    elif key != 'Key.backspace':
        word += key.char
        print('a',word)

    if word == "teste":
        print('rolou')   

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()