#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for existential_use

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

DEBUG_existential_use = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_existential_use.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_existential_use:
        print("[existential_use] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["測試句"] = inputSTR
    resultDICT["existential"] = []
    if 'intent' not in resultDICT.keys():
        resultDICT["intent"] = []
    if utterance == "可曾看到有誰去辦誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("可曾看到有誰去辦誰")
                     
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b2")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                    
    
    if utterance == "或者說誰誰誰不好":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("或者說誰誰誰不好")
                       
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b4")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "所以我記得是誰呀":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("所以我記得是誰呀")
                       
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b3")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]

    if utterance == "那個誰呀":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("那個誰呀")
                        
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b1")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "沒有誰注意我存在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("沒有誰注意我存在")
                        
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b5")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "彷彿生著誰的氣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("彷彿生著誰的氣")
                        
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b6")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]
                
    if utterance == "只要我是人家的誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["existential"].append("彷彿生著誰的氣")
                       
            if 'a1' not in resultDICT["intent"] and 'a5' not in resultDICT["intent"] and 'a9' not in resultDICT["intent"] and 'a25' not in resultDICT["intent"]:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False
                resultDICT["intent"].append("b7")
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "a" not in item]        

    return resultDICT