# coding_ability_analysis
2020年数据科学基础大作业 Python编程能力分析

## to-do
1. 如何选择学生的编程能力评价指标？
    - 数据预处理：
        - 题目完成率
        - 各种题目类型完成率
        - 编程行为（提交次数、每次的提交得分）
        - 最终得分等等
    - 重复值、异常值处理
    - 将定性数据转化为定量数据
    - 数据规范化（min-max规范化）
    - 评价指标决定：![](https://lqhoss.oss-cn-beijing.aliyuncs.com/index.jpg)
    
2. 如何自动评价学生的编程水平？
    - 指标量化：
        - 分别运行evaluationIndex目录下的py文件，获得的“allTestsCompleteRate.json”、“commitTimesRank.json”、“eachTypeCompleteRate.json”、“scoreRank.json”、“scoreRatesRank.json”文件移到FAHP目录下（仓库中已经有这些文件）
    - 模糊层次分析：
        - 运行FAHP目录下的dataCollect.py文件
        - 运行FAHP目录下的FAHP.py文件,对学生编程能力进行评估，将生成的“dataSet.json”文件移动到BPNN目录下（仓库中已经有该文件）
    - bp神经网络：
       - 运行BPNN目录下的BPNN.py文件
       - 之后便可使用该模型对学生编程能力进行评估（BPNN目录下的BPNN_predict.py文件）
