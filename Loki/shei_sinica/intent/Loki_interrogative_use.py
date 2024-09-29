#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for interrogative_use

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

DEBUG_interrogative_use = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_interrogative_use.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_interrogative_use:
        print("[interrogative_use] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["測試句"] = inputSTR
    resultDICT["interrogative"] = [] 
    if 'intent' not in resultDICT.keys():
        resultDICT["intent"] = []
    if utterance == "誰先誰後": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰先誰後")
            resultDICT["intent"].append("a18")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]    
    
    if utterance == "不論誰是誰非":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("不論誰是誰非")
            resultDICT["intent"].append("a16")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            # filter 第二個誰後面是否為動詞
            
    if utterance == "或是沒有能力去判斷候選人的政策究竟誰好誰壞":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("或是沒有能力去判斷候選人的政策究竟誰好誰壞")
            resultDICT["intent"].append("a23")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰跟誰求婚": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰跟誰求婚")
            resultDICT["intent"].append("a9")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]    
        
    if utterance == "你寫給誰呢": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("你寫給誰呢")
            resultDICT["intent"].append("a1")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            

    if utterance == "幸運者是誰": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["interrogative"].append("幸運者是誰")
            resultDICT["intent"].append("a4")

    if utterance == "未來又由誰來決定接班的人呢": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("未來又由誰來決定接班的人呢")
            if 'c3' not in resultDICT["intent"] and 'b4' not in resultDICT['intent']and 'b5' not in resultDICT['intent']and 'b6' not in resultDICT['intent']:
                resultDICT["interrogative wh checker"] = True
                resultDICT["intent"].append("a3")

    if utterance == "看誰能給得更多": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["interrogative"].append("看誰能給得更多")
            resultDICT["intent"].append("a8")

    if utterance == "票投給誰只有天知、地知、我知": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["interrogative"].append("票投給誰只有天知、地知、我知")
            resultDICT["intent"].append("a6")

    if utterance == "誰是高人呢": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["interrogative"].append("誰是高人呢")
            resultDICT["intent"].append("a2")

    if utterance == "還有誰會來買本國的產品": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("還有誰會來買本國的產品")
            resultDICT["intent"].append("a5")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]

    if utterance == "那這樣你怎麼知道誰在愛你": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["interrogative"].append("那這樣你怎麼知道誰在愛你")
            resultDICT["intent"].append("a7")
            
    if utterance == "要不然誰把你Ｆｉｒｅ": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("要不然誰把你Ｆｉｒｅ")
            resultDICT["intent"].append("a10")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰狠心": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰狠心")
            resultDICT["intent"].append("a11")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "究竟是其中誰的貢獻了": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:    
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("究竟是其中誰的貢獻了")
            if 'b6' not in resultDICT['intent']:                
                resultDICT["intent"].append("a12")
            if 'b6' in resultDICT['intent']:
                resultDICT["existential wh checker"] = True
                resultDICT["interrogative wh checker"] = False                
                resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
                
    if utterance == "誰不要臉": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰不要臉")
            resultDICT["intent"].append("a13")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "我們誰又不是邁向歸途": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("我們誰又不是邁向歸途")
            resultDICT["intent"].append("a14")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰在醫學院屋頂": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰在醫學院屋頂")
            resultDICT["intent"].append("a15")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰爸爸有錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰爸爸有錢")
            resultDICT["intent"].append("a17")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰比較恐怖":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("誰比較恐怖")
            resultDICT["intent"].append("a19")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "你怪誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("你怪誰")
            resultDICT["intent"].append("a20")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "現在誰還有農業時代那麼好的耐心和浪漫情懷":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("現在誰還有農業時代那麼好的耐心和浪漫情懷")
            resultDICT["intent"].append("a21")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "談判雙方誰在上風":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("談判雙方誰在上風")
            resultDICT["intent"].append("a22")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "不論發生在何時、何地、針對何人、由誰所為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("不論發生在何時、何地、針對何人、由誰所為")
            resultDICT["intent"].append("a24")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "所以它到底是誰在說什麼故事給誰聽":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("所以它到底是誰在說什麼故事給誰聽")
            resultDICT["intent"].append("a25")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "我想知道誰都考第一名":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative wh checker"] = True
            resultDICT["universal wh checker"] = False
            resultDICT["interrogative"].append("我想知道誰都考第一名")
            resultDICT["intent"].append("a26")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]        
            
    return resultDICT