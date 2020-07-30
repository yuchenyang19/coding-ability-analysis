import json
import urllib.request, urllib.parse
import os

f = open('../data/sample.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
print(data)

for key,value in data.items():
    cases = data[key]['cases']
    print(cases)
    for case in cases:
        upload_records=case['upload_records']
        scores=[]
        maxScore = 0
        maxScoreIndex=0
        index=0
        for upload_record in upload_records:
            if upload_record['score']>maxScore:
                maxScore=upload_record['score']
                maxScoreIndex=index
                if maxScore == 100:
                    break
            index+=1
        code_url=upload_records[maxScoreIndex]['code_url']
        filename='user'+key+'_case'+case['case_id']+'_'+str(upload_records[maxScoreIndex]['upload_id'])+'.zip'
        print(filename)
        urllib.request.urlretrieve(code_url, '../data/student/'+key+'/'+case['case_id']+'/'+filename)
