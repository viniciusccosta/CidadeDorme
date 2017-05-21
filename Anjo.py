from Jogador 	import Jogador
from random 	import choice

class Anjo(Jogador):
	def __init__(self, nome = None, saude = 'Vivo', honestidade = 0, analisado = None):
		super().__init__(nome,saude,honestidade, analisado)
		self.anjos 		= {}									# Dicionário para que os anjos se conheçam
		self.jaSalvo 	= False 								# Cada anjo só pode ser salvo uma única vez
	
	# -------------------------------------------------------------------------------------------------------------------------------------------------------------
	# TODO: Implementar a inteligência de escolher alguém
	def escolherAlguem(self, jogadores, partida):
		return ''
		
		"""
			A inteligência artificial dos anjos será a mesma que a dos assassinos,
			apenas o objetivo que será diferente.
			Tanto os anjos, quantos os assassinos, aprenderão sobre todos os BOTS,
			e tentarão sempre escolher os mais sinceros ou os mais mentirosos,
			(pois mentir sempre ou sempre ser sincero demais facilita pro usuário identificar essas pessoas)
			no caso dos assassinos para tentar matar e no caso do anjos, para tentar salvar.
			
			A grande dificuldade dos anjos é que eles só podem salvar cada anjo uma única vez.
			
			O assassino analisará a melhor escolha através de cálculos proporcionais simples:
				aux1 = verdades / qtdRespostas
				aux2 = mentiras / qtdRespostas
				
				Da melhor escolha para a o pior escolha
				se aux1 == 100%:
					significa que BOT só falou verdade até então
				se aux2 == 100%:
					significa que o BOT só mentiu até então
					
				se aux1 > aux2:
					signfica que o BOT falou mais verdades do que mentiras
				se aux1 < aux2:
					significa que o BOT mentiu mais do que falou verdades
	
				se aux1 == aux2:
					significa que o BOT mentiu a mesma quantidade de vezes que falou a verdade
				
			Caso exista mais do que uma melhor escolha, 
			o assassino escolherá de forma aleátoria entre essas melhores escolhas.
		"""
	# -------------------------------------------------------------------------------------------------------------------------------------------------------------