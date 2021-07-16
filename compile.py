import sys

if len(sys.argv) < 3:
    string = ""
    for x in ['\n', '-- brainfuck in python --\n', '\n', '-- originally created by Urban Müller in 1993 --\n', '\n', 'more info: https://esolangs.org/wiki/Brainfuck\n', '\n', 'How to run:\n', 'python3 compile.py [ filename ] [ output ] { template/engine file }\n', '\n', 'commands\n', '[ > ] moves the pointer to the right (+1)\n', '[ < ] moves the pointer to the left (-1)\n', '[ + ] changes the selected cell by 1\n', '[ - ] changes the selected cell by -1\n', '[ . ] outputs the ASCII value represented by the current cell\n', '[ , ] inputs one character and gets converted to a number\n', '\n', 'loops\n', '[] loops the code inside it if the pointer is 0\n', '][ loops the code inside it if the pointer is not 0\n', '\n', 'engine files\n', '\n', 'Two engine files are:\n', 'og.txt\n', 'temp.txt\n', '\n', 'temp.txt is the default. It has infinite cells.\n', 'og.txt can be turned on from the command line. It has 50 looping cells.\n']:
        string += x
    print(string)
    exit()

def removeNS(input_):
    output_ = []
    number = 0
    num = 0
    
    for x in input_:
        num += 1
        
        if num != len(input_):
            number = 0
            string = ""
            while number != len(x) - 1:
                number += 1
                string = string + x[number - 1]
            output_.append(string)
        else:
           output_.append(x) 
    return(output_)

args = list(sys.argv)
print("Compiling...")

open(args[2],"x")
file = open(args[2],"a")

def add(string):
    file.write(string + "\n")

def addlist(table):
    for x in table:
        add(x)

indent = 0
sti = ""

def update_ind():
    global indent
    global sti
    string = ""
    for x in range(indent):
        string += "  "
    sti = string

def top(array):
    if len(array) == 0:
        return None
    else:
        return array[len(array) - 1]
try:
    temp = args[3]
except IndexError:
    temp = "temp.txt"
addlist(removeNS(open(temp,"r").readlines()))
stack = []

for string in removeNS(open(args[1].readlines())):
    for x in string:
        if x == ">":
            add(sti + "right()")
        if x == "<":
            add(sti + "left()")
        if x == "+":
            add(sti + "up()")
        if x == "-":
            add(sti + "down()")
        if x == ".":
            add(sti + "printb()")
        if x == ",":
            add(sti + "inputb()")
        if x == "[":
            if top(stack) == "]":
                indent -= 1
                stack.pop()
            else:
                add(sti + "while table[pointer] != 0:")
                indent += 1
                stack.append("[")
            update_ind()
        if x == "]":
            if top(stack) == "[":
                indent -= 1
                stack.pop()
            else:
                add(sti + "while table[pointer] == 0:")
                indent += 1
                stack.append("]")
            update_ind()