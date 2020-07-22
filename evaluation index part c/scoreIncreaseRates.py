import json

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

# 各题分数增长率排名：scoreRatesRank.json "cases_rates_rank_average"

# 1、算出每一题的分数增长率

rateDict = dict()
for key, value in data.items():
    userDict = dict()
    casesList = []
    for case in value["cases"]:
        caseDict = dict()
        finalScore = case["final_score"]
        records = list(case["upload_records"])
        times = 0
        for i in range(len(records)):
            if records[i]["score"] == finalScore:
                times = i
                break
        increaseRate = round(finalScore / (times + 1), 2)
        caseDict["case_id"] = case["case_id"]
        caseDict["rate_of_increase"] = increaseRate
        casesList.append(caseDict)
    userDict["user_id"] = key
    userDict["cases"] = casesList
    rateDict[key] = userDict
eachTestScoreRate = open('eachTestScoreRate.json', 'w')
eachTestScoreRate.write(json.dumps(rateDict, indent=4))
eachTestScoreRate.close()
f.close()

# 2、获得每一题的所有分数增长率

eachTestScoreRate = open('eachTestScoreRate.json')
eachTestScoreRateRead = eachTestScoreRate.read()
eachTestScoreRateData = json.loads(eachTestScoreRateRead)

caseIdHasDone = []
re = dict()
for key, value in eachTestScoreRateData.items():
    for case in value["cases"]:
        caseId = case["case_id"]
        if caseId in caseIdHasDone:
            continue
        caseIdHasDone.append(caseId)
        li = []
        for k, v in eachTestScoreRateData.items():
            for c in v["cases"]:
                if caseId == c["case_id"]:
                    li.append(c["rate_of_increase"])
                    break
        tmp = dict()
        tmp["case_id"] = caseId
        tmp["case_num"] = len(li)
        tmp["all_rate_of_increase"] = li
        re[caseId] = tmp
allScoreRates = open('allScoreRates.json', 'w')
allScoreRates.write(json.dumps(re, indent=4))
allScoreRates.close()
eachTestScoreRate.close()

# 3、对每一题的增长率进行排名，每题算出排名占比（公式为100*（总数-排名）/总数-1），并算出每个人所有题目排名占比的平均值

allScoreRates = open('allScoreRates.json')
allScoreStr = allScoreRates.read()
allScoreData = json.loads(allScoreStr)
eachTestScoreRate = open('eachTestScoreRate.json')
eachTestScoreRateRead = eachTestScoreRate.read()
eachTestScoreRateData = json.loads(eachTestScoreRateRead)
rankDic = dict()
for key, value in eachTestScoreRateData.items():
    userDict = dict()
    userId = key
    caseList = []
    exeId = []
    caseRankScoreRateList = []
    for case in value["cases"]:
        caseDic = dict()
        caseId = case["case_id"]
        if caseId in exeId:
            continue
        exeId.append(caseId)
        caseDic["case_id"] = caseId
        rateOfIncrease = case["rate_of_increase"]
        for k, v in allScoreData.items():
            if caseId == k:
                allNum = v["case_num"]
                li = list(v["all_rate_of_increase"])
                li.sort(reverse=True)
                rank = li.index(rateOfIncrease) + 1
                caseRateRankScore = 0
                if (allNum == 1):
                    caseRateRankScore = 100
                else:
                    caseRateRankScore = round(100 * (allNum - rank) / (allNum - 1), 2)
                caseDic["rank"] = rank
                caseDic["case_num"] = allNum
                caseDic["rate_rank_score"] = caseRateRankScore
                caseRankScoreRateList.append(caseRateRankScore)
                break
        caseList.append(caseDic)
    caseRateRankScoreListAverage = round(sum(caseRankScoreRateList) / len(caseRankScoreRateList), 2)
    userDict["user_id"] = userId
    userDict["cases_rates_rank_average"] = caseRateRankScoreListAverage
    userDict["cases"] = caseList
    rankDic[userId] = userDict
fScoreRatesRank = open("scoreRatesRank.json", 'w')
fScoreRatesRank.write(json.dumps(rankDic, indent=4))
fScoreRatesRank.close()
