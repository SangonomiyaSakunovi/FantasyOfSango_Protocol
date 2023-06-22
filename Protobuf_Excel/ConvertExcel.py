import os, json, zlib, google, xlrd
from SangoLog import LogInfo, LogProcessing, LogDone, LogWarn, LogError

# Developer: SangonomiyaSakunovi

def get_relative_path(dir, filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), dir, filename)

configFile = open(get_relative_path("config", "config.json"), encoding='utf-8')
configJson = json.load(configFile)
exec("import " + configJson["proto"] + "_pb2")
exec("proto = " + configJson["proto"] + "_pb2")

def generate_cs():
    for path in configJson["csPath"]:
        if os.path.exists(path) == False:
            os.makedirs(path)
        os.system(".\software\protogen.exe --csharp_out=%s %s.proto" % (path, configJson["proto"]))
    LogDone("Generate .cs has done.")

def loop_work():
    LogProcessing("starting loop work...")
    xlsxConfig = configJson["xls"]
    for config in xlsxConfig:      
        convert_data(config)
    LogDone("Loop work has done.")

def convert_data(convertConfig):
    LogDone("Generate Structure: " + convertConfig["structure"])
    tempClass = getattr(proto, convertConfig["structure"])        # return the proto value which defined by the key:convertItem["structure"]
    tempData = tempClass()
    streamingData = tempData.Lst
    for xlsFile in convertConfig["files"]:
        LogProcessing("Processing xls file >> " + xlsFile)
        book = xlrd.open_workbook(get_relative_path("input", xlsFile), formatting_info=True)
        sheets = book.sheets()
        for index, table in enumerate(sheets):
            if table.name in configJson["ignore"]:
                continue
            if table.nrows <= configJson["titleRowNum"]:        # nrows == rowNum, ncols == colNum
                continue
            LogInfo("Current convert sheetName >> " + table.name)
            firstRowInfos = table.row(configJson["titleRowNum"])
            firstRowColumnNames = []
            for column in firstRowInfos:
                firstRowColumnNames.append(str(column.value))

            # DESCRIPTOR will get the attribute of Lst in .proto, such as message Skill Lst, you will get info of Skill define
            fieldStructureDict = get_structure_dict("", firstRowColumnNames, tempClass.Lst.DESCRIPTOR.message_type.fields)

            for i in range(configJson["startRowNum"], table.nrows):
                currentRow = table.row(i)
                if str(currentRow[0].value) == "":
                    continue
                newStramingData = streamingData.add()
                try:
                    set_value(newStramingData, currentRow, fieldStructureDict, convertConfig)
                except:
                    LogError("Set value error in FileName:" + xlsFile + " Item:" + convertConfig['structure'] + " TableName: " + table.name + " RowNum:" + str(i))
                    assert(False)
        if "jsonPath" in configJson:
            if "ConvertJson" in convertConfig and convertConfig["ConvertJson"]:
                for path in configJson["jsonPath"]:
                    if os.path.exists(path) == False:
                        os.makedirs(path)
                    write_json_file(tempData, path + convertConfig["structure"] + ".json")
        if "bytesPath" in configJson:
            if "ConvertBytes" in convertConfig and convertConfig["ConvertBytes"]:
                for path in configJson["bytesPath"]:
                    if os.path.exists(path) == False:
                        os.makedirs(path)
                    write_bytes_file(tempData, path + convertConfig["structure"] + ".bytes")

def get_structure_dict(preColumnName, firstRowColumnNames, descriptorFields):
    fieldStructureDict = {}
    exist = False
    for field in descriptorFields:
        if field.label == field.LABEL_REPEATED:         # The label in .proto is repeated
            fieldStructureDict[field.name] = []
            # Custom structure: example1: cooldown0 cooldown1
            # Custom structure: example2: drop0id drop1id drop0num drop1num
            colunmNamePostfixIndex = 0       
            while True:
                currenColunmName = preColumnName + field.name + str(colunmNamePostfixIndex)
                if field.type == field.TYPE_MESSAGE:
                    subFieldStructureDict = get_structure_dict(currenColunmName, firstRowColumnNames, field.message_type.fields)
                    if subFieldStructureDict:
                        fieldStructureDict[field.name].append(subFieldStructureDict)
                    else:
                        break
                else:
                    if currenColunmName not in firstRowColumnNames:
                        break
                    fieldStructureDict[field.name].append({"path": colunmName, "col": firstRowColumnNames.index(colunmName), "type": field.type})
                exist = True
                colunmNamePostfixIndex += 1

        else:
            colunmName = preColumnName + field.name
            if field.type == field.TYPE_MESSAGE:
                subFieldStructureDict = get_structure_dict(colunmName, firstRowColumnNames, field.message_type.fields)
                if subFieldStructureDict:
                    fieldStructureDict[field.name] = subFieldStructureDict
                    exist = True
            else:
                if colunmName in firstRowColumnNames:
                    fieldStructureDict[field.name] = {"path": colunmName, "col": firstRowColumnNames.index(colunmName), "type": field.type}
                    exist = True
    if exist:
        return fieldStructureDict
    else:
        return None

def set_value(streamingData, row, fieldStructureDict, convertConfig):
    isSetValue = False
    for fieldName, subFieldStructureDict in fieldStructureDict.items():
        subData = getattr(streamingData, fieldName)       # return the streamingData value which defined by the key
        if isinstance(subFieldStructureDict, list):     # return if the value is list
            for dict in subFieldStructureDict:
                if "col" in dict:
                    value, hasValue = get_value(row, dict)
                    if hasValue or ("keepArray" in convertConfig and convertConfig["keepArray"]):
                        subData.append(value)
                        isSetValue = True
                    else:
                        continue
                else:
                    newSubData = subData.add()
                    hasValue = set_value(newSubData, row, dict, convertConfig)
                    if hasValue or ("keepArray" in convertConfig and convertConfig["keepArray"]):
                        isSetValue = True
                    else:
                        subData.remove(newSubData)
        else:
            if "col" in subFieldStructureDict:
                value, hasValue = get_value(row, subFieldStructureDict)
                setattr(streamingData, fieldName, value)
                if hasValue:
                    isSetValue = True
            else:
                hasValue = set_value(subData, row, subFieldStructureDict, convertConfig)
                if hasValue:
                    isSetValue = True
    return isSetValue

def get_value(row, fieldStructureDict):
    hasValue = True
    value = row[fieldStructureDict["col"]].value
    if value == "":
        hasValue = False
    colunmeType = fieldStructureDict["type"]
    if colunmeType == google.protobuf.descriptor.FieldDescriptor.TYPE_DOUBLE or colunmeType == google.protobuf.descriptor.FieldDescriptor.TYPE_FLOAT:
        return (convert_float(value), hasValue)
    elif colunmeType == google.protobuf.descriptor.FieldDescriptor.TYPE_STRING:
        if isinstance(value, (int, float)):
            value = str(int(value))
        return (value, hasValue)
    else:
        return (convert_int(value), hasValue)

def convert_float(value):
    value = str(value)
    if value == '':
        return 0
    else:
        return float(value)

def convert_int(value):
    return int(convert_float(value))

def convert_protobuf_struct(tempData):
    tempStruct = {}
    fields = tempData.ListFields()
    for type in tempData.DESCRIPTOR.fields:
        if type.has_default_value:
            tempStruct[type.name] = type.default_value
        if type.label == type.LABEL_REPEATED or type.type == type.TYPE_MESSAGE:
            tempStruct[type.name] = []
    for (type, streamingData) in fields:
        if type.label == type.LABEL_REPEATED:
            tempStruct[type.name] = []
            for data in streamingData:
                if type.type == type.TYPE_MESSAGE:
                    stStruct = convert_protobuf_struct(data)
                    tempStruct[type.name].append(stStruct)
                else:
                    tempStruct[type.name].append(data)
        else:
            if type.type == type.TYPE_MESSAGE:
                stStruct = convert_protobuf_struct(streamingData)
                tempStruct[type.name] = stStruct
            else:
                tempStruct[type.name] = streamingData
    return tempStruct

def write_json_file(tempData, filePath):
    tempStruct = convert_protobuf_struct(tempData)
    encodeJson = json.dumps(tempStruct, sort_keys=True, indent=2, ensure_ascii=False).encode("utf-8")
    file = open(filePath, "wb+")
    file.write(encodeJson)
    file.close

def write_bytes_file(tempData, filePath):
    bytesPackage = tempData.SerializeToString()
    zipBytesPackage = zlib.compress(bytesPackage)
    file = open(filePath, "wb+")
    file.write(zipBytesPackage)
    file.close 

loop_work()
generate_cs()