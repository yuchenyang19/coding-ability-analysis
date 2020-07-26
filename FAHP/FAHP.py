import numpy as np
import json


# 优先判断矩阵得到模糊一致矩阵
def get_fuzzy_consistent_matrix(matrix):
    r = matrix.sum(axis=1)
    fuzzy_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
    for i in range(len(fuzzy_matrix)):
        for j in range(len(fuzzy_matrix)):
            fuzzy_matrix[i][j] = (r[i] - r[j]) / (2 * len(fuzzy_matrix)) + 0.5
    return fuzzy_matrix


# 模糊一致矩阵计算出权值
def get_weight(fuzzy_matrix):
    r = fuzzy_matrix.sum(axis=1)
    n = fuzzy_matrix.shape[0]
    w = np.zeros(n)
    alpha = (n - 1) / 2
    for i in range(n):
        w[i] = 1 / n - 1 / (2 * alpha) + r[i] / (n * alpha)
    return w


# 梯度分布法求隶属度
def get_t1(pt):
    if pt >= 90:
        return 1
    elif pt >= 80:
        return (pt - 80) / 10
    else:
        return 0


def get_t2(pt):
    if pt >= 90:
        return (100 - pt) / 10
    elif pt >= 80:
        return 1
    elif pt >= 70:
        return (pt - 70) / 10
    else:
        return 0


def get_t3(pt):
    if pt >= 90:
        return 0
    elif pt >= 80:
        return (90 - pt) / 10
    elif pt >= 70:
        return 1
    elif pt >= 60:
        return (pt - 60) / 10
    else:
        return 0


def get_t4(pt):
    if pt >= 80:
        return 0
    elif pt >= 70:
        return (80 - pt) / 10
    elif pt >= 60:
        return 1
    else:
        return pt / 60


def get_t5(pt):
    if pt >= 70:
        return 0
    elif pt >= 60:
        return (70 - pt) / 10
    else:
        return 1


# 由指标得分得到每个模糊评估矩阵t
def get_fuzzy_evaluation_vector(pt):
    f = np.zeros(5)
    f[0] = get_t1(pt)
    f[1] = get_t2(pt)
    f[2] = get_t3(pt)
    f[3] = get_t4(pt)
    f[4] = get_t5(pt)
    return f


def get_fuzzy_evaluation_matrix(pt_list):
    li = []
    for i in range(len(pt_list)):
        li.append(get_fuzzy_evaluation_vector(pt_list[i]))
    t = np.array(li)
    return t


# 由权重w与模糊评估矩阵t相乘，并求出评估结果Q
def get_evaluation(w, t):
    q_vector = w.dot(t)
    q_sum = q_vector.sum()
    q_vector = q_vector / q_sum
    q = 0
    for i in range(5):
        if i != 4:
            q += q_vector[i] * (95 - i * 10)
        else:
            q += q_vector[i] * 30
    return q


# 优先关系矩阵
f1 = np.array([[0.5, 0.8],
               [0.2, 0.5]])
f2 = np.array([[0.5, 0.4],
               [0.6, 0.5]])
f3 = np.array([[0.5, 0.7, 0.7],
               [0.3, 0.5, 0.6],
               [0.3, 0.4, 0.5]])

li = []
li.append(f2)
li.append(f3)

f_weight_li = []
for i in range(len(li)):
    f_weight_li.append(get_weight(get_fuzzy_consistent_matrix(li[i])))

f1_weight = get_weight(get_fuzzy_consistent_matrix(f1))

f = open('dataCollect.json')
res = f.read()
data = json.loads(res)

for key, value in data.items():
    stu_list = []
    s1 = []
    s1.append(value["s11"])
    s1.append(value["s12"])
    s2 = []
    s2.append(value["s21"])
    s2.append(value["s22"])
    s2.append(value["s23"])
    stu_list.append(s1)
    stu_list.append(s2)
    f1_matrix = []
    for i in range(len(stu_list)):
        f1_matrix.append(get_evaluation(f_weight_li[i], get_fuzzy_evaluation_matrix(stu_list[i])))
    f1_matrix = np.array(f1_matrix)
    value["score"] = round(get_evaluation(f1_weight, get_fuzzy_evaluation_matrix(f1_matrix)), 2)

f_result = open("dataSet.json", 'w')
f_result.write(json.dumps(data, indent=4))
f_result.close()
