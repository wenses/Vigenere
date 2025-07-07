import string,os
ll=string.ascii_lowercase
ul=string.ascii_uppercase



def shift_letter(l,p):
	#p=p-2
	global ll
	global ul	
	ld={}
	ud={}

	for i in range(len(ll)):
		try:
			ld.update({ll[i]:ll[(i+p)%len(ll)]})
			ud.update({ul[i]:ul[(i+p)%len(ll)]})
		except:
			pass
	
	if l.islower():
		return ld[l]
	else:
		return ud[l]

def rev_letter(l,p):
	#p=p-2
	
	global ll
	global ul	
	
	ld={}
	ud={}

	for i in range(len(ll)):
		try:
			ld.update({ll[(i+p)%len(ll)]:ll[i]})
			ud.update({ul[(i+p)%len(ul)]:ul[i]})
		except:
			pass
	
	if l.islower():
		return ld[l]
	else:
		return ud[l]

def get_index(l):
	global ll
	global ul

	if l.islower():
		for id, char in enumerate(ll):
			if char==l:
				res=id 

	else:
		for id,char in enumerate(ul):
			if char==l:
				res=id 

	return res


def cipher(text,key):
	es=''
	ki=0

	for i, char in enumerate(text):
		if char.isalpha():
			es+=shift_letter(char,get_index(key[ki%len(key)]))
			ki+=1
		else:
			es+=char

	return es

def decipher(enc,key):
	ds=''

	ki=0

	for i, char in enumerate(enc):
		if char.isalpha():
			ds+=rev_letter(char,get_index(key[ki%len(key)]))
			ki+=1
		else:
			ds+=char

	return ds


def cycle_cipher(text,key,n):
	if n>0:
		return cycle_cipher(cipher(text,key),key,n-1)
	else:
		return cipher(text,key)

def cycle_decipher(enc,key,n):
	if n>0:
		return cycle_decipher(decipher(enc,key),key,n-1)
	else:
		return decipher(enc,key)

print(cycle_cipher('hello','key',1))