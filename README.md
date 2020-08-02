# Coding Ability Analysis
2020年数据科学基础大作业 Python编程能力分析

## Table of Contents
[toc]

## Background
- 数据来源：```/data/test_data.json```
- 数据下载：运行```/util/download.py```，可能需要进行2次解压操作
- 评价指标决定：![](https://lqhoss.oss-cn-beijing.aliyuncs.com/index.jpg)
   
## Usage
Run the following files in the particular order:

| Order | Run | Generated json file |
| ---- | ---- | ----|
| 1 | /evaluationIndex/allTestsCompleteRate.py<br>/evaluationIndex/commitTimes.py<br>/evaluationIndex/eachTypeTestCompleteRate.py<br>/evaluationIndex/scoreIncreaseRates.py<br>/evaluationIndex/scoreRank.py | allTestsCompleteRate.json<br>commitTimesRank.json<br>eachTypeCompleteRate.json<br>scoreRatesRank.json<br>scoreRank.json
| 2 | /FAHP/dataCollect.py<br>/FAHP/FAHP.py | dataCollect.json<br>dataSet.json |
| 3 | /BPNN/BPNN.py | model.h5 |
| 4 | /BPNN/BPNN_predict.py | - |

## Contributing
[@LiQuanhongl](https://github.com/LiQuanhongl)

[@yuchenyang19](https://github.com/yuchenyang19)

[@181250201](https://github.com/181250201)


## License
