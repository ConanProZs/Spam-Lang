import pyautogui
import time

def execute_line(line, linecount):

    args = list(line.split(":"))
    args[0] = args[0].replace(" ", "")
    ##print(args)

    #print
    if args[0] == "print":
        print(args[1]+ "\n")
        return

    #spam
    if args[0] == "spam":
        try:
            msg = args[1]
            n = args[2]

            for i in range(0,int(n)):
                pyautogui.typewrite(msg + '\n')
                print(f"(spamming {args[1]}: {i}/{n})", end="\r")
                time.sleep(0.01)
            print(f"(spamming {args[1]}: {n}/{n})", end="\r")
            print("\n")
        except IndexError:
            return "No count, (line: " + str(linecount) + ")"
        return

    #test
    if args[0] == "test":
        print("--TEST--"+ "\n")
        return
    
    #sleep
    if args[0] == "sleep":
        try:
            args[1] = int(args[1]) / 1000
            print(f"(sleeping for {args[1]} second(s))")
            time.sleep(int(args[1]))
        except:
            return "Value invalid, (line: " + str(linecount) + ")"
        return

    #exit
    if line.startswith("exit"):
        return 0

    #comment
    if line.startswith("#"):
        return


    #notfound
    line = line.replace(" ", "")
    if line == "\n":
        pass
    else:
        return "Function not found, (line: " + str(linecount) + ")"