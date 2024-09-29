#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for universal_use

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_universal_use = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_universal_use.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_universal_use:
        print("[universal_use] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["測試句"] = inputSTR
    resultDICT["universal"] = []
    if 'intent' not in resultDICT.keys():
        resultDICT["intent"] = []    
    if utterance == "無論誰當權":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("無論誰當權")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c3")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "誰也不敢動":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰也不敢動")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c1")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "誰也說不上來":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰也說不上來")
                 
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c7")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "誰做好公民誰就是傻瓜":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰做好公民誰就是傻瓜")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c4")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "誰再出聲便處分誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰再出聲便處分誰")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c6")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "誰打破了這個平衡誰就輸":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰打破了這個平衡誰就輸")
                        
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["existential wh checker"] = False
                resultDICT["intent"].append("c5")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "選誰來做都一樣可行":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("選誰來做都一樣可行")
            
            if 'a1' not in resultDICT["intent"] or 'a5' not in resultDICT["intent"] or 'a9' not in resultDICT["intent"] or 'a25' not in resultDICT["intent"]or 'a26' not in resultDICT["intent"]:
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c2")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "誰也聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰也聽不懂")
                       
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c8")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "隨機性即誰想做什麼就吃什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("隨機性即誰想做什麼就吃什麼")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c9")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "老實說誰都綑不住我":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("老實說誰都綑不住我")
                 
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c10")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "只要誰說有效我就帶他去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("只要誰說有效我就帶他去")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c11")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                    
                
    if utterance == "誰也難討好":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("誰也難討好")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c12")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
    
    if utterance == "再也沒有誰能聽得到了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("再也沒有誰能聽得到了")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c13")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]        
                
    if utterance == "換了我們誰也會這樣做的":   
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("換了我們誰也會這樣做的")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c14")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]        
    
    if utterance == "任誰也知道這時候女孩還能發信":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("任誰也知道這時候女孩還能發信")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c15")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "半夜誰起來就順便看一下":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["universal"].append("半夜誰起來就順便看一下")
            
            if all(x not in resultDICT["intent"] for x in ['a1', 'a5', 'a9', 'a25', 'a26']):
                resultDICT["universal wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("c16")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]        
        


    return resultDICT