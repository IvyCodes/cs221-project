import pandas
import util

with open('full_format_recipes.json', 'r') as file:
	recipes = file.read()
file.close()

# recs = recipes.split("directions\": [\"")
# new_recs = [i.split(']')[0][:-1] for i in recs]
# new_recs = new_recs[1:]

# recipe_string_lengths = [len(i) for i in new_recs]
# print(len(recipe_string_lengths))
ingredient_names = util.ingredient_names()


new_recs = recipes.split('{')
# new_recs = [i.split(',')[0] for i in recs][1:]
# print(new_recs[0:5])
# print(new_recs[-5:])
print(len(new_recs))

recs_dict = {'rating':[], 'directions':[], 'ingredients':[]}
total = 0
num_ok = 0
for r in new_recs:
	total+=1
	if '\"directions\": [' in r and "\"rating\": " in r and '\"ingredients\": [' in r:
		num_ok+=1
		rating = r.split("\"rating\": ")[1].split(',')[0]
		directions = r.split("\"directions\": [")[1].split(']')[0]
		ingredients = r.split('\"ingredients\": [')[1].split(']')[0]
		title = r.split('\"title\": \"')[1].split('\"')[0]
		
		# print(len(ingredients))
		try:
			rating = float(rating)
		except:
			pass
		else:
			if len(directions) > 5 and len(ingredients)>5:
				recs_dict['rating'].append(rating)
				recs_dict['directions'].append(directions)
				recs_dict['ingredients'].append(ingredients)
				# print(title)
				# print(ingredients)
				# print(directions)
				# print('\n')
				# print('\n')



recs_dict['direction_lengths'] = [len(i) for i in recs_dict['directions']]
recs_dict['ingredient_lengths'] = [len(i) for i in recs_dict['ingredients']]


for ingredient in ingredient_names:
	recs_dict[ingredient + '_freq'] = [i.count(ingredient) for i in recs_dict['ingredients']]
	recs_dict['has_' + ingredient] = [1 if i > 0 else 0 for i in recs_dict[ingredient + '_freq']]

data = pandas.DataFrame(recs_dict)
train = data.sample(frac=0.6)
test = data.drop(train.index)
validation = test.sample(frac = 0.5)
test = test.drop(validation.index)

train.to_csv('train_data.csv', index = False)
validation.to_csv('validation_data.csv', index = False)
test.to_csv('test_data.csv', index = False)

print(len(train))
print(len(test))
print(len(validation))
