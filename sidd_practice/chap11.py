def en2sp():
	eng2sp = dict()
	print eng2sp
	eng2sp['one'] = 'uno'
	print 'eng2sp is ', eng2sp
	eng2sp = {'one':'uno', 'two':'dos', 'three':'trois'}
	print 'eng2sp is ', eng2sp
	print eng2sp['two']

def collins():
	sidd = dict()
	sidd ['phone'] = 'iPhone'
	julia = {'phone': 'Droid', 'car' : 'mazda', 'pen' : 'not sarsa'}
	print sidd
	print julia['phone']

# Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesnt matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
def findwords():
	fin = open('words.txt')
	wlist = dict()
	counter = 0
	for line in fin:
		word = line.strip()
		wlist[counter] = word	
		counter += 1
	return wlist	

def histogram(s):
	d = dict()
	for c in s:
		# get (c,0)
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def print_hist(h):
	# for c in h:
	# 	print c, h[c]
	t = []
	t = h.keys()
	t.sort()
	print t

h = histogram('parrot')
print_hist(h)

# a = histogram('abracadabra')
# print 'a is', a
# print histogram('abracadabra')
# print histogram('banana')
# print findwords()
# en2sp()
# collins()