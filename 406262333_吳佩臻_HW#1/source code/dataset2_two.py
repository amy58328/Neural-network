import numpy  as np

# 各種初始
p = np.array([
	[0.],
	[0.],
	[0.]
])

t = np.array([
	[0],
	[0]
])

a = np.array([
	[1],
	[1]
])

w = np.array([
	[0.,0.,1.],
	[1.,1.,1.]
])

b = np.array([
	[1.],
	[1.]
])

W = np.array([
	[0],
	[0]
])

P = np.array([
	[1],
	[0]
])

B = np.array([
	[1],
	[1]
])

O = np.array([
	[0],
	[1]
])
# 初始end

def hardlim(n):
	index = 0
	for i in n:
		if(i < 0):
			a[index] = 0
		else:
			a[index] = 1
		index += 1

# trainging 
file = open("training_data.txt","r")
lists = file.readlines() # 以行分開
datalen = len(lists)
corr = 0
while(corr != datalen):
	corr = 0
	for li in lists:
		li = li.strip('\n').split(" ") # 用空格切開每行的數值
		index = 0
		for i in li:
			if(index == 3): # 找到t
				if( i == 'W'):
					t = W
				elif(i == 'P'):
					t = P
				elif(i == 'O'):
					t = O
				elif(i == 'B'):
					t = B
			else:# 分割出x,y
				i = float(i)
				p[index] = i
			index += 1

		n = w.dot(p) + b

		hardlim(n)

		if(~(a == t).all()):
			e = t - a
			w = w + e.dot(p.T)
			b = b + e
		else:
			corr += 1
#training end

#test
file = open("testing_data.txt","r")
lists = file.readlines() # 以行分開

dataindex = 1
for li in lists:
	li = li.strip('\n').split(" ")
	index = 0
	for i in li:
		i = float(i)
		p[index] = i
		index += 1

	n = w.dot(p) + b

	hardlim(n)

	if((a == W).all()):
		print(dataindex,"W")
	elif((a == B).all()):
		print(dataindex,"B")
	elif((a == O).all()):
		print(dataindex,"O")
	elif((a == P).all()):
		print(dataindex,"P")
	dataindex += 1








