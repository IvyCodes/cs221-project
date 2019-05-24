import pandas
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import util





def get_baseline_predictions(train, test, x_cols, y_col):
	avg = train[y_col[0]].sum()/len(train)
	prediction = [avg]*len(test)
	return prediction


def get_KNN_predictions(train, test, x_cols, y_cols, n_neighbors = 100):
	knn = KNeighborsRegressor(n_neighbors=200)
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

# print(data.columns.values) #list of all column names
x_cols = train.columns.values[3:]
y_col = train.columns.values[0]

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

actual = validate[y_col]
prediction = get_KNN_predictions(train, validate, x_cols, y_col)
acc = util.get_accuracy(prediction,actual)

print(acc)