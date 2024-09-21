#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from copy import deepcopy
from requests import post
from requests import codes
from pprint import pprint
import json
import math
import os
import re
try:
    from intent import Loki_existential_use
    from intent import Loki_interrogative_use
    from intent import Loki_universal_use
except:
    from .intent import Loki_existential_use
    from .intent import Loki_interrogative_use
    from .intent import Loki_universal_use


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(__file__), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key"]
except Exception as e:
    print("[ERROR] AccountInfo => {}".format(str(e)))
    USERNAME = ""
    LOKI_KEY = ""

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    if "word_count_balance" in result:
                        self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[], refDICT={}):
    resultDICT = deepcopy(refDICT)
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {
                "測試句": "",
                "interrogative wh checker": False,
                "existential wh checker": False,
                "universal wh checker": False,
            }
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # existential_use
                if lokiRst.getIntent(index, resultIndex) == "existential_use":
                    lokiResultDICT = Loki_existential_use.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # interrogative_use
                if lokiRst.getIntent(index, resultIndex) == "interrogative_use":
                    lokiResultDICT = Loki_interrogative_use.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # universal_use
                if lokiRst.getIntent(index, resultIndex) == "universal_use":
                    lokiResultDICT = Loki_universal_use.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

            # save lokiResultDICT to resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                if type(resultDICT[k]) != list:
                    resultDICT[k] = [resultDICT[k]] if resultDICT[k] else []
                if type(lokiResultDICT[k]) == list:
                    resultDICT[k].extend(lokiResultDICT[k])
                else:
                    resultDICT[k].append(lokiResultDICT[k])
    else:
        resultDICT["msg"] = lokiRst.getMessage()
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[], refDICT={}):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content
        refDICT       DICT           參考內容

    output
        resultDICT    DICT           合併 runLoki() 的結果

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    resultDICT = deepcopy(refDICT)
    if resultDICT is None:
        resultDICT = {}

    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST=filterLIST, refDICT=resultDICT)
            if "msg" in resultDICT:
                break

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # existential_use
    print("[TEST] existential_use")
    inputLIST = ['那個誰呀','或者說誰誰誰不好','所以我記得是誰呀','可曾看到有誰去辦誰']
    testLoki(inputLIST, ['existential_use'])
    print("")

    # interrogative_use
    print("[TEST] interrogative_use")
    inputLIST = ['你寫給誰呢','幸運者是誰','誰是高人呢','看誰能給得更多','還有誰會來買本國的產品','那這樣你怎麼知道誰在愛你','未來又由誰來決定接班的人呢','票投給誰只有天知、地知、我知']
    testLoki(inputLIST, ['interrogative_use'])
    print("")

    # universal_use
    print("[TEST] universal_use")
    inputLIST = ['無論誰當權','誰也不敢動','誰也說不上來','誰再出聲便處分誰','選誰來做都一樣可行','誰做好公民誰就是傻瓜','誰打破了這個平衡誰就輸']
    testLoki(inputLIST, ['universal_use'])
    print("")


if __name__ == "__main__":
        
    inputLIST = ["連誰會來都不知道"]
    
    for i, inputSTR in enumerate(inputLIST, start=1):  
        resultDICT = execLoki([inputSTR])
        print(f"測試句：{resultDICT['測試句']}")
        #print(f"{resultDICT['intent']}\n")
        print(f"interrogative wh checker：{resultDICT['interrogative wh checker']}")
        print(f"existential wh checker：{resultDICT['existential wh checker']}")
        print(f"universal wh checker：{resultDICT['universal wh checker']}")            
        print("=======================================================================================================================================")    
    
'''
    with open("../../log/log_P.txt", "w", encoding='utf-8') as log:
    
        for i, inputSTR in enumerate(inputLIST, start=1):  
            resultDICT = execLoki([inputSTR])
            print(f"測試句：{resultDICT['測試句']}")
            #print(f"{resultDICT['intent']}\n")
            print(f"interrogative wh checker：{resultDICT['interrogative wh checker']}")
            print(f"existential wh checker：{resultDICT['existential wh checker']}")
            print(f"universal wh checker：{resultDICT['universal wh checker']}")            
            print("=======================================================================================================================================")        
    
            log.write(f"[{i}]\n")  
            log.write(f"測試句：{resultDICT['測試句']}\n")
            log.write(f"interrogative wh checker：{resultDICT['interrogative wh checker']}\n")
            log.write(f"existential wh checker：{resultDICT['existential wh checker']}\n")
            log.write(f"universal wh checker：{resultDICT['universal wh checker']}\n")
            
        

    
    
    begin = 0
    end = 2697
    with open("../../Corpus/purged/shei_sinica_purged.txt", "r", encoding="utf-8") as f:
        testLIST = f.readlines()
        
    with open("../../log/log_0423.txt", "w", encoding='utf-8') as log:
        for i, inputSTR in enumerate(testLIST[begin:end], start=begin+1):
            resultDICT = execLoki(inputSTR)
            if 'intent' in resultDICT.keys():
                log.write(f"{i}. {resultDICT['intent']}\n")
            else:
                log.write(f"{i}. Missed\n")

            print(f"{i}. {resultDICT}")
            print("\n")
            print(f"測試句：{resultDICT['測試句']}")
            print(f"interrogative wh checker：{resultDICT['interrogative wh checker']}")
            print(f"existential wh checker：{resultDICT['existential wh checker']}")
            print(f"universal wh checker：{resultDICT['universal wh checker']}")            
            print("=======================================================================================================================================")
'''