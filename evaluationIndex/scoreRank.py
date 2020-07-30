import json

f = open('../data/test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

# 各题分数排名：scoreRank.json "cases_rank_average"
# 1、遍历所有题目，获得每一题的做的数量和所有分数

fAllScore = open("../data/allScore.json", 'w')
exeId = []
re = dict()
for key, value in data.items():
    for case in value["cases"]:
        caseId = case["case_id"]
        if caseId in exeId:
            continue
        exeId.append(caseId)
        li = []
        for k, v in data.items():
            for c in v["cases"]:
                if caseId == c["case_id"]:
                    li.append(c["final_score"])
                    break
        tmp = dict()
        tmp["case_id"] = caseId
        tmp["case_num"] = len(li)
        tmp["score"] = li
        re[caseId] = tmp
fAllScore.write(json.dumps(re, indent=4))
fAllScore.close()

# 2、对每个学生进行每题的排名,每题算出排名占比（公式为100*（总数-排名）/总数-1），并算出每个人所有题目排名占比的平均值

fAllScore = open('../data/allScore.json')
fAllScoreStr = fAllScore.read()
fAllScoreData = json.loads(fAllScoreStr)
fScoreRank = open("../data/scoreRank.json", 'w')
rankDic = dict()
for key, value in data.items():
    userDict = dict()
    userId = key
    caseList = []
    exeId = []
    caseRankScoreList = []
    for case in value["cases"]:
        caseDic = dict()
        caseId = case["case_id"]
        if caseId in exeId:
            continue
        exeId.append(caseId)
        caseDic["case_id"] = caseId
        finalScore = case["final_score"]
        for k, v in fAllScoreData.items():
            if caseId == k:
                allNum = v["case_num"]
                li = list(v["score"])
                li.sort(reverse=True)
                rank = li.index(finalScore) + 1
                caseRankScore = 0
                if (allNum == 1):
                    caseRankScore = 100
                else:
                    caseRankScore = round(100 * (allNum - rank) / (allNum - 1), 2)
                caseDic["rank"] = rank
                caseDic["case_num"] = allNum
                caseDic["rank_score"] = caseRankScore
                caseRankScoreList.append(caseRankScore)
                break
        caseList.append(caseDic)
    caseRankScoreListAverage = round(sum(caseRankScoreList) / len(caseRankScoreList), 2)
    userDict["user_id"] = userId
    userDict["cases_rank_average"] = caseRankScoreListAverage
    userDict["cases"] = caseList
    rankDic[userId] = userDict
fScoreRank.write(json.dumps(rankDic, indent=4))
fScoreRank.close()
f.close()
