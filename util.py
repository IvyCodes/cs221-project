import matplotlib.pyplot as plt
import pandas

ingredients = ['almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot',
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

def get_accuracy(prediction,actual):
	num_correct = 0
	for (x,y) in zip(prediction,actual):
		if y-1 <= x <= y+1:
			num_correct+=1
	# print(str(num_correct) + ' out of ' + str(len(actual)) + ' correct')
	# print('Accuracy = ' + str(num_correct/len(actual)))
	return num_correct/len(actual)

def make_accuracy_plot(prediction,actual):
	plt.plot(actual,prediction, "bo")
	plt.ylim([0,5])
	plt.show()

def write_accuracy_data(prediction, actual, filename):
	results = {'prediction':prediction, 'actual':actual}
	results_csv = pandas.DataFrame(results)

	results_csv.to_csv('./results/' + filename,index = False)


def ingredient_names():
	return ingredients

def ingredient_freq_labels():
	result = []
	for i in ingredients:
		print(i)
		result.append(i + '_freq')
	return result

def has_ingredient_labels():
	result = []
	for i in ingredients:
		result.append('has_' + i)
	return result

def ingredient_length_labels():
	return ['ingredient_lengths']

def direction_length_labels():
	return ['direction_lengths']

def ingredient_labels():
	return ['ingredients']

def direction_labels():
	return ['directions']

def rating_label():
	return ['rating']