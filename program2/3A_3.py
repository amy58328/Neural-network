import numpy as np
import math 
import random

hidden_layer = 1
number_of_input = 2
number_of_output = 2
learning_rate = 0.3

# 各種開矩陣
# w1 = np.zeros((hidden_layer,number_of_input),dtype = np.float)
# b1 = np.zeros((hidden_layer,1),dtype = np.float)
a1 = np.zeros((hidden_layer,1),dtype = np.float)
error1 = np.zeros((hidden_layer,1),dtype = np.float)

# w2 = np.zeros((number_of_output,hidden_layer),dtype = np.float)
# b2 = np.zeros((number_of_output,1),dtype = np.float)
a2 = np.zeros((number_of_output,1),dtype = np.float)
error2 = np.zeros((number_of_output,1),dtype = np.float)

# 各種初始化
# for i in range(0,hidden_layer):
# 	for j in range(0,number_of_input):
# 		w1[i][j] = random.random()
# 	b1[i] = random.random()

# for i in range(0,number_of_output):
# 	for j in range(0,hidden_layer):
# 		w2[i][j] = random.random()
# 	b2[i] = random.random()
w1 = np.array([0.1 , 0.1])
b1 = np.array([0.1])
w2 = np.array([[0.1],[0.1]])
b2 = np.array([[0.1],[0.1]])

print("w1:",w1)
print("b1:",b1)
print("w2:",w2)
print("b2:",b2)

# p 跟 t 的設定(讀黨)
p = np.array([
	[1.],
	[0.]
])

t = np.array([
	[1.],
	[0.]
])


# 計算a1
for i in range(0,hidden_layer):
	print("w1[i]",w1[i])
	print("p",p)
	temp = w1.dot(p)+b1
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
	temp = b2[i] + 2 * learning_rate * error2[i]
	b2[i] = temp
print("new w2:" , w2)
print("new b2:" , b2)

for i in range(0,hidden_layer):
	for j in range(0,number_of_input):
		temp = w1[j] + 2* learning_rate * error1 * p[j]
		w1[j] = temp
	temp = b1 + 2 * learning_rate * error1
	b1 = temp
print("new w1" , w1	)
print("new b1:" , b1)

