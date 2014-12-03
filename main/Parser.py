'''
Created on Dec 2, 2014

@author: alejandro
'''

NOTHING = 0
READING = 1

WORD = 1
PUNCTUATION = 2

def getTokens(str_in):
	tokens = []
	state = 0
	position = 0
	ini_token = 0
	for c in str_in:
		if state == NOTHING:
			if c.isalpha():
				ini_token = position
				state = READING
			elif c == '.' or c == ',':
				tokens.append(lexical_node(c, PUNCTUATION))
		elif state == READING:
			if c == '.' or c == ',':
				tokens.append(lexical_node(str_in[ini_token:position], WORD))
				tokens.append(lexical_node(c, PUNCTUATION))
				state = NOTHING
			elif not c.isalpha():
				tokens.append(lexical_node(str_in[ini_token:position], WORD))
				state = NOTHING
		position += 1
	if state == READING:
		tokens.append(lexical_node(str_in[ini_token:], WORD))
	return tokens


class lexical_node:
	
	def __init__(self, token, kind):
		self.token = token
		self.kind = kind