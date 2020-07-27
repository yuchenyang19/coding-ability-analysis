import numpy as np
import matplotlib.pyplot as plt
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers.core import Dense, Activation,Dropout
import json

# 读数据
x_data = []
y_data = []
f = open('dataSet.json')
res = f.read()
data = json.loads(res)
for k,v in data.items():
    user_x = []
    user_x.append(v["s11"])
    user_x.append(v["s12"])
    user_x.append(v["s21"])
    user_x.append(v["s22"])
    user_x.append(v["s23"])
    user_x = np.array(user_x)
    user_y =[]
    user_y.append(v["score"])
    user_y = np.array(user_y)
    x_data.append(user_x)
    y_data.append(user_y)
x_data = np.array(x_data)
y_data = np.array(y_data)
x_max = x_data.max()
x_min = x_data.min()
x_data_nor = (x_data - x_min)/(x_max - x_min)
y_max = y_data.max()
y_min = y_data.min()
y_data_nor = (y_data - y_min)/(y_max-y_min)
x_train = x_data_nor[:200]
y_train = y_data_nor[:200]
x_valid = x_data_nor[200:250]
y_valid = y_data_nor[200:250]

epoch = 60000 #迭代次数
inputnum = 5  #输入层节点个数
midnum = 5 #隐含层节点个数
outputnum = 1 #输出层节点个数

# 构建模型
model = Sequential()
model.add(Dense(midnum, activation='tanh', input_dim=inputnum))
model.add(Dense(outputnum, activation='sigmoid'))
sgd = SGD(lr=0.01, decay=1e-5, momentum=0.9, nesterov=True)
model.compile(loss='mse',
              optimizer=sgd,
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=epoch,batch_size=10,validation_data=(x_valid, y_valid))
plt.plot(model.predict(x_data_nor[250:]),'r')
plt.plot(y_data_nor[250:],'b')
plt.show()
model.save('model.h5')