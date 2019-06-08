import pandas
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np
import util
import pickle

def get_KNN_predictions(train, test, x_cols, y_cols, n_neighbors = 10):
	knn = KNeighborsRegressor(n_neighbors = n_neighbors)
	knn.fit(train[x_cols], train[y_col])
	prediction = knn.predict(test[x_cols])
	return prediction


with open("train_data_embeddings.csv", 'r') as csvfile:
	train = pandas.read_csv(csvfile)
csvfile.close()

with open("test_data_embeddings.csv", 'r') as csvfile:
	test = pandas.read_csv(csvfile)
csvfile.close()

with open("validate_data_embeddings.csv", 'r') as csvfile:
	validate = pandas.read_csv(csvfile)
csvfile.close()

x_cols = ['x' + str(i) for i in range(150)]
y_col = 'rating'

actual = validate[y_col]

n = 110
prediction = get_KNN_predictions(train, validate, x_cols, y_col, n_neighbors = n)

acc = util.get_accuracy(prediction,actual)
print(n)
print(acc)
# util.make_accuracy_plot(prediction,actual)
# util.write_accuracy_data(prediction, actual, 'KNN_results.csv')

# #for tuning k
# accs = []
# plot = []
# ns = []
# for n in range(10):
# 	num_neighbors = n*400+1500
# 	print(num_neighbors)
# 	prediction = get_KNN_predictions(train,validate, x_cols, y_col, n_neighbors = num_neighbors)
# 	acc = util.get_accuracy(prediction,actual)
# 	accs.append((num_neighbors,acc))
# 	plot.append(acc)
# 	ns.append(num_neighbors)
# 	print(acc)

# accs.sort(key = lambda x: x[1])
# print(accs)
# plt.plot(ns,plot)
# plt.show()

