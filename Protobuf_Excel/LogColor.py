import ctypes, sys

# Developer: SangonomiyaSakunovi

# HandleDefine
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# ColorDefine
FOREGROUND_BLUE = 0x09
FOREGROUND_GREEN = 0x0a
FOREGROUND_RED = 0x0c
FOREGROUND_YELLOW = 0x0e

# GetHandle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# Public
def PrintGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess + '\n')
    resetColor()

def PrintRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess + '\n')
    resetColor()

def PrintYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess + '\n')
    resetColor()

# Private
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

if __name__ == '__main__':
    PrintGreen('printGreen:Gree Color Text')
    PrintRed('printRed:Red Color Text')
    PrintYellow('printYellow:Yellow Color Text')