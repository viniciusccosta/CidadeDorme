from Jogador 	import Jogador
from random 	import choice

class Cidadao(Jogador):
	def __init__(self, nome = None, saude = 'Vivo', honestidade = 0, analisado = None):
		super().__init__(nome,saude,honestidade, analisado)