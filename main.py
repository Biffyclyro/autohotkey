from pynput import keyboard

word = ""
auto_press = False
hotkeys = {}

def paste_hotkey(text):
    global auto_press
    auto_press = True
    key_controller = keyboard.Controller()
    
    with key_controller.pressed(keyboard.Key.ctrl):
        with key_controller.pressed(keyboard.Key.shift):
            key_controller.tap(keyboard.Key.left)
    
    key_controller.tap(keyboard.Key.delete)

    key_controller.type(text)


def on_press(key):
    global word
    global auto_press
    #print(word)
    
    if not auto_press:

        if key == keyboard.Key.space:
            word = ""

        elif hasattr(key, 'char'):
            word += key.char

        if word in hotkeys.keys():
            paste_hotkey(hotkeys[word])
            word = ""
            auto_press = False

with open('template.txt', 'r', encoding='utf-8') as template:
    for line in template.readlines():
        key_value = line.split("::");
        hotkeys[key_value[0]] = key_value[1][:-1]


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
