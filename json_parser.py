import pandas


with open('full_format_recipes.json', 'r') as file:
	recipes = file.read()
file.close()

# recs = recipes.split("directions\": [\"")
# new_recs = [i.split(']')[0][:-1] for i in recs]
# new_recs = new_recs[1:]

# recipe_string_lengths = [len(i) for i in new_recs]
# print(len(recipe_string_lengths))

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

df = pandas.DataFrame(recs_dict)
df.to_csv('new.csv', index = False)

# with open('new.csv','w+') as csvfile:
# 	csvfile.write(csv_string)

# csvfile.close()
# data['recipe_length'] = recipe_string_lengths

# s = data.to_csv()

# with open('new_recipesData.csv', 'w+') as new_file:
# 	new_file.write(s)