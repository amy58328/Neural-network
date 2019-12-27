import numpy as np
import math 

w1 = np.array([0.1,0.1,0.1,0.1])

b1 = np.array([0.1])

p1 = np.array([
	[1],
	[1],
	[1],
	[1]
])

t = np.array([
	[0.9],
	[0.9],
	[0.9]
])

an1 = w1.dot(p1) + b1

print(an1)

a1 = 1 / (1+math.exp(-an1))

print(a1)

w2 = np.array([
	[0.1],
	[0.1],
	[0.1]
])

b2 = np.array([
	[0.1],
	[0.1],
	[0.1]
])


an2 = w2*a1 + b2
print(an2)


# 計算誤差值
error = np.array([
	[0],
	[0],
	[0]
])

for i in range(0,len(w2)):
	error[i] = (t[i] - an2[i]) * an2[i] *(1-an2[i])

print(error)

# 更新開始

