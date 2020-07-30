from keras.models import load_model

# 可以使用该模型进行预测（输入学生的指标数据进行对编程能力的评估）
model = load_model('../data/model.h5')

# 过程：1、读取数据
#      2、将数据进行归一化处理
#      3、调用model.predict()进行预测
#      4、反归一化得到预测结果
