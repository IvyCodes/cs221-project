import pandas
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import util

def get_KNN_predictions(train, test, x_cols, y_cols, n_neighbors = 10):
	knn = KNeighborsRegressor(n_neighbors = n_neighbors)
	knn.fit(train[x_cols], train[y_col])
	prediction = knn.predict(test[x_cols])
	return prediction

with open("train_data.csv", 'r') as csvfile:
	train = pandas.read_csv(csvfile)
csvfile.close()

with open("validation_data.csv", 'r') as csvfile:
	validate = pandas.read_csv(csvfile)
csvfile.close()

print('Training set size = ' + str(len(train)))
print('Validation set size = ' + str(len(validate)))

x_cols = train.columns.values[3:]
# x_cols = []
# x_cols.extend(util.direction_length_labels())
# x_cols.extend(util.ingredient_length_labels())
# # x_cols.extend(util.has_ingredient_labels())
y_col = train.columns.values[0]
# print(x_cols)
actual = validate[y_col]
n = 105
prediction = get_KNN_predictions(train, validate, x_cols, y_col, n_neighbors = n)

# accs = []
# plot = []
# ns = []
# for n in range(8):
# 	print(n)
# 	prediction = get_KNN_predictions(train,validate, x_cols, y_col, n_neighbors = n+100)
# 	acc = util.get_accuracy(prediction,actual)
# 	accs.append((n+100,acc))
# 	plot.append(acc)
# 	ns.append(n+100)
# 	print(acc)

# accs.sort(key = lambda x: x[1])
# print(accs)
# plt.plot(ns,plot)
# plt.show()

acc = util.get_accuracy(prediction,actual)
print(n)
print(acc)
util.make_accuracy_plot(prediction,actual)
# util.write_accuracy_data(prediction, actual, 'KNN_results.csv')

