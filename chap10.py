# Sidd Tewari

z = [1,2,3,4]
a = [[0,1],[1,1],[1,2],[2,2]]
b = [['a','b'],['c','d'],['e','f']]
c = ['a','b','c','D','E','f']
d = [7,8,9]
e = 'spam'
f = 'This is the way the world works my friend. This is just how it is!'
g = 'spam-spam-spam'
h = ['pining', 'for', 'the', 'fjords']
i = 'apple'
j = 'paple'

def add_all(t):
	total = 0
	for x in t:
		total += x
	return total
#--------------------------------
#Exercise 10.1. Write a function called nested_sum that takes a nested list of integers and add up the elements from all of the nested lists.
def add_nests(t):
	total = 0
	for x in t:
		#print x
		for i in x:
			total += i
			#print total
	return total

#--------------------------------
def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

#--------------------------------
# Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new nested list with all strings capitalized.
def capitalize_nests(t):
	res = []
	for x in t:
		res.append(capitalize_all(x))
	return res

#--------------------------------
def only_upper(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
	return res

#--------------------------------
# Exercise 10.3. Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the 
# ith element is the sum of the first i + 1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

def cumulative_add(t):
	res=[]
	sumly = 0
	for i in t:
		sumly += i
		res.append(sumly)
	return res

#--------------------------------
# Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains all 
# but the first and last elements. So middle([1,2,3,4]) should return [2,3].

def middle(t):
	newL = t
	newL.pop(0)
	end = len(newL) - 1
	newL.pop(end)
	return newL

#--------------------------------
# Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.

def chop(t):
	t.pop(0)
	end = len(t) - 1
	t.pop(end)
	# print t
	return

#--------------------------------
def playing(t):
	# s = 'spam'
	t = list(t)
	print t

def playSplit(t):
	s = t.split()
	print s

def delimited(t):
	delimiter = '-'
	s = t.split(delimiter)
	print s 

def merge(t):
	delimiter = ' '
	s = delimiter.join(t)
	return s


#--------------------------------
# Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(t,u):
	x = list(t)
	y = list(u)
	print x
	print y
	for i in x:
		if i not in y:
			return False
	for i in y:
		if i not in x:
			return False
		else:
			return True
#--------------------------------
# print add_all(z)
# print add_nests(a)
# print capitalize_nests(b)
# print only_upper(c)
# print cumulative_add(d)
# print middle(d)
# print chop(d)
# playing(e)
# playSplit(f)
# delimited(g)
# print merge(h)
print is_anagram(i,j)