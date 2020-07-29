import json

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

# 各题目提交次数：commitTimesRank.json "commitTimes_rank_score"
resultDict = dict()
timesResultDict=dict() # 返回的restult，内含所有同学每道题的提交次数
timesTestDict={} # 一个同学200道题每道题的提交次数
testNum=0

for key, value in data.items():# 遍历所有同学的数据
    userDict = dict()
    casesList = []
    allTestsCommitTimes=0
    allValidTests=len(list(value["cases"]))
    for case in value["cases"]:
        if len(list(case["upload_records"]))==0:
            allValidTests-=1
        caseDict = dict()
        finalScore = case["final_score"]
        records = list(case["upload_records"])
        times = len(records)
        allTestsCommitTimes+=times
        caseDict["case_id"] = case["case_id"]
        caseDict["commit_times"] = times
        casesList.append(caseDict)
    userDict["user_id"] = key
    userDict["allTestsCommitTimes"] = allTestsCommitTimes
    userDict["allValidTests"]=allValidTests
    if allValidTests==0:
        userDict["testsCommitTimesAVG"]=0
    else:
        userDict["testsCommitTimesAVG"]=allTestsCommitTimes//allValidTests
    userDict["cases"] = casesList
    timesResultDict[key]=userDict


fTestCompleteRate = open("commitTimes.json", 'w')
fTestCompleteRate.write(json.dumps(timesResultDict, ensure_ascii=False, indent=4))
fTestCompleteRate.close()
f.close()

# 获得所有人平均每题的提交次数
fTestCompleteRate = open("commitTimes.json")
fTestCompleteRateRead=fTestCompleteRate.read()
fTestCompleteRateData=json.loads(fTestCompleteRateRead)

result=dict()
timesRecords=[]
reD={}
for key,value in fTestCompleteRateData.items():
    timesRecords.append(value["testsCommitTimesAVG"])
reD["allCommitTimes"]=timesRecords
result["commitTimes"]=reD

allCommitTimes=open("allCommitTimes.json",'w')
allCommitTimes.write(json.dumps(result,ensure_ascii=False,indent=4))
allCommitTimes.close()
fTestCompleteRate.close()

# 对每一题的提交次数进行排名，每题算出排名占比（公式为100*（总数-排名）/总数-1），并算出每个人所有题目排名占比的平均值

allCommitTimes=open("allCommitTimes.json")
allCommitTimesRead=allCommitTimes.read()
allCommitTimesData=json.loads(allCommitTimesRead)
fTestCompleteRate=open("commitTimes.json")
fTestCompleteRateRead=fTestCompleteRate.read()
fTestCompleteRateData=json.loads(fTestCompleteRateRead)

reDict={}
commitTimes_rank_score=0

for key,value in fTestCompleteRateData.items():
    userD={}
    useid=key
    rank=0
    commitlist=[]
    AVGcommitTimes=value["testsCommitTimesAVG"]
    # commitTimes_rank_score=100
    if AVGcommitTimes==0:
        commitTimes_rank_score=0
    else:
        rank=0
        allValidRank=0
        for k, v in allCommitTimesData.items():
            commitlist = list(v["allCommitTimes"])
            while 0 in commitlist:
                commitlist.remove(0)
            commitlist.sort()
            allValidRank = len(commitlist)
            rank = commitlist.index(AVGcommitTimes)+1
        commitTimes_rank_score=round(100*(allValidRank-rank)/(allValidRank-1),2)
    userD["user_id"]=useid
    #userD["commitlist"]=commitlist
    userD["rank"]=rank
    userD["commitTimes_rank_score"]=commitTimes_rank_score
    reDict[key]=userD
scoreRank=open("commitTimesRank.json",'w')
scoreRank.write(json.dumps(reDict,indent=4))
scoreRank.close()


