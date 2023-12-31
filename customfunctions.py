import os,sys,pickle,json
import tkinter as tk

#custom seconds converter because time.strftime("%H:%M:%S",time.gmtime(timerSec)
#rolls over to 01:00:00 when seconds is greater than 89999.
def S_To_H_M_S(secondsIn: int, paddingEN: bool):
    MS = secondsIn%3600
    H = int(((secondsIn - MS)/3600))
    S = MS%60
    M = int(((MS - S)/60))
    if paddingEN == True:
        if S < 10:
            sPadding = "0"
        else:
            sPadding = ""
        if M < 10:
            mPadding = "0"
        else:
            mPadding = ""
        if H < 10:
            hPadding = "0"
        else:
            hPadding= ""
    else:
        hPadding= ""
        mPadding= ""
        sPadding= ""
    Result  = str(hPadding + str(H) + ":" + mPadding + str(M) + ":" + sPadding +str(S))
    return Result

#code to locate image in pyinstaller executeable: https://stackoverflow.com/questions/31836104
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('')
    return os.path.join(base_path,relative_path)

def writePickle(fileIn: str, dataIn):
    with open(fileIn,"wb") as fp:
        pickle.dump(dataIn,fp)
        fp.close()

def readPickle(fileIn: str, defaultVal, disableCheck: bool):
    if(defaultVal == None):
        defaultVal = 0
    if(os.path.exists(fileIn) or disableCheck):
        with open(fileIn,"rb") as fp:
            unpickler = pickle.Unpickler(fp)
            data = unpickler.load()
            fp.close()
    else:
        writePickle(fileIn,0)
        with open(fileIn,"rb") as fp:
            unpickler = pickle.Unpickler(fp)
            data = unpickler.load()
            fp.close()
    return data

def writeJSON(fileIn:str, dataIn,index:str):
    with open(fileIn, "w+") as fp:
        try:
            buffer = json.load(fp)
        except json.JSONDecodeError:
            buffer = []
            buffer = {index: [dataIn]}
            #buffer[index] = dataIn
        json.dump(obj=buffer, fp= fp, indent=4,separators=(',', ': '))
        fp.close()
        buffer = 0

def readJSON(fileIn,defVal = 0, createIfDosentExist:bool = True, index:str = "seconds"):
    if(os.path.exists(fileIn) or not createIfDosentExist):
        try:
            with open(fileIn,"r+") as fp:
                fullData = json.load(fp)
                data = fullData[index]
                fp.close()
        except json.JSONDecodeError:
            data = [1]
            data[0] = 0
    else:
        writeJSON(fileIn,0,index)
        with open(fileIn,"r") as fp:
            fullData = json.load(fp)
            data = fullData[index]
            fp.close()
    print (type(data))
    print (data)
    return data
    
    

def configureAll(slaves: list, fontSize):
    for item in slaves:
        item.configure(font=("arial", fontSize))
        print(type(item))