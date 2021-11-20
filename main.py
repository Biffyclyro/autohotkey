from pynput import keyboard
import clipboard

word = ""


def paste_hotkey(text):
    key_controller = keyboard.Controller()
    print('chegou aqui')
    #key_controller.type(text)

def on_press(key):
    global word
    print(key)
    if key == keyboard.Key.space:
        word = ""

    elif key == keyboard.Key.backspace:
        word = word[:-1]
    elif hasattr(key, 'char'):
        word += key.char
        #print('a',word)

    if word == "teste":
        paste_hotkey('escreve isso')
        #clipboard.copy('era pra funcionar assim')
        #with key_controller.press(keyboard.Key.ctrl.value):
        #    key_controller.press('v')
        #    key_controller.release('v')


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
