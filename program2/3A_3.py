import numpy as np
import math 
import random

hidden_layer = 1
number_of_input = 4
number_of_output = 3
learning_rate = 0.3

# 各種開矩陣
w1 = np.zeros((hidden_layer,number_of_input),dtype = np.float)
b1 = np.zeros((hidden_layer,1),dtype = np.float)
a1 = np.zeros((hidden_layer,1),dtype = np.float)
error1 = np.zeros((hidden_layer,1),dtype = np.float)

w2 = np.zeros((number_of_output,hidden_layer),dtype = np.float)
b2 = np.zeros((number_of_output,1),dtype = np.float)
a2 = np.zeros((number_of_output,1),dtype = np.float)
error2 = np.zeros((number_of_output,1),dtype = np.float)

# 各種初始化
for i in range(0,hidden_layer):
	for j in range(0,number_of_input):
		w1[i][j] = random.random()
	b1[i] = random.random()

for i in range(0,number_of_output):
	for j in range(0,hidden_layer):
		w2[i][j] = random.random()
	b2[i] = random.random()

print("w1:",w1)
print("b1:",b1)
print("w2:",w2)
print("b2:",b2)

# p 跟 t 的設定(讀黨)
p = np.array([[6],[2.7],[5.1],[1.6]])
t = np.array([[0.1],[0.9],[0.1]])


# 計算a1
for i in range(0,hidden_layer):
	temp = w1[i].dot(p)+b1[i]
	print("temp",temp)
	temp = 1 / (1 + math.exp(-temp))
	a1[i] = temp

print("a1:",a1)

# 計算a2
for i in range(0,number_of_output):
	temp = w2[i].dot(a1) + b2[i]
	temp = 1 / (1 + math.exp(-temp))
	a2[i] = temp
print("a2:",a2)

# 計算誤差值

for i in range(0,number_of_output):
	temp = (t[i] - a2[i]) * a2[i] * (1 - a2[i])
	error2[i] = temp

print("error2:" , error2 )

for i in range(0,hidden_layer):
	temp = 0
	for j in range(0,number_of_output):
		temp += w2[j][i] * error2[j]
	temp = temp * a1[i] * (1 - a1[i])
	error1[i] = temp

print("error1",error1)

# 更新的部分

for i in range(0,number_of_output):
	for j in range(0,hidden_layer):
		temp = w2[i][j] + 2 * learning_rate * error2[i] * a1[j]
		w2[i][j] = temp
print("new w2:" , w2)

for i in range(0,hidden_layer):
	for j in range(0,number_of_input):
		temp = w1[i][j] + 2* learning_rate * error1[i] * p[j]
		w1[i][j] = temp
print("new w1" , w1	)

