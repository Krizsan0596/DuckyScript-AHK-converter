from time import sleep
import os
import sys

os.chdir(os.path.realpath(__file__).replace("\\", "/").replace(os.path.basename(__file__), ""))

def main():
    clear_console()
    print("This script converts Ducky Script into AutoHotKey code.")
    print("Make sure you include the file extension too.")
    print("Keep in mind that this is case sensitive!")
    filename = input("Please enter the file you would like to modify\n>")
    script: str = ''
    config = '''
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
'''
    if filename == "":
        print("Please enter a filename!")
        sleep(3)
        main()
    elif filename.find(".") == -1:
        print("Please include the file extension!")
        sleep(3)
        main()
    else:
        if os.path.isfile(filename):
            f = open(filename, 'r')
            script = f.read()
            f.close()
            print("File found! Processing...")
        else:
            print("File not found!\nCreate one(Y/n/x to exit)?")
            i = input(">")
            if i == "y" or i == "Y":
                open(filename, "x")
            elif i == "n" or i == "N":
                print("Alright! Restarting...")
                sleep(3)
                main()
            elif i == "x" or i == "X":
                print("Exiting...")
                sleep(3)
                sys.exit()
            else:
                print("Invalid response!")
                sleep(3)
                main()

    script = script.replace("ď»ż", "")
    script = script.replace("DELAY", "Sleep,")
    script = script.replace("STRING", "Send,")
    script = script.replace("ENTER", "Send, {Enter}")
    script = script.replace("REM", ";")
    script = script.replace("GUI ", "Send #")
    script = script.replace("ALT ", "Send !")
    script = script.replace("SHIFT ", "Send +")
    script = script.replace("CONTROL ", "Send ^")
    script = script.replace("CTRL ", "Send ^")
    script = script.replace("CONTROL ", "Send ^")
    script = script.replace("UP ", "Send {Up}")
    script = script.replace("DOWN ", "Send {Down}")
    script = script.replace("LEFT ", "Send {Left}")
    script = script.replace("RIGHT ", "Send {Right}")
    script = script.replace("TAB", "Send {Tab}")

    print("Replacement complete!")

    if script.find(config) == -1:
        script = config + "\n" + script
    print("Generating output...")
    f = open('output.ahk', 'w')
    f.write(script)
    f.close()

    print("Done!\nResults are in output.ahk.")
    s = 3
    for i in range(s):
        print(f"Closing in {s} seconds")
        s -= 1
        sleep(1)
    sys.exit()
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == "__main__":
    main()
