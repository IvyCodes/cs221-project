import pandas
import util


def get_baseline_predictions(train, test, x_cols, y_col):
	avg = train[y_col].sum()/len(train)
	prediction = [avg]*len(test)
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

actual = validate[y_col]
prediction = get_baseline_predictions(train, validate, x_cols, y_col)
acc = util.get_accuracy(prediction,actual)

util.make_accuracy_plot(prediction,actual)
util.write_accuracy_data(prediction, actual, 'baseline_results.csv')

print(acc)