"""
CS 221: recipes2vec Team
Implementation Based on word2vec by Derek Chia's Towards Data Science post: "An implementation guide to Word2Vec using NumPy"
"""

import csv
import random
import numpy as np
from   collections import defaultdict
import util
import pickle

class word2vec():

	def __init__(self):
		self.n = settings['n']
		self.lr = settings['learning_rate']
		self.epochs = settings['epochs']
		self.window = settings['window_size']

	def generate_training_data(self, settings, corpus):

		# Build up unique Word Dict
		word_counts = defaultdict(int)
		for row in corpus:
			for word in row:
				word_counts[word] += 1

		# Unique word count 
		self.v_count = len(word_counts.keys())

		# Generate Lookup Dictionaries
		self.words_list = list(word_counts.keys())
		self.word_index = dict((word, i) for i, word in enumerate(self.words_list))
		self.index_word = dict((i, word) for i, word in enumerate(self.words_list))
							
		# training_data will be populated with one-hot representations of words																				
		training_data = []

		# Cycle through each sentence in corpus
		for sentence in corpus:
			sent_len = len(sentence)

			# Cycle through each word in sentence
			for i, word in enumerate(sentence):
				# Convert target word to one-hot
				w_target = self.word2onehot(sentence[i])

				# Cycle through context window
				w_context = []

				# Note: window_size 2 will have range of 5 values
				for j in range(i - self.window, i + self.window+1):
					if j != i and j <= sent_len-1 and j >= 0:
						# Append the one-hot representation of word to w_context
						w_context.append(self.word2onehot(sentence[j]))																							
				training_data.append([w_target, w_context])

		return np.array(training_data)

	def word2onehot(self, word):
		# word_vec - initialise a blank vector
		word_vec = [0 for i in range(0, self.v_count)] # Alternative - np.zeros(self.v_count)

		# Get ID of word from word_index
		word_index = self.word_index[word]

		# Change value from 0 to 1 according to ID of the word
		word_vec[word_index] = 1

		return word_vec

	def train(self, training_data):
		# Randomly initializing weight matrices:

		self.w1 = np.random.uniform(-1, 1, (self.v_count, self.n))
		self.w2 = np.random.uniform(-1, 1, (self.n, self.v_count))
		
		# Cycle through each epoch
		for i in range(self.epochs):
			# Intialise loss to 0
			self.loss = 0
			# Cycle through each training sample
			# w_t = vector for target word, w_c = vectors for context words
			for w_t, w_c in training_data:
				# Forward pass
				# 1. predicted y using softmax (y_pred) 2. matrix of hidden layer (h) 3. output layer before softmax (u)
				y_pred, h, u = self.forward_pass(w_t)

				EI = np.sum([np.subtract(y_pred, word) for word in w_c], axis=0)

				# Backpropagation
				# Using Stochastic Gradient Descent to Backprop errors
				self.backprop(EI, h, w_t)

				# LOSS = Sum of all outputs + len(context words) * log of sum for all elems in output layer (previous to softmax)
				self.loss += -np.sum([u[word.index(1)] for word in w_c]) + len(w_c) * np.log(np.sum(np.exp(u)))
				
			print('Epoch:', i, "Loss:", self.loss)

	def forward_pass(self, x):
		# x is one-hot vector for target word, shape - (Embedding Dim x 1)
		# Run through first matrix (w1) to get hidden layer - (Vocab Size x Embedding Dim) dot (Embedding Dim x 1) = (Vocab Size x 1)
		h = np.dot(x, self.w1)
		# Dot product hidden layer with second matrix (w2) - (Embedding Dim x Vocab Size) dot (Vocab Size x 1) = (Embedding Dim x 1)
		u = np.dot(h, self.w2)
		# Run 1 x Embedding Dim through softmax to force each element to range of [0, 1]
		y_c = self.softmax(u)
		return y_c, h, u

	def softmax(self, x):
		e_x = np.exp(x - np.max(x))
		return e_x / e_x.sum(axis=0)

	def backprop(self, e, h, x):

		dl_dw2 = np.outer(h, e)
		dl_dw1 = np.outer(x, np.dot(self.w2, e.T))

		# Update weights
		self.w1 = self.w1 - (self.lr * dl_dw1)
		self.w2 = self.w2 - (self.lr * dl_dw2)

	# Get vector from word
	def word_vec(self, word):
		w_index = self.word_index[word]
		v_w = self.w1[w_index]
		return v_w

	# Input vector, returns nearest word(s)
	def vec_sim(self, word, top_n):
		v_w1 = self.word_vec(word)
		word_sim = {}

		for i in range(self.v_count):
			# Find the similary score for each word in vocab
			v_w2 = self.w1[i]
			theta_sum = np.dot(v_w1, v_w2)
			theta_den = np.linalg.norm(v_w1) * np.linalg.norm(v_w2)
			theta = theta_sum / theta_den

			word = self.index_word[i]
			word_sim[word] = theta

		words_sorted = sorted(word_sim.items(), key=lambda kv: kv[1], reverse=True)

		for word, sim in words_sorted[:top_n]:
			print(word, sim)

# -------------------------------------------------------------------------------------------------
# Run recipes2vec.py

# "recipescorpus.txt" should contain all recipees ingredients consecutively
# recipescorpus = open("recipescorpus.txt", "r")

# if (recipescorpus.mode == 'r'):
#     corpusText = recipescorpus.read()

# recipescorpus.close()

corpus = [util.ingredient_names()]

# Get Size of Word Embedding
ingredientDict = defaultdict(int)
for row in corpus:
	for word in row:
		ingredientDict[word] += 1
embed_size = len(ingredientDict.keys())

settings = {
	'window_size': 2,		# context window size
	'n': embed_size,		# dimensions of word embeddings
	'epochs': 50,			# number of training epochs
	'learning_rate': 0.01	# learning rate
}

# Initialise object
w2v = word2vec()

# Numpy ndarray with one-hot representation for [target_word, context_words]
training_data = w2v.generate_training_data(settings, corpus)

# Training
w2v.train(training_data)

# print("Weights:")
# print (w2v.w1)
# print (w2v.w2)
# print("Weights:")

# Saving Ingredient Embeddings
embeddings = {}
for key,val in ingredientDict.items():
	vec = w2v.word_vec(key)
	embeddings[key] = vec
	print(len(vec))

outfile = open('ingredient_embeddings.pickle', 'wb')
pickle.dump(embeddings, outfile)
outfile.close()
# with open('ingredientEmbeddings.csv', mode='w') as ing_emb:
# 	writer = csv.writer(ing_emb, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 	for key, val in ingredientDict.items():
# 		vec = w2v.word_vec(key)

# 		embedded = {key: vec}
# 		print(embedded)
# 		writer.writerow(embedded.items())
# ing_emb.close()
