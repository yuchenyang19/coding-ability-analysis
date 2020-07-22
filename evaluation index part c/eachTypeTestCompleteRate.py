import json

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

# 各类型题目完成率：eachTypeCompleteRate.json "test_each_type_complete_score"

# 各类题目数目
testTypeNum = {"字符串": 18, "线性表": 28, "数组": 47, "查找算法": 20, "排序算法": 11, "数字操作": 34, "图结构": 12, "树结构": 29}

# 分配的权重，可自行更改
weight = {"字符串": 0.125, "线性表": 0.125, "数组": 0.125, "查找算法": 0.125, "排序算法": 0.125, "数字操作": 0.125, "图结构": 0.125,
          "树结构": 0.125}

resultDict = dict()
for key, value in data.items():
    testDict = {"字符串": 0, "线性表": 0, "数组": 0, "查找算法": 0, "排序算法": 0, "数字操作": 0, "图结构": 0, "树结构": 0}
    testId = []
    for case in value["cases"]:
        if case["case_id"] in testId:
            continue
        testId.append(case["case_id"])
        if case["final_score"] != 100:
            continue
        caseType = case["case_type"]
        testDict[caseType] = testDict[caseType] + 1
    CompleteRateScore = 0
    for k, v in testDict.items():
        testDict[k] = v / testTypeNum[k]
        CompleteRateScore += (testDict[k] * weight[k] * 100)
        testDict[k] = round(testDict[k], 2)
    if CompleteRateScore > 100:
        CompleteRateScore = 100
    testDict["test_each_type_complete_score"] = round(CompleteRateScore, 2)
    resultDict[key] = testDict

fTestCompleteRate = open("eachTypeCompleteRate.json", 'w')
fTestCompleteRate.write(json.dumps(resultDict, ensure_ascii=False, indent=4))
fTestCompleteRate.close()
f.close()
