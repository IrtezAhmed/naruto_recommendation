import random
import time

A = ['male', 'strong', 'hokage']
B = ['male', 'strong', 'sage']
C = ['male', 'weak', 'animal']
D = ['pet', 'weak', 'animal']
E = ['male', 'weak', 'animal']
F = ['female', 'weak', 'kunoichi']
G = ['female', 'strong', 'kunoichi']
H = ['male', 'strong', 'sage']
I = ['male', 'strong', 'sage']
J = ['female', 'strong', 'sage']
K = ['male', 'strong', 'animal']
L = ['male', 'strong', 'uchiha']
M = ['male', 'strong', 'uchiha']
N = ['pet', 'weak', 'animal']
O = ['female', 'weak', 'kunoichi']
P = ['male', 'strong', 'hokage']
Q = ['male', 'strong', 'hokage']



dictionary = {'Naruto': A, 'Sasuke': B, "Kiba": C, "Akamaru": D, 'Shino': E, 'Ino': F, 
"Hinata": G, "Mitsuki": H, "Jiraiya": I, "Tsunade": J, "Orochimaru": K, "Madara": L, 
"Itachi": M, "Gamatatsu": N, "Kurenai": O, "Hiruzen": P, "Tobirama": Q}

dictionary2 = {'Naruto': A, 'Sasuke': B, "Kiba": C, "Akamaru": D, 'Shino': E, 'Ino': F, 
"Hinata": G, "Mitsuki": H, "Jiraiya": I, "Tsunade": J, "Orochimaru": K, "Madara": L, 
"Itachi": M, "Gamatatsu": N, "Kurenai": O, "Hiruzen": P, "Tobirama": Q}

gender = set() #creates empty set for each major characteristic
strength = set()
quality = set()

for values in dictionary.values(): #adds characteristics from dictionary to set
		gender.add(values[0])
		strength.add(values[1])
		quality.add(values[2])

gender = list(gender) #converts sets to lists so they are iterable
strength = list(strength)
quality = list(quality)

attr_male = 0 #creates attributes to be ranked in competitive section
attr_female = 0
attr_pet = 0
attr_strong = 0
attr_weak = 0
attr_sage = 0
attr_hokage = 0
attr_kunoichi = 0
attr_animal = 0

male_list = []
female_list = []
pet_list = []
strong_list = []
weak_list = []
sage_list = []
hokage_list = []
kunoichi_list = []
animal_list = []


'''Next Phase: Gender'''

for name in dictionary:
	if 'male' in dictionary[name]:
		male_list.append(name)
	if 'female' in dictionary[name]:
		female_list.append(name)
	if 'pet'  in dictionary[name]:
		pet_list.append(name)

male1 = random.choice(male_list)
male2 = random.choice(male_list)
while male1 == male2:
	male2 = random.choice(male_list)

female1 = random.choice(female_list)
female2 = random.choice(female_list)
while female2 == female1:
	female2 = random.choice(female_list)

pet1 = random.choice(pet_list)
pet2 = random.choice(pet_list)
while pet2 == pet1:
	pet2 = random.choice(pet_list)


print(male1, female1, sep='     VS     ')
response1 = ""
while (response1 != male1) and (response1 != female1):
	response1 = input('Type the one you prefer: \n')
	if response1 == male1:
		attr_male += 1
		print('Great!')
		time.sleep(1)
	elif response1 == female1:
		attr_female += 1
		print('Great!')
		time.sleep(1)
	else:
		print('That is not an option.')


response2 = ''
print(female2, pet1, sep='     VS     ')

while (response2 != female2) and (response2 != pet1):
	response2 = input('Type the one you prefer: \n')
	if response2 == female2:
		attr_female += 1
		print('Great!')
		time.sleep(1)
	elif response2 == pet1:
		attr_pet += 1
		print('Great!')
		time.sleep(1)
	else:
		print('That is not an option.')
			
response3 = ''
print(male2, pet2, sep='     VS     ')
while (response3 != male2) and (response3 != pet2):
	response3 = input('Type the one you prefer: \n')
	if response3 == male2:
		attr_male += 1
		print('Great!')
		time.sleep(1)
	elif response3 == pet2:
		attr_pet += 1
		print('Great!')
		time.sleep(1)
	else:
		print('That is not an option.')
					


def remove_male():
	'''removes all items from dictionary that contain the 'male' attribute'''
	for items in list(dictionary2):
			if ('female' in dictionary2[items]) or ('pet' in dictionary2[items]):
				 dictionary2.pop(items, None)

def remove_female():
	'''removes all items from dictionary that contain the 'female' attribute'''
	for items in list(dictionary2):
		if ('male' in dictionary2[items]) or ('pet' in dictionary2[items]):
			dictionary2.pop(items, None)

def remove_pet():
	'''removes all items from dictionary that contain the 'pet' attribute'''
	for items in list(dictionary2):
		if ('female' in dictionary2[items]) or ('male' in dictionary2[items]):
			dictionary2.pop(items, None)

if (attr_male > attr_pet) and (attr_male > attr_female):
	remove_male()
elif (attr_female > attr_male) and (attr_female > attr_pet):
	remove_female()
elif (attr_pet > attr_male) and (attr_pet > attr_female):
	remove_pet()
print('Items remaining', dictionary2)
'''Next Phase: Strength'''

(strong1, weak1, strong2, weak2) = (0, 0, 0, 0) #must pre-define if weak/strong_list only has one item.

for names in dictionary2:
	if 'strong' in dictionary2[names]:
		strong_list.append(names)
	if 'weak' in dictionary2[names]:
		weak_list.append(names)

if len(strong_list) > 1:
	strong1 = random.choice(strong_list) 
	strong2 = random.choice(strong_list)
	while strong2 == strong1:
		strong2 = random.choice(strong_list)
elif len(strong_list) == 1:
	strong1 = strong_list[0]

if len(weak_list) > 1:
	weak1 = random.choice(weak_list)
	weak2 = random.choice(weak_list)
	while weak2 == weak1:
		weak2 = random.choice(weak_list)
elif len(weak_list) == 1:
	weak1 = weak_list[0]

if (weak1 != 0) and (strong1 != 0):

	print(weak1, strong1, sep='     VS     ')
	
	response4 = ''
	
	while (response4 != weak1) and (response4 != strong1): ###
		response4 = input('Type the one you prefer: \n')
		if response4 == weak1:
			attr_weak += 1
			print('Great!')
			time.sleep(1)
		elif response4 == strong1:
			attr_strong += 1
			print('Great!')
			time.sleep(1)
		else:
			print('That is not an option.')
elif (weak1 == 0) and (strong1 != 0):
	attr_strong += 1
elif (weak1 != 0) and (strong1 == 0):
	attr_weak += 1

	
if (weak2 != 0) and (strong2 != 0): 
	print(weak2, strong2, sep='     VS     ')
	
	response5 = ''
	
	while (response5 != weak2) and (response5 != strong2):  ### # ##
		response5 = input('Type the one you prefer: \n')
		if response5 == weak2:
			attr_weak += 1
			print('Great!')
			time.sleep(1)
		elif response5 == strong2:
			attr_strong += 1
			print('Great!')
			time.sleep(1)
		else:
			print('That is not an option.')
elif (weak2 == 0) and (strong2 != 0):
	attr_strong += 1
elif (weak2 != 0) and (strong2 == 0):
	attr_weak += 1



def remove_strong():
	'''removes all items from dictionary that contain the 'male' attribute'''
	for items in list(dictionary2):
		if ('weak') in dictionary2[items]:
			dictionary2.pop(items, None)

def remove_weak():
	'''removes all items from dictionary that contain the 'female' attribute'''
	for items in list(dictionary2):
		if ('strong') in dictionary2[items]:
			dictionary2.pop(items, None)	

if attr_strong > attr_weak:
	remove_strong()
else:
	remove_weak()
print('Items remaining', dictionary2)

'''Next Phase: Quality '''

for items in dictionary2:
	if 'sage' in dictionary2[items]:
		sage_list.append(items)
	if 'hokage' in dictionary2[items]:
		hokage_list.append(items)
	if 'kunoichi' in dictionary2[items]:
		kunoichi_list.append(items)
	if 'animal' in dictionary2[items]:
		animal_list.append(items)

if len(sage_list) > 1:
	sage1 = random.choice(sage_list)
	sage2 = random.choice(sage_list)
	while sage2 == sage1:
		sage2 = random.choice(sage_list)
elif len(sage_list) == 1:
	(sage1, sage2) = (sage_list[0], 0)
elif len(sage_list) == 0:
	(sage1, sage2) = (0, 0)

if len(hokage_list) > 1:		
	hokage1 = random.choice(hokage_list)
	hokage2 = random.choice(hokage_list)
	while hokage2 == hokage1:
		hokage2 = random.choice(hokage_list)
elif len(hokage_list) == 1:
	(hokage1, hokage2) = (hokage_list[0], 0)
elif len(hokage_list) == 0:
	(hokage1, hokage2) = (0,0)

if len(kunoichi_list) > 1:
	kunoichi1 = random.choice(kunoichi_list)
	kunoichi2 = random.choice(kunoichi_list)
	while kunoichi2 == kunoichi1:
		kunoichi2 = random.choice(kunoichi_list)
elif len(kunoichi_list) == 1:
	kunoichi1, kunoichi2 = kunoichi_list[0], 0
elif len(kunoichi_list) == 0:
	kunoichi1, kunoichi2 = 0, 0

if len(animal_list) > 1:
	animal1 = random.choice(animal_list)
	animal2 = random.choice(animal_list)
	while animal2 == animal1:
		animal2 = random.choice(animal_list)
elif len(animal_list) == 1:
	animal1, animal2 = animal_list[0], 0
elif len(animal_list) == 0:
	animal1, animal2 = 0, 0

if (sage1 != 0) and (kunoichi1 != 0):
# sage, kunoichi, hokage, animal
	print(sage1, kunoichi1, sep='     VS     ')
	
	response6 = ''
	
	while (response6 !=sage1) and (response6!=kunoichi1):
		response6 = input('Type the one you prefer: \n')
		if response6 == sage1:
			attr_sage += 1
			print('Great!')
			time.sleep(1)
		elif response6 == kunoichi1:
			attr_kunoichi += 1
			print('Great!')
			time.sleep(1)
		else:
			print('That is not an option.')
elif (sage1==0) and (kunoichi1!=0):
	attr_kunoichi+=1
elif (sage1!=0) and (kunoichi1==0):
	attr_sage+=1
				
	
if (hokage1!=0) and (animal1!=0):
	print(hokage1, animal1, sep='     VS     ')

	response7 = ''

	while (response7 != hokage1) and (response7!=animal1): 
		response7 = input('Type the one you prefer: \n')
		if response7 == hokage1:
			attr_hokage += 1
			print('Great!')
			time.sleep(1)
		elif response7 == animal1:
			attr_animal += 1
			print('Great!')
			time.sleep(1)
		else:
			print('That is not an option.')
elif (hokage1==0) and (animal1!=0):
	attr_animal+=1
elif (hokage1!=0) and (animal1==0):
	attr_hokage+=1

if (sage2 !=0) and (kunoichi2!=0):
	print(sage2, kunoichi2, sep='     VS     ')

	response8 = ''

	while (response8 !=sage2) and (response8!=kunoichi2):
		response8 = input('Type the one you prefer: \n')
		if response8 == sage2:
			attr_sage += 1
			print('Great!')
			time.sleep(1)
		elif response8 == kunoichi2:
			attr_kunoichi += 1
			print('Great!')
			time.sleep(1)
		else:
			print('That is not an option.')
elif (sage2==0) and (kunoichi2!=0):
	attr_kunoichi+=1
elif (sage2!=0) and (kunoichi2==0):
	attr_sage+=1

if (hokage2!=0) and (animal2!=0):
	print(hokage2, animal2, sep='     VS     ')
	
	response9 = ''
	
	while (response9 != hokage2) and (response9!=animal2):
		respons9 = input('Type the one you prefer: \n')
		if response9 == hokage2:
			attr_hokage += 1
			print('Great!')
			time.sleep(1)
		elif response9 == animal2:
			attr_animal += 1
			print('Great!')
			time.sleep(1)
		else:
			print('That is not an option.')
elif (hokage2==0) and (animal2!=0):
	attr_animal+=1
elif (hokage2!=0) and (animal2==0):
	attr_hokage+=1		



def remove_kunoichi():
	'''removes all items from dictionary that contain the ('hokage' or 'sage' or 'animal') attribute''' 
	for items in list(dictionary2):
			if ('hokage' in dictionary2[items]) or ('sage' in dictionary2[items])  or ('animal' in dictionary2[items]):
				 dictionary2.pop(items, None)

def remove_hokage():
	'''removes all items from dictionary that contain the ('kunoichi' or 'sage' or 'animal') attribute'''
	for items in list(dictionary2):
			if ('kunoichi' in dictionary2[items]) or ('sage' in dictionary2[items])  or ('animal' in dictionary2[items]):
				 dictionary2.pop(items, None)	

def remove_sage():
	'''removes all items from dictionary that contain the ('hokage' or 'kunoichi' or 'animal') attribute'''
	for items in list(dictionary2):
			if ('hokage' in dictionary2[items]) or ('kunoichi' in dictionary2[items])  or ('animal' in dictionary2[items]):
				 dictionary2.pop(items, None)

def remove_animal():
	'''removes all items from dictionary that contain the ('sage' or 'kunoichi' or 'hokage') attribute'''
	for items in list(dictionary2):
			if ('hokage' in dictionary2[items]) or ('sage' in dictionary2[items])  or ('kunoichi' in dictionary2[items]):
				 dictionary2.pop(items, None)	


if (attr_kunoichi >= attr_sage) and (attr_kunoichi >= attr_hokage) and (attr_kunoichi >= attr_animal):
	remove_kunoichi()
elif (attr_sage >= attr_kunoichi) and (attr_sage >= attr_animal) and (attr_sage >= attr_hokage):
	remove_sage()
elif (attr_hokage >= attr_sage) and (attr_hokage >= attr_animal) and (attr_hokage >= attr_kunoichi):
	remove_hokage()
elif (attr_animal >= attr_sage) and (attr_animal >= attr_hokage) and (attr_animal >= attr_kunoichi):
	remove_animal()

print(attr_animal, attr_hokage, attr_kunoichi, attr_sage)

print("The following Ninja are probably your favourite:")

for items in dictionary2:
	print(items)
######PROBLEM: Return is not excluding some attributes


