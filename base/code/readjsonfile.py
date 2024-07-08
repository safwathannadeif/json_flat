'''
Text Type:	        str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:	        set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
None Type:	        NoneType
Enum:               Enum
'''
# Python program to read
# json file
import json


def readjson(inpfile):
    try:
        with open(inpfile, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {inpfile} file encountered an error")
    return data


def readfile(filex):
    # Opening JSON file
    with open(filex) as my_file:
        rout = my_file.read()
    # returns JSON object as  a dictionary
    jdata = json.loads(rout)
    # print("JSON Dict =", jdata)
    # json.dumps(jdata, indent=1)
    return jdata
