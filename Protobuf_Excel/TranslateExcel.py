import os, json, zlib, google, pandas
from SangoLog import LogInfo, LogDone, LogWarn, LogError

# Developer: SangonomiyaSakunovi

def calc_relative_path(dir, filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), dir, filename)

configFile = open(calc_relative_path("config", "config.json"), encoding='utf-8')
configJson = json.load(configFile)
exec("import " + configJson["proto"] + "_pb2")
exec("proto = " + configJson["proto"] + "_pb2")

def generate_cs():
    for path in configJson["csPath"]:
        if os.path.exists(path) == False:
            os.makedirs(path)
        os.system(".\software\protogen.exe --csharp_out=%s %s.proto" % (path, configJson["proto"]))

def loop_work():
    LogInfo("starting loop work...")
    xlsxConfig = configJson["xlsx"]
    for item in xlsxConfig:      
        convert_data(item)

def convert_data(convertItem):
    LogInfo("Generate Structure: " + convertItem["structure"])


def calc_structure(prePath, firstRow, fields, isCheck):
    LogDone

def set_value(eData, row, desc, tconfig):
    LogDone

def get_value(row, entry):
    LogDone

def write_json_file(tData, path):
    LogDone

def write_bytes_file(tData, path):
    LogDone

def trans_float(value):
    value = str(value)
    if value == '':
        return 0
    else:
        return float(value)

def trans_int(value):
    return int(trans_float(value))

loop_work()
generate_cs()