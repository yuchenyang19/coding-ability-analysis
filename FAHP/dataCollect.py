import json

s11 = open('commitTimesRank.json')
res11 = s11.read()
data11 = json.loads(res11)

s12 = open('scoreRatesRank.json')
res12 = s12.read()
data12 = json.loads(res12)

s21 = open('scoreRank.json')
res21 = s21.read()
data21 = json.loads(res21)

s22 = open('eachTypeCompleteRate.json')
res22 = s22.read()
data22 = json.loads(res22)

s23 = open('allTestsCompleteRate.json')
res23 = s23.read()
data23 = json.loads(res23)

resultDict = dict()
for key, value in data11.items():
    userDict = dict()
    userDict["s11"] = value["commitTimes_rank_score"]
    for k, v in data12.items():
        if k == key:
            userDict["s12"] = v["cases_rates_rank_average"]
            break
    for k, v in data21.items():
        if k == key:
            userDict["s21"] = v["cases_rank_average"]
            break
    for k, v in data22.items():
        if k == key:
            userDict["s22"] = v["test_each_type_complete_score"]
            break
    for k, v in data23.items():
        if k == key:
            userDict["s23"] = v
            break
    resultDict[key] = userDict
fDataCollect = open('dataCollect.json', 'w')
fDataCollect.write(json.dumps(resultDict, indent=4))
fDataCollect.close()
