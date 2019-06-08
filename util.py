import matplotlib.pyplot as plt
import pandas

ingredients = ['almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot',
	 'artichoke', 'arugula', 'asparagus', 'avocado', 'bacon', 'bake',
	 'banana', 'barley', 'basil', 'bass', 'bean', 'beef', 'rib', 'shank',
	 'tenderloin', 'beer', 'beet', 'bell', 'berr', 'biscuit', 'bitter',
	 'blackberry', 'blender', 'blue', 'blueberr', 'bok','choy', 'bourbon',
	 'braise', 'bran', 'brandy', 'bread', 'breadcrumb', 'brie', 'brine', 'brisket',
	 'broccoli', 'brown', 'brownie', 'brussel sprout',
	 'buffalo', 'bulgur', 'butter', 'buttermilk', 'butternut',
	 'butterscotch', 'cabbage', 'cake', 'calvados', 'campari', 'candy', 'cantaloupe',
	 'caper', 'caraway', 'cardamom', 'carrot', 'cashew', 'casserole',
	 'cauliflower', 'caviar', 'celery', 'chambord', 'champagne', 'chard',
	 'chartreuse', 'cheddar', 'cheese', 'cherry', 'chestnut', 'chicago', 'chicken',
	 'chickpea', 'chile', 'chile pepper', 'chili', 'chive', 'chocolate', 'cilantro',
	 'cinnamon', 'citrus', 'clam', 'clove', 'cobbler','crumble', 'cocktail',
	 'party', 'coconut', 'cod', 'coffee', 'grinder',
	 'cognac', 'collard', 'connecticut', 'cookie',
	 'coriander', 'corn', 'cornmeal', 'costa', 'cottage', 'couscous',
	 'crab', 'cranberry', 'cream', 'cuba', 'cucumber',
	 'cumin', 'cupcake', 'currant', 'curry', 'custard', 'date', 'dill', 'dip',
	 'greenspan', 'double', 'dried', 'drink', 'duck',
	 'eau', 'egg', 'nog', 'eggplant', 'endive', 'escarole', 'fennel',
	 'feta', 'fig', 'fish', 'flat bread', 'fontina',
	 'frangelico', 'frittata', 'fritter', 'fruit', 'juice', 'fry', 'game',
	 'garlic', 'gin', 'ginger', 'goat', 'goose', 'gouda', 'gourmet', 'grain',
	 'marnier', 'grand', 'granola', 'grape', 'grapefruit', 'grappa', 'green', 'grill', 'grill/barbecue', 'ground beef', 'guava',
	 'halibut', 'ham', 'hamburger', 'hazelnut', 'herb', 
	 'honey', 'honeydew', 'horseradish', 'hot', 'hummus', 'ice', 'jalapeño', 'jam', 'jelly', 'jícama', 'kahlúa',
	 'kale', 'kirsch', 'kiwi', 'kumquat', 'lamb',
	 'lancaster', 'lasagna', 'leafy', 'leek', 'legume', 'lemon', 'lemongrass', 'lentil', 'lettuce', 'lima', 'lime',
	 'lingonberry', 'liqueur', 'lobster', 'lychee',
	 'macadamia', 'macaroni', 'maine', 'mandoline', 'mango',
	 'maple', 'margarita', 'marinade', 'marsala', 'marscarpone',
	 'marshmallow', 'martini', 'mayonnaise', 'meat', 'meatball', 'meatloaf', 'melon',
	 'mezcal', 'midori', 'milk', 'mint', 'molasses', 'monterey', 'jack',
	 'mozzarella', 'muffin', 'mushroom', 'mussel', 'mustard',
	 'nectarine', 'noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus', 'okra',
	 'olive', 'oil','omelet', 'onion', 'orange', 'oregano', 'orzo',
	 'oyster', 'pancake', 'papaya', 'paprika', 'parmesan', 'parsley', 'parsnip',
	 'passion', 'pasta', 'pastry', 'pea', 'peach', 'peanut',
	 'pear', 'pecan', 'pepper', 'pernod', 'persimmon', 'phyllo', 'dough', 'puff',
	 'pickle', 'pie', 'pine', 'pineapple', 'pistachio', 'pittsburgh', 'pizza',
	 'plantain', 'plum', 'pomegranate', 'poppy', 'pork', 'port', 'pot', 'potato',
	 'poultry', 'prosciutto', 'prune', 'pumpkin',
	 'punch', 'quail', 'quiche', 'quince', 'quinoa', 'rabbit', 'rack',
	 'radicchio', 'radish', 'raisin', 'raspberr', 'red wine', 'rhubarb', 'rice',
	 'ricotta', 'roast', 'root', 'rum', 'rutabaga', 'rye', 'saffron',
	 'sage', 'sake', 'salad', 'dressing', 'salmon', 'salsa', 'sangria',
	 'sardine', 'sausage', 'scallop', 'scotch', 'seed', 'semolina', 'sesame', 'salt',
	 'shallot', 'shellfish', 'sherry', 'shrimp', 'snapper',
	 'sour', 'sourdough', 'soy', 'sparkling', 'spice', 'spinach',
	 'spirit', 'spritzer', 'squash', 'squid', 'steak', 'stew', 'stock', 'strawberr',
	 'snap', 'sugar', 'sukkot', 'yam', 'sweet', 'swiss', 'swordfish',
	 'tamarind', 'tangerine', 'tapioca', 'tarragon', 'tea', 'tequila', 'thyme',
	 'tilapia', 'tofu', 'tomatillo', 'tomato', 'tortilla', 'tree',
	 'tropical', 'trout', 'tuna', 'turnip', 'vanilla', 'veal', 'vegetable',
	 'venison', 'vermouth', 'vinegar', 'vodka', 'waffle', 'walnut', 'wasabi',
	 'watercress', 'watermelon','water', 'wheat', 'whiskey', 'whole',
	 'wild', 'wine', 'wok', 'yogurt', 'yuca', 'zucchini', 'turkey', 'baguette']

def get_accuracy(prediction,actual):
	num_correct = 0
	for (x,y) in zip(prediction,actual):
		if y-1 <= x <= y+1:
			num_correct+=1
	print(str(num_correct) + ' out of ' + str(len(actual)) + ' correct')
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