import numpy as np

# 宣告p & 初始
p = np.array([
	[0],
	[0]
])

# 宣告a & 初始
a = np.array([
	[0],
	[0]
])


# 宣告t & 初始
t = np.array([
	[0],
	[0]
])

# 宣告w & 初始
w = np.array([
	[1,0],
	[0,1]
])

# 宣告b & 初始
b = np.array([
	[1],
	[1]
])

print("initial weights:\nW = \n",w,"\n")
print("initial biases:\nb = \n",b,"\n")
epoch = 0

# training 
file = open("training_data.txt","r")

lists = file.readlines() #分行
datalen = len(lists)

def hardlim(n):
	index = 0
	for i in n:
		if(i>=0):
			a[index] = 1
		else:
			a[index] = 0
		index += 1

corr = 0
while(corr != datalen):
	epoch += 1
	corr = 0
	for li in lists:
		li = li.strip('\n').split(" ")
		index = 0
		for i in li:
			i = int(i)
			if(index < 2):  # 分割出x,y
				p[index] = i
			else:			# 分割出tx,ty
				j = index-2
				t[j] = i
			index += 1

		n = w.dot(p) + b
		
		hardlim(n)

		if(~(t== a).all()):  #(1)
			e = t - a
			w = w + e.dot(p.T)
			b = b + e
		else:
			corr += 1
#end training

print("final weights:\nW = \n",w,"\n")
print("final biases:\nb = \n",b,"\n")
print("the number of epoch = ",epoch,"\n")
print("the test output:")

# test
file = open("test_data.txt","r")

lists = file.readlines()

for li in lists:
	li = li.strip('\n').split()
	index = 0
	for i in li:
		i = int(i)
		p[index] = i
		index += 1

	n = w.dot(p) + b
	hardlim(n)
	print(a)
# test emd



# (1)
# (t.all() == a.all()) => 只要元素相同 就會是true
# (t == a).all() => 元素相同 而且 順序相同 才會是true

