import pyautogui
import time
import sys


try:
    file = sys.argv[1]
except IndexError:
    print("enter file:")
    file = input(">> ")

#write file
wfile = open(f"{file}.py", "w+")
wfile.truncate()
def writefile(line):
    wfile.write(line + "\n")

#init


writefile("""
import pyautogui
import time
import sys
""")

def execute_line(line, linecount):
    #init
    main_error_msg = f"line: {linecount} - Failed to compile (run file for testing before compiling)"

    args = list(line.split(":"))
    args[0] = args[0].replace(" ", "")
    ##print(args)


    #print
    if args[0] == "print":
        try:
            args[1] = "\\n" + args[1].strip()
            writefile(f'print("{args[1]}", end="\\n")')
        except:
            return main_error_msg
        return

    #spam
    if args[0] == "spam":
        try:
            msg = args[1].strip()
            msg = msg.replace("\\n", " ")
            n = args[2].strip('\n')
            writefile(f'''
timesdone = 0
while timesdone < {n}:
    pyautogui.typewrite("{msg}" + '\\n')
    print("(spamming {msg}: "+ str(timesdone) +"/{n})", end="\\r")
    timesdone += 1
print("(spamming {msg}: "+ str({n}) +"/{n})", end="\\r")
            ''')
        except:
            return main_error_msg
        return

    #test
    if args[0] == "test":
        try:
            writefile('print("--TEST--"+ "\\n")')
        except:
            return main_error_msg
        return
    
    #sleep
    if args[0] == "sleep":
        try:
            args[1] = int(args[1]) / 1000
            writefile(f'print("(sleeping for {args[1]} second(s))")')
            writefile(f'time.sleep({int(args[1])})')
        except:
            return main_error_msg
        return

    #exit
    if line.startswith("exit"):
        writefile("exit()")
        return

    #comment
    if line.startswith("#"):
        writefile(line)
        return


    #notfound
    line = line.replace(" ", "")
    if line == "\n":
        pass
    else:
        return "Function not found, (line: " + str(linecount) + ")"