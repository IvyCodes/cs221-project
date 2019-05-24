import pandas


with open('full_format_recipes.json', 'r') as file:
	recipes = file.read()
file.close()

# recs = recipes.split("directions\": [\"")
# new_recs = [i.split(']')[0][:-1] for i in recs]
# new_recs = new_recs[1:]

# recipe_string_lengths = [len(i) for i in new_recs]
# print(len(recipe_string_lengths))
ingredient_names = ['almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot',
 'artichoke', 'arugula', 'asian pear', 'asparagus', 'avocado', 'bacon', 'bake',
 'banana', 'barley', 'basil', 'bass', 'bean', 'beef', 'beef rib', 'beef shank',
 'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry', 'biscuit', 'bitters',
 'blackberry', 'blender', 'blue cheese', 'blueberry', 'bok choy', 'bourbon',
 'braise', 'bran', 'brandy', 'bread', 'breadcrumbs', 'brie', 'brine', 'brisket',
 'broccoli', 'broccoli rabe', 'brown rice', 'brownie', 'brussel sprout',
 'buffalo', 'bulgur', 'butter', 'buttermilk', 'butternut squash',
 'butterscotch', 'cabbage', 'cake', 'calvados', 'campari', 'candy', 'cantaloupe',
 'capers', 'caraway', 'cardamom', 'carrot', 'cashew', 'casserole/gratin',
 'cauliflower', 'caviar', 'celery', 'chambord', 'champagne', 'chard',
 'chartreuse', 'cheddar', 'cheese', 'cherry', 'chestnut', 'chicago', 'chicken',
 'chickpea', 'chile', 'chile pepper', 'chili', 'chive', 'chocolate', 'cilantro',
 'cinnamon', 'citrus', 'clam', 'clove', 'cobbler/crumble', 'cocktail',
 'cocktail party', 'coconut', 'cod', 'coffee', 'coffee grinder',
 'cognac/armagnac', 'collard greens', 'connecticut', 'cookie',
 'coriander', 'corn', 'cornmeal', 'costa mesa', 'cottage cheese', 'couscous',
 'crab', 'cranberry', 'cranberry sauce', 'cream cheese', 'cuba', 'cucumber',
 'cumin', 'cupcake', 'currant', 'curry', 'custard', 'date', 'dill', 'dip',
 'dorie greenspan', 'double boiler', 'dried fruit', 'drinks', 'duck',
 'eau de vie', 'egg', 'egg nog', 'eggplant', 'endive', 'escarole', 'fennel',
 'feta', 'fig', 'fish', 'flaming hot summer', 'flat bread', 'fontina',
 'frangelico', 'frittata', 'fritter', 'fruit', 'fruit juice', 'fry', 'game',
 'garlic', 'gin', 'ginger', 'goat cheese', 'goose', 'gouda', 'gourmet', 'grains',
 'grand marnier', 'granola', 'grape', 'grapefruit', 'grappa', 'green bean',
 'green onion/scallion', 'grill', 'grill/barbecue', 'ground beef', 'guava',
 'halibut', 'ham', 'hamburger', 'hazelnut', 'herb', 
 'honey', 'honeydew', 'horseradish', 'hot pepper', 'hummus', 'ice cream',
 'iced coffee', 'iced tea', 'jalapeño', 'jam or jelly', 'jícama', 'kahlúa',
 'kale', 'kansas', 'kirsch', 'kiwi', 'kumquat', 'lamb',
 'lancaster', 'las vegas', 'lasagna', 'leafy green', 'leek', 'legume', 'lemon',
 'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lime',
 'lime juice', 'lingonberry', 'liqueur', 'lobster', 'long beach', 'lychee',
 'macadamia nut', 'macaroni and cheese', 'maine', 'mandoline', 'mango',
 'maple syrup', 'margarita', 'marinade', 'marsala', 'marscarpone',
 'marshmallow', 'martini', 'mayonnaise', 'meat', 'meatball', 'meatloaf', 'melon',
 'mezcal', 'midori', 'milk/cream', 'mint', 'molasses', 'monterey jack',
 'mozzarella', 'muffin', 'mushroom', 'mussel', 'mustard', 'mustard greens',
 'nectarine', 'noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus', 'okra',
 'olive', 'omelet', 'onion', 'orange', 'orange juice', 'oregano', 'orzo',
 'oyster', 'pancake', 'papaya', 'paprika', 'parmesan', 'parsley', 'parsnip',
 'passion fruit', 'pasta', 'pastry', 'pea', 'peach', 'peanut', 'peanut butter',
 'pear', 'pecan', 'pepper', 'pernod', 'persimmon', 'phyllo/puff pastry dough',
 'pickles', 'pie', 'pine nut', 'pineapple', 'pistachio', 'pittsburgh', 'pizza',
 'plantain', 'plum', 'pomegranate', 'pomegranate juice', 'poppy', 'pork',
 'pork chop', 'pork rib', 'pork tenderloin', 'port', 'pot pie', 'potato',
 'potato salad', 'poultry', 'poultry sausage', 'prosciutto', 'prune', 'pumpkin',
 'punch', 'quail', 'quiche', 'quince', 'quinoa', 'rabbit', 'rack of lamb',
 'radicchio', 'radish', 'raisin', 'raspberry', 'red wine', 'rhubarb', 'rice',
 'ricotta', 'roast', 'root vegetable', 'rum', 'rutabaga', 'rye', 'saffron',
 'sage', 'sake', 'salad', 'salad dressing', 'salmon', 'salsa', 'sangria',
 'sardine', 'sausage', 'scallop', 'scotch', 'seed', 'semolina', 'sesame',
 'sesame oil', 'shallot', 'shellfish', 'sherry', 'shrimp', 'snapper',
 'sour cream', 'sourdough', 'soy sauce', 'sparkling wine', 'spice', 'spinach',
 'spirit', 'spritzer', 'squash', 'squid', 'steak', 'stew', 'stock', 'strawberry',
 'sugar snap pea', 'sukkot', 'sweet potato/yam', 'swiss cheese', 'swordfish',
 'tamarind', 'tangerine', 'tapioca', 'tarragon', 'tea', 'tequila', 'thyme',
 'tilapia', 'tofu', 'tomatillo', 'tomato', 'tortillas', 'tree nut',
 'tropical fruit', 'trout', 'tuna', 'turnip', 'vanilla', 'veal', 'vegetable',
 'venison', 'vermouth', 'vinegar', 'vodka', 'waffle', 'walnut', 'wasabi',
 'watercress', 'watermelon', 'wheat', 'whiskey', 'whole wheat',
 'wild rice', 'wine', 'wok', 'yogurt', 'yuca', 'zucchini', 'turkey']


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
