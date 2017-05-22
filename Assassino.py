from Jogador 	import Jogador
from random 	import choice

class Assassino(Jogador):
	def __init__(self, nome = None, saude = 'Vivo', honestidade = 0, analisado = None):
		super().__init__(nome,saude,honestidade,analisado)
		self.assassinos = {}									# Dicionário para que os assassinos se conheçam
	
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------------	
	def escolherAlguem(self, jogadores, partida):
		# ---------------------------------------------------------------------------------------------------------
		if self.analisado is not None and (partida > 1): 		 	# Não é possível escolher alguém se nunca jogamos, e não existe inteligência na primeira partida!
			escolhas 			= {}
			melhoresEscolhas 	= {}
			
			# -------------------------------------------------
			# Calculando porcentagens:
			for nomeKey, analise in self.analisado.items():
				jogador = jogadores[nomeKey]
				
				if jogador.getClass() != 'Assassino' and jogador.saude == 'Vivo':	# Assassino não comete suicídio e nem mata alguém que já está morto
					aux1 = analise['verdades'] / len(analise)
					aux2 = analise['mentiras'] / len(analise)
				
					escolhas[nomeKey] = (aux1,aux2)
			
			# ---------------------------------------------------------------------------
			# Existe escolha?
			
			if len(escolhas) > 0:
				# ---------------------------------------------
				# Classificando as escolhas:
				for nomeKey, (aux1,aux2) in escolhas.items():
					jogador = jogadores[nomeKey]
					
					if   aux1 == 1:
						melhoresEscolhas[nomeKey] 	= (aux1,aux2) 	# Significa que BOT só falou verdade até então, logo ele é uma ótima escolha para os assassinos matarem
						
					elif aux2 == 1:
						melhoresEscolhas[nomeKey] 	= (aux1,aux2) 	# Significa que o BOT só mentiu até então, logo ele é uma ótima escolha para os assassinos matarem
				
				# ---------------------------------------------	
				# Se não tivemos uma melhor escolha, faremos que ter uma melhor escolha:
				if len(melhoresEscolhas) == 0:
					maxValue 		= sorted(  max   (  escolhas.values(), key = lambda v: sorted(v,           reverse=True)                        ), reverse = True )
					nomes 			= list  (  filter(                           lambda k: sorted(escolhas[k], reverse=True) == maxValue, escolhas  )                 )
					
					for nomeKey in nomes:						
						melhoresEscolhas[nomeKey] = escolhas[nomeKey] 					# Tanto faz o value, o importante será o nomeKey
					
				# ---------------------------------------------
				# Melhor escolha:
				melhoresEscolhas = list( melhoresEscolhas.keys() )							# Se só tem uma, vai retorna ela, senão,...
				melhorEscolha 	 = choice( melhoresEscolhas )								# ... vai retornar de forma aleatória uma das melhores escolhas
				
				return melhorEscolha
				
			# ---------------------------------------------------------------------------
			# Se o usuário só perguntou sobre assassinos e pessoas que estão mortas, dicionário 'escolha' será vazio, logo, temos que escolher aleatoriamente:
			else:
				# Retorna algum valor aleatório:
				vivos = {}
				for nomeKey, jogador in jogadores.items():
					if jogador.saude == 'Vivo' and jogador.getClass() != 'Assassino': 		# Assassino não comete suicídio e nem mata alguém que já está morto
						vivos[nomeKey] = jogador											# Tanto faz o value, o importante será o nomeKey
				
				nomeVivos 		= list  ( vivos.keys() )
				jogador 		= jogadores[ choice( nomeVivos ) ] 							# Seleciona algum BOT que ainda esteja vivo
				
				return jogador.nome.lower()
				
		# ---------------------------------------------------------------------------------------------------------
		# Se é a primeira rodada, vai no aleatório:
		else:
			# Retorna algum valor aleatório:
			vivos = {}
			for nomeKey, jogador in jogadores.items():
				if jogador.saude == 'Vivo' and jogador.getClass() != 'Assassino': 		# Assassino não comete suicídio e nem mata alguém que já está morto
					vivos[nomeKey] = jogador											# Tanto faz o value, o importante será o nomeKey
			
			nomeVivos 		= list  ( vivos.keys() )
			jogador 		= jogadores[ choice( nomeVivos ) ] 							# Seleciona algum BOT que ainda esteja vivo
			
			return jogador.nome.lower()
			
												
		# ---------------------------------------------------------------------------------------------------------
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
	
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
