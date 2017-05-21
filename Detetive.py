from Jogador import Jogador

class Detetive(Jogador):
	def __init__(self, nome = None, saude = 'Vivo', honestidade = 0, analisado = None):
		super().__init__(nome,saude,honestidade, analisado)
		self.jogadoresConhecidos = {} 											# Dicionário[jogador.nome] = objJogador
		
	def arriscar(self,jogadores, partida):
		pass