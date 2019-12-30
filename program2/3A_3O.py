<<<<<<< HEAD
import numpy as np
import math 
import random

hidden = [1,5,10,1520]
learning = [0.3,0.5,0.7,1]

number_of_input = 4
number_of_output = 3
target_RMSE = 0.15
MAX_epoch = 50000



file = open("iris_training_data.txt","r")
train_lists = file.readlines() # 以行分開


file = open("iris_testing_data.txt","r")
test_lists = file.readlines() # 以行分開


def backpropogation(hidden_layer,learning_rate):

	print("Number of hidden layer neural : " ,hidden_layer)
	print("The learning rate : ",learning_rate)
	# 各種開矩陣
	w1 = np.zeros((hidden_layer,number_of_input),dtype = np.float)
	b1 = np.zeros((hidden_layer,1),dtype = np.float)
	a1 = np.zeros((hidden_layer,1),dtype = np.float)
	error1 = np.zeros((hidden_layer,1),dtype = np.float)

	w2 = np.zeros((number_of_output,hidden_layer),dtype = np.float)
	b2 = np.zeros((number_of_output,1),dtype = np.float)
	a2 = np.zeros((number_of_output,1),dtype = np.float)
	error2 = np.zeros((number_of_output,1),dtype = np.float)
	p = np.array([[6],[2.7],[5.1],[1.6]])
	t = np.array([[0.1],[0.9],[0.1]])

	# 各種初始化
	for i in range(0,hidden_layer):
		for j in range(0,number_of_input):
			w1[i][j] = random.random()
		b1[i] = random.random()

	for i in range(0,number_of_output):
		for j in range(0,hidden_layer):
			w2[i][j] = random.random()
		b2[i] = random.random()

	print("The init w1:",w1)
	print("The init b1:",b1)
	print("The init w2:",w2)
	print("The init b2:",b2)


	RMSE = 0.5
	min_RMSE = 1
	epoch = 0

	while(RMSE > target_RMSE and epoch < MAX_epoch):
		epoch += 1


		RMSE = 0.


		for li in train_lists:
			# p 跟 t 的設定(讀黨)
			li = li.strip('\n').split(" " )
			index = 0
			for i in li:
				if(index == 4):
					if(i == 'versicolor'):
						t = ([[0.1],[0.9],[0.1]])
					elif(i == 'virginica'):
						t = ([[0.1],[0.1],[0.9]])
					elif(i == 'setosa'):
						t = ([[0.9],[0.1],[0.1]])
				elif(index < 4):
					i = float(i)
					p[index] = i

				index += 1		

			# 計算a1
			for i in range(0,hidden_layer):
				temp = w1[i].dot(p)+b1[i]
				temp = 1 / (1 + math.exp(-temp))
				a1[i] = temp


			# 計算a2
			for i in range(0,number_of_output):
				temp = w2[i].dot(a1) + b2[i]
				temp = 1 / (1 + math.exp(-temp))
				a2[i] = temp

			# 計算誤差值 & 計算RMSE
			RMSE_temp = 0.
			for i in range(0,number_of_output):
				temp = (t[i] - a2[i]) * a2[i] * (1 - a2[i])
				error2[i] = temp

				RMSE_temp += pow((t[i] - a2[i]),2)

			for i in range(0,hidden_layer):
				temp = 0
				for j in range(0,number_of_output):
					temp += w2[j][i] * error2[j]
				temp = temp * a1[i] * (1 - a1[i])
				error1[i] = temp

			# 更新的部分

			for i in range(0,number_of_output):
				for j in range(0,hidden_layer):
					temp = w2[i][j] + 2 * learning_rate * error2[i] * a1[j]
					w2[i][j] = temp
				temp = b2[i] + 2 * learning_rate * error2[i]
				b2[i] = temp

			for i in range(0,hidden_layer):
				for j in range(0,number_of_input):
					temp = w1[i][j] + 2* learning_rate * error1[i] * p[j]
					w1[i][j] = temp
				temp = b1[i] + 2 * learning_rate * error1[i]
				b1[i] = temp

			RMSE_temp /= 120
			RMSE += math.sqrt(RMSE_temp)

			# if(RMSE < min_RMSE):
			# 	min_RMSE = RMSE
			# 	ans_w1 = w1
			# 	ans_b1 = b1
			# 	ans_b2 = b2
			# 	ans_w2 = w2

	print("The training epoch : ", epoch)

	print("The finial w1 : ",w1)
	print("The finial b1 : ",b1)
	print("The finial w2 : ",w2)
	print("The finial b2 : ",b2)
	correct = 0

	# 計算 錯誤率

	for li in train_lists:
		# p 跟 t 的設定(讀黨)
		li = li.strip('\n').split(" " )
		index = 0
		for i in li:
			if(index == 4):
				if(i == 'versicolor'):
					t = ([[0.1],[0.9],[0.1]])
				elif(i == 'virginica'):
					t = ([[0.1],[0.1],[0.9]])
				elif(i == 'setosa'):
					t = ([[0.9],[0.1],[0.1]])
			elif(index < 4):
				i = float(i)
				p[index] = i

			index += 1	

		# 計算a1
		for i in range(0,hidden_layer):
				temp = w1[i].dot(p)+b1[i]
				temp = 1 / (1 + math.exp(-temp))
				a1[i] = temp

		# 計算a2
		for i in range(0,number_of_output):
			temp = w2[i].dot(a1) + b2[i]
			temp = 1 / (1 + math.exp(-temp))
			a2[i] = temp

		max_index = 0

		for i in range(0,number_of_output):
			if(a2[i] > a2[max_index]):
				max_index = i
		
		if(max_index == 0):
			a = np.array([[0.9],[0.1],[0.1]])
		elif(max_index == 1):
			a = np.array([[0.1],[0.9],[0.1]])
		elif(max_index == 2):
			a = np.array([[0.1],[0.1],[0.9]])

		if((a == t).all()):
			correct += 1

	print("The Correct rate of training data : ",correct/120*100)


	correct = 0

	for li in test_lists:
		# p 跟 t 的設定(讀黨)
		li = li.strip('\n').split(" " )
		index = 0
		for i in li:
			if(index == 4):
				if(i == 'versicolor'):
					t = ([[0.1],[0.9],[0.1]])
				elif(i == 'virginica'):
					t = ([[0.1],[0.1],[0.9]])
				elif(i == 'setosa'):
					t = ([[0.9],[0.1],[0.1]])
			elif(index < 4):
				i = float(i)
				p[index] = i

			index += 1	

		# 計算a1
		for i in range(0,hidden_layer):
				temp = w1[i].dot(p)+b1[i]
				temp = 1 / (1 + math.exp(-temp))
				a1[i] = temp

		# 計算a2
		for i in range(0,number_of_output):
			temp = w2[i].dot(a1) + b2[i]
			temp = 1 / (1 + math.exp(-temp))
			a2[i] = temp

		max_index = 0

		for i in range(0,number_of_output):
			if(a2[i] > a2[max_index]):
				max_index = i
		
		if(max_index == 0):
			a = np.array([[0.9],[0.1],[0.1]])
		elif(max_index == 1):
			a = np.array([[0.1],[0.9],[0.1]])
		elif(max_index == 2):
			a = np.array([[0.1],[0.1],[0.9]])

		if((a == t).all()):
			correct += 1

	print("The Correct rate of testing data : ",correct/30*100)


for q in range(0,len(hidden)):
	for w in range(0,len(learning)):
		print("=========================================")
		backpropogation(hidden[q],learning[w])
		print("=========================================")


=======
import numpy as np
import math 
import random

hidden = [5,10,15,20]
learning = [0.3,0.5,0.7,1]

# hidden_layer = 5
number_of_input = 4
number_of_output = 3
# learning_rate = 1
target_RMSE = 0.15
MAX_epoch = 50000

def backpropogation(hidden_layer,learning_rate):

	print("Number of hidden layer neural : " ,hidden_layer)
	print("The learning rate : ",learning_rate)
	# 各種開矩陣
	w1 = np.zeros((hidden_layer,number_of_input),dtype = np.float)
	b1 = np.zeros((hidden_layer,1),dtype = np.float)
	a1 = np.zeros((hidden_layer,1),dtype = np.float)
	error1 = np.zeros((hidden_layer,1),dtype = np.float)

	w2 = np.zeros((number_of_output,hidden_layer),dtype = np.float)
	b2 = np.zeros((number_of_output,1),dtype = np.float)
	a2 = np.zeros((number_of_output,1),dtype = np.float)
	error2 = np.zeros((number_of_output,1),dtype = np.float)
	p = np.array([[6],[2.7],[5.1],[1.6]])
	t = np.array([[0.1],[0.9],[0.1]])

	# 各種初始化
	for i in range(0,hidden_layer):
		for j in range(0,number_of_input):
			w1[i][j] = random.random()
		b1[i] = random.random()

	for i in range(0,number_of_output):
		for j in range(0,hidden_layer):
			w2[i][j] = random.random()
		b2[i] = random.random()

	print("The init w1:",w1)
	print("The init b1:",b1)
	print("The init w2:",w2)
	print("The init b2:",b2)


	RMSE = 0.5
	min_RMSE = 1
	epoch = 0

	while(RMSE > target_RMSE and epoch < MAX_epoch):
		epoch += 1
		file = open("iris_training_data.txt","r")
		lists = file.readlines() # 以行分開
		datalen = len(lists)

		RMSE = 0.


		for li in lists:
			# p 跟 t 的設定(讀黨)
			li = li.strip('\n').split(" " )
			index = 0
			for i in li:
				if(index == 4):
					if(i == 'versicolor'):
						t = ([[0.1],[0.9],[0.1]])
					elif(i == 'virginica'):
						t = ([[0.1],[0.1],[0.9]])
					elif(i == 'setosa'):
						t = ([[0.9],[0.1],[0.1]])
				elif(index < 4):
					i = float(i)
					p[index] = i

				index += 1		

			# 計算a1
			for i in range(0,hidden_layer):
				temp = w1[i].dot(p)+b1[i]
				temp = 1 / (1 + math.exp(-temp))
				a1[i] = temp


			# 計算a2
			for i in range(0,number_of_output):
				temp = w2[i].dot(a1) + b2[i]
				temp = 1 / (1 + math.exp(-temp))
				a2[i] = temp

			# 計算誤差值 & 計算RMSE
			RMSE_temp = 0.
			for i in range(0,number_of_output):
				temp = (t[i] - a2[i]) * a2[i] * (1 - a2[i])
				error2[i] = temp

				RMSE_temp += pow((t[i] - a2[i]),2)

			for i in range(0,hidden_layer):
				temp = 0
				for j in range(0,number_of_output):
					temp += w2[j][i] * error2[j]
				temp = temp * a1[i] * (1 - a1[i])
				error1[i] = temp

			# 更新的部分

			for i in range(0,number_of_output):
				for j in range(0,hidden_layer):
					temp = w2[i][j] + 2 * learning_rate * error2[i] * a1[j]
					w2[i][j] = temp
				temp = b2[i] + 2 * learning_rate * error2[i]
				b2[i] = temp

			for i in range(0,hidden_layer):
				for j in range(0,number_of_input):
					temp = w1[i][j] + 2* learning_rate * error1[i] * p[j]
					w1[i][j] = temp
				temp = b1[i] + 2 * learning_rate * error1[i]
				b1[i] = temp

			RMSE_temp /= 120
			RMSE += math.sqrt(RMSE_temp)

			if(RMSE < min_RMSE):
				min_RMSE = RMSE
				ans_w1 = w1
				ans_b1 = b1
				ans_b2 = b2
				ans_w2 = w2

	print("The training epoch : ", epoch)

	print("The finial w1 : ",ans_w1)
	print("The finial b1 : ",ans_b1)
	print("The finial w2 : ",ans_w2)
	print("The finial b2 : ",ans_b2)
	correct = 0

	# 計算 錯誤率
	file = open("iris_training_data.txt","r")
	lists = file.readlines() # 以行分開
	datalen = len(lists)

	for li in lists:
		# p 跟 t 的設定(讀黨)
		li = li.strip('\n').split(" " )
		index = 0
		for i in li:
			if(index == 4):
				if(i == 'versicolor'):
					t = ([[0.1],[0.9],[0.1]])
				elif(i == 'virginica'):
					t = ([[0.1],[0.1],[0.9]])
				elif(i == 'setosa'):
					t = ([[0.9],[0.1],[0.1]])
			elif(index < 4):
				i = float(i)
				p[index] = i

			index += 1	

		# 計算a1
		for i in range(0,hidden_layer):
				temp = w1[i].dot(p)+b1[i]
				temp = 1 / (1 + math.exp(-temp))
				a1[i] = temp

		# 計算a2
		for i in range(0,number_of_output):
			temp = w2[i].dot(a1) + b2[i]
			temp = 1 / (1 + math.exp(-temp))
			a2[i] = temp

		max_index = 0

		for i in range(0,number_of_output):
			if(a2[i] > a2[max_index]):
				max_index = i
		
		if(max_index == 0):
			a = np.array([[0.9],[0.1],[0.1]])
		elif(max_index == 1):
			a = np.array([[0.1],[0.9],[0.1]])
		elif(max_index == 2):
			a = np.array([[0.1],[0.1],[0.9]])

		if((a == t).all()):
			correct += 1

	print("The Correct rate of training data : ",correct/120*100)


	correct = 0
	file = open("iris_testing_data.txt","r")
	lists = file.readlines() # 以行分開
	datalen = len(lists)

	for li in lists:
		# p 跟 t 的設定(讀黨)
		li = li.strip('\n').split(" " )
		index = 0
		for i in li:
			if(index == 4):
				if(i == 'versicolor'):
					t = ([[0.1],[0.9],[0.1]])
				elif(i == 'virginica'):
					t = ([[0.1],[0.1],[0.9]])
				elif(i == 'setosa'):
					t = ([[0.9],[0.1],[0.1]])
			elif(index < 4):
				i = float(i)
				p[index] = i

			index += 1	

		# 計算a1
		for i in range(0,hidden_layer):
				temp = w1[i].dot(p)+b1[i]
				temp = 1 / (1 + math.exp(-temp))
				a1[i] = temp

		# 計算a2
		for i in range(0,number_of_output):
			temp = w2[i].dot(a1) + b2[i]
			temp = 1 / (1 + math.exp(-temp))
			a2[i] = temp

		max_index = 0

		for i in range(0,number_of_output):
			if(a2[i] > a2[max_index]):
				max_index = i
		
		if(max_index == 0):
			a = np.array([[0.9],[0.1],[0.1]])
		elif(max_index == 1):
			a = np.array([[0.1],[0.9],[0.1]])
		elif(max_index == 2):
			a = np.array([[0.1],[0.1],[0.9]])

		if((a == t).all()):
			correct += 1

	print("The Correct rate of testing data : ",correct/30*100)

for q in range(0,4):
	for w in range(0,4):
		print("=========================================")
		backpropogation(hidden[q],learning[w])
		print("=========================================")


>>>>>>> 219d9ecbc26c643c2bed1fcf200eae21bd5dcf09
	