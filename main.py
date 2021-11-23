from pynput import keyboard

word = ""
auto_press = False
hotkeys = []


def paste_hotkey(text):
    global auto_press
    auto_press = True
    key_controller = keyboard.Controller()
    with key_controller.pressed(keyboard.Key.ctrl):
        key_controller.tap(keyboard.Key.left)
    
    with key_controller.pressed(keyboard.Key.ctrl):
        with key_controller.pressed(keyboard.Key.shift):
            key_controller.tap(keyboard.Key.right)
    
    key_controller.tap(keyboard.Key.delete)

    key_controller.type(text)


def on_press(key):
    global word
    global auto_press
    print(key)
    
    if not auto_press:

        if key == keyboard.Key.space:
            word = ""

        elif key == keyboard.Key.backspace:
            word = word[:-1]
        elif hasattr(key, 'char'):
            word += key.char

        if word == "teste":
            paste_hotkey('escreve isso, porém é uma frase maior pra eu ver se demora muito pra ela escrever ou algo assim')
            word = ""
            auto_press = False

with open('template.txt', 'r') as template:
    for line in template.readlines():
        key_value = line.split(":");
        hotkey = {}
        hotkey[key_value[0]] = key_value[1]
        hotkeys.append(hotkey) 

print(hotkeys)
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
