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

def get_embedding(recipe, x_cols, embeddings, count_ingredients = False):
	num_ingredients = 0
	recipe_embedding = np.array([0]*len(list(embeddings.values())[0]))
	for x in x_cols:
		num_appearances = recipe[x] if count_ingredients else min(1,recipe[x])
		num_ingredients += num_appearances
		recipe_embedding = recipe_embedding + embeddings[x[0:-5]]*num_appearances
	recipe_embedding = recipe_embedding/num_ingredients
	if num_ingredients == 0:
		recipe_embedding = np.array([0]*len(list(embeddings.values())[0]))
		print(recipe)
	return recipe_embedding


def apply_recipe_embedding(data, x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle'):
	infile = open(embedding_file, 'rb')
	embeddings = pickle.load(infile) #dict from ingredient -> embedding
	infile.close()
	new_x_cols = ['x' + str(i) for i in range(len(list(embeddings.values())[0]))]
	print(new_x_cols)

	new_y_col = y_col


	data_entries = []
	for index, row in data.iterrows():
		entry = dict(zip(new_x_cols, get_embedding(row, x_cols, embeddings)))
		entry[new_y_col] = row[y_col]
		data_entries.append(entry)

	new_data = pandas.DataFrame(data_entries)
	return new_data, new_x_cols, new_y_col

with open("train_data.csv", 'r') as csvfile:
	train = pandas.read_csv(csvfile)
csvfile.close()

with open("validation_data.csv", 'r') as csvfile:
	validate = pandas.read_csv(csvfile)
csvfile.close()

print('Training set size = ' + str(len(train)))
print('Validation set size = ' + str(len(validate)))


# old_x_cols = util.ingredient_freq_labels()
# y_col = train.columns.values[0]
# train, x_cols, y_col = apply_recipe_embedding(train, old_x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle')
# validate, _, _ = apply_recipe_embedding(validate, old_x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle')
# outfile = open('train.pickles','wb')
# pickle.dump(train, outfile)
# outfile.close()
# outfile = open('validate.pickles','wb')
# pickle.dump(validate, outfile)
# outfile.close()

#for reading embedding data
infile = open('train.pickles','rb')
pickle.dump(train, outfile)
infile.close()
infile = open('validate.pickles','rb')
pickle.dump(validate, outfile)
infile.close()


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

