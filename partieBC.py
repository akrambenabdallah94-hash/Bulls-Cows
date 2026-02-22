import random 

def combinaison_secrete():
	T = [0] * 4
	for i in range(4) :
		nb_aleatoire = random.randint(0, 9)
		T[i] = nb_aleatoire

	return T


def conversion_saisie(chn):
	T = []
	chn_propre = chn.replace(" ","")

	if len(chn_propre) != 4:
		print("Saisir un code de 4 chiffe")
		return []
		
	for caractere in chn: 
		if caractere.isdigit():
			T.append(int(caractere))
	
	return T

def histo(configuartion):

	h = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for x in configuartion:
		h[x] += 1

	return h		

def nombre_communs(config1, config2):
	h1 = histo(config1)
	h2 = histo(config2)

	communs = 0
	for i in range(10):
		communs += min(h1[i], h2[i])

	return communs

def nombre_bulls_cows(config1, config2):
	bulls = 0
	cows = 0

	for i in range(len(config1)):
		if config1[i] == config2[i]:
			bulls += 1

	h1 = histo(config1)
	h2 = histo(config2)

	communs = 0
	for i in range(10):
		communs += min(h1[i], h2[i])
	
	cows = communs - bulls

	return bulls, cows


def partie_joueur_humain(nbmax_essai):
	chn = input("Propostion sous la forme '1234' : ")
	prop = conversion_saisie(chn)
	essai = 0
	secret = combinaison_secrete()
	bulls, cows = nombre_bulls_cows(prop, secret)
	
	
	while prop != secret:
		essai += 1

		if essai == nbmax_essai:
			print(f"Vous avez perdu !!! le nombre secret était {secret}")
			break

		print(f"essai={essai}, bulls={bulls}, cows={cows}")
		print("---------------------------------------\n")
		chn = input("Propostion sous la forme '1234' : ")
		prop = conversion_saisie(chn)
		bulls, cows = nombre_bulls_cows(prop, secret)


	if prop == secret:
			print(f"Vous avez réussi après {essai} essai")
		
 		
	


	