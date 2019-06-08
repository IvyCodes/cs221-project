import pandas
import numpy as np
import util
import pickle

def get_embedding(recipe, x_cols, embeddings, count_ingredients = False):
	num_ingredients = 0
	recipe_embedding = np.array([0]*len(list(embeddings.values())[0]))
	for x in x_cols:
		num_appearances = recipe[x] if count_ingredients else min(1,recipe[x])
		num_ingredients += num_appearances
		recipe_embedding = recipe_embedding + embeddings[x[0:-5]]*num_appearances
	if num_ingredients == 0:
		recipe_embedding = np.array([0]*len(list(embeddings.values())[0]))
		# print(recipe)
	else:
		recipe_embedding = recipe_embedding/num_ingredients

	return recipe_embedding


def apply_recipe_embedding(data, x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle'):
	infile = open(embedding_file, 'rb')
	embeddings = pickle.load(infile) #dict from ingredient -> embedding
	infile.close()
	new_x_cols = ['x' + str(i) for i in range(len(list(embeddings.values())[0]))]
	# print(new_x_cols)

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

with open("test_data.csv", 'r') as csvfile:
	test = pandas.read_csv(csvfile)
csvfile.close()

print('Training set size = ' + str(len(train)))
print('Validation set size = ' + str(len(validate)))
print('Test set size = ' + str(len(test)))

#for making new embedding data
y_col = train.columns.values[0]
old_x_cols = util.ingredient_freq_labels()
train, x_cols, y_col = apply_recipe_embedding(train, old_x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle')
print(train)
validate, _, _ = apply_recipe_embedding(validate, old_x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle')
test, _, _ = apply_recipe_embedding(test, old_x_cols, y_col, embedding_file = 'ingredient_embeddings.pickle')

train.to_csv('train_data_embeddings.csv',index = False)
test.to_csv('test_data_embeddings.csv',index = False)
validate.to_csv('validate_data_embeddings.csv',index = False)


