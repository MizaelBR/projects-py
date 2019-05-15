## Python ######################
## PokedeX Api - Web Scraping ##

import requests
import json

# FUNÇÃO
def pokeInfo():
	try:
		page = requests.get('https://pokeapi.co/api/v2/pokemon/')
		doc = json.loads(page.text)
		return doc['count']
	except:
		return '[ ERRO ]'
def pokemon(numero):

	try:
		d = dict()
		NUMX = 9198

		if int(numero) >= 803:
			for i in range(803,950):
				d[i] = i + NUMX
			numero = d[int(numero)]

		page = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(numero)).text
		page = json.loads(page)

		nome = page['name']

		tipo = list()
		for i in page['types']:
			tipo.append(i['type']['name'])

		return [nome, tipo]
	except:
		return [' ---- ', [' ERRO ']]

# PROGRAMA
boo = True
while boo:
	# DADOS SOBRE O PROGRAMA
	print('{0}-- POKEDEX --{0}'.format(' '*12))
	print(' - Digite um numero para ver um pokemon!\n - Temos: {0} Pokemons na Pokedex.\n{1}'
		.format(pokeInfo(), '-'*45))

	# INPUT
	z = input(' > Digite um numero: ')
	print('-'*45)
	poke = pokemon(z)

	# OUTPUT
	print(' -- Nome:  {}'.format( poke[0].upper() ))
	print(' -- Tipo:', end='')
	for i in poke[1]:
		print('|', i.upper(), end=' ')
	print('|')  # Enfeite :P
	
	loop = True
	while loop:
		print('-'*45)
		tente = input('Continuar? [S ou N]: ')
		if tente.upper() == 'N':
			print('='*45)
			boo = False
			loop = False
		elif tente.upper() == 'S':
			print('-'*45)
			loop = False
		else:
			print('[ S - SIM ] ou [ N - NAO]')


