from pynput import keyboard
#import clipboard

word = ""
auto_press = False


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
        #print('a',word)

        if word == "teste":
            paste_hotkey('escreve isso')
            word = ""
            auto_press = False
        #clipboard.copy('era pra funcionar assim')
        #with key_controller.press(keyboard.Key.ctrl.value):
        #    key_controller.press('v')
        #    key_controller.release('v')


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
