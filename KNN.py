import pandas
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt


def find_accuracy(prediction,actual):
	num_correct = 0
	for (x,y) in zip(prediction,actual):
		if y-1 <= x <= y+1:
			num_correct+=1
	# print(str(num_correct) + ' out of ' + str(len(actual)) + ' correct')
	# print('Accuracy = ' + str(num_correct/len(actual)))
	return num_correct/len(actual)


def get_baseline_predictions(train, test, x_cols, y_col):
	avg = train[y_col[0]].sum()/len(train)
	prediction = [avg]*len(test)
	return prediction


def get_KNN_predictions(train, test, x_cols, y_cols, n_neighbors = 100):
	knn = KNeighborsRegressor(n_neighbors=5000)
	knn.fit(train[x_cols], train[y_col])
	prediction = knn.predict(test[x_cols])
	return prediction

with open("recipes.csv", 'r') as csvfile:
	data = pandas.read_csv(csvfile)
csvfile.close()

# data = data.sample(frac = 0.5)
train=data.sample(frac=0.8,random_state=500)
test=data.drop(train.index)

print('Training set size = ' + str(len(train)))
print('Test set size = ' + str(len(test)))

# print(data.columns.values) #list of all column names
x_cols = data.columns.values[1:]
y_col = ['Rating']

# accs = []
# for i in range(len(train)/100):
# 	knn = KNeighborsRegressor(n_neighbors=i*100+1)
# 	knn.fit(train[x_cols], train[y_col])
# 	prediction = knn.predict(test[x_cols])
# 	actual = test[y_col[0]]
# 	acc = find_accuracy(prediction,actual)
# 	accs.append(acc)

# plt.plot(accs)
# plt.show()

# print(x_cols)

actual = test[y_col[0]]
prediction = get_KNN_predictions(train, test, x_cols, y_col)
acc = find_accuracy(prediction,actual)

print(acc)