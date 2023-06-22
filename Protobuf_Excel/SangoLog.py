import time
from LogColor import PrintGreen, PrintRed, PrintYellow, PrintBlue

# Developer: SangonomiyaSakunovi

# Public
def LogInfo(message):
    logString = getLogString(message)
    print(logString)

def LogProcessing(message):
    logString = getLogString(message)
    PrintBlue(logString)

def LogDone(message):
    logString = getLogString(message)
    PrintGreen(logString)

def LogWarn(message):
    logString = getLogString(message)
    PrintYellow(logString)

def LogError(message):
    logString = getLogString(message)
    PrintRed(logString)

# Private
def getLogString(message):
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    string = currentTime + " >> " + message
    return string

if __name__ == "__main__":
    LogInfo("Info message.")
    LogProcessing("Processing message.")
    LogDone("Done message.")
    LogWarn("Warn message.")
    LogError("Error message.")
