from random import choice

class Jogador:
	def __init__(self, nome = None, saude = 'Vivo', honestidade = 0, analisado = None):
		self.nome 			= nome
		self.saude 			= saude						# Vivo ou Morto
		self.honestidade 	= honestidade
		
		if analisado is None:
			self.analisado = dict()
		else:
			self.analisado = analisado
		
		"""
			Honestidade:
				
			-2: sempre mente
			-1: mais mente do que fala a verdade
			 0: as vezes mente, as vezes fala a verdade
			 1: mais fala a verdade do que fala mente
			 2: sempre fala a verdade
			
			para honestidade -2, basta sempre mentir
			para honestidade  0, basta um choice[-2, 2] para decidir se irá falar a verdade ou mentirá naquela rodada
			para honestidade -2, basta sempre falar a verdade
			
			para honestidade -1, basta um choice entre [ 	'mentir1', 	  	 'mentir2', 	  'mentir1', 		'falarVerdade'	] (3/4 de chance)
			para honestidade  1, basta um choice entre [ 	'falarVerdade1', 'falarVerdade2', 'falarVerdade3', 	'mentir'		] (3/4 de chance)
		"""
		
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def responder(self,pergunta):							# Método responsável por responder as perguntas do detetive
		honestidadeAux 	= self.honestidade
		carta 			= self.getClass()
		
		# -------------------------------------------------------------
		# Meio a Meio:
		if honestidadeAux == 0:
			honestidadeAux = choice( [-2,2] )				# O honestidadeAux tem que ser -2 ou 2 agora
		
		# ------------------------------------
		# Mais mente do que fala a verdade:
		elif honestidadeAux == -1:
			aleatorio = choice ( [ 'mentir1', 'mentir2', 'mentir1', 'falarVerdade' ] )
			
			if aleatorio == 'falarVerdade':
				honestidadeAux = 2
			else:
				honestidadeAux = -2
		
		# ------------------------------------	
		# Mais fala a verdade do que mente:
		elif honestidadeAux == 1:
			aleatorio = choice ( [ 'falarVerdade1', 'falarVerdade2', 'falarVerdade3', 'mentir' ] )
			
			if aleatorio == 'mentir':
				honestidadeAux = -2
			else:
				honestidadeAux = 2
				
		# -------------------------------------------------------------
		# Falará a verdade:
		if honestidadeAux == 2:
			if pergunta == carta:
				return 'Sim, eu sou ' 		+ pergunta
			else:
				return 'Não, eu não sou ' 	+ pergunta
		
		# ------------------------------------
		# Mentirá:	
		elif honestidadeAux == -2:
			if pergunta == carta:
				return 'Não, eu não sou ' 	+ pergunta
			else:
				return 'Sim, eu sou ' 		+ pergunta
				
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def analisarRespostas(self, jogadores, jogadoresConhecidos):
		for nomeKey,respostas in jogadoresConhecidos.items():
			verdade = 0
			mentira = 0

			carta 	= jogadores[nomeKey].getClass() 						# Essa é a carta de verdade do BOT
			
			# Verificando cada resposta desse BOT:
			for resposta in respostas:
				respSplit = resposta.replace(',','').split()
				
				afirmacao = respSplit[0] 									# "Sim, ..." ou "Não, ...", queremos saber se ele disse sim ou não !
				pergunta  = respSplit[-1] 									# "... Assassino"	      , queremos saber sobre qual carta ele respondeu
				
				if   afirmacao == 'Sim' and pergunta == carta:
					verdade += 1
				elif afirmacao == 'Não' and pergunta != carta:
					verdade += 1
				else:
					mentira += 1
			
			# Armazenando a análise
			if nomeKey not in self.analisado: 								# Se é a primeira vez que está analisando esse BOT, precisamos criar os dicionários internos
				self.analisado[nomeKey] = {'verdades': 0, 'mentiras': 0}
				
			self.analisado[nomeKey]['verdades'] += verdade
			self.analisado[nomeKey]['mentiras'] += mentira
	
	
	"""
		Em resumo, o que esse método faz é contar quantas vezes os BOTS mentiram e quantas vezes falaram a verdade.
		Essa informação será guardada em um dicionário chamando "analisado", sendo que dentro dele teremos a quantidade de vezes que o BOT
		mentiu e a quantidade de vezes que ele falou a verdade.
		Obviamente, a soma desses dois valores é a quantidade de vezes que o BOT respondeu ao detetive.

		analisado = {nomeBOT1:
								{ 'verdades': x1 ,
								  'mentiras': y1 ,
								},
					 nomeBOT2:
								{ 'verdades': x2 ,
								  'mentiras': y2 ,
								},
					}
							
	"""
	
	def analisarRespostasPorRodada(self, jogadores, nomeKey, resposta):
		# Neste caso respostas terá sempre tamanho 1
		# print('RESP POR RODADA', nomeKey, resposta) 					# DEBUG
		verdade = 0
		mentira = 0

		carta 	= jogadores[nomeKey].getClass() 						# Essa é a carta de verdade do BOT
			
		respSplit = resposta.replace(',','').split()
				
		afirmacao = respSplit[0] 										# "Sim, ..." ou "Não, ...", queremos saber se ele disse sim ou não !
		pergunta  = respSplit[-1] 										# "... Assassino"	      , queremos saber sobre qual carta ele respondeu
				
		if   afirmacao == 'Sim' and pergunta == carta:
			verdade += 1
		elif afirmacao == 'Não' and pergunta != carta:
			verdade += 1
		else:
			mentira += 1
			
		# Armazenando a análise
		if nomeKey not in self.analisado: 								# Se é a primeira vez que está analisando esse BOT, precisamos criar os dicionários internos
			self.analisado[nomeKey] = {'verdades': 0, 'mentiras': 0}
				
		self.analisado[nomeKey]['verdades'] += verdade
		self.analisado[nomeKey]['mentiras'] += mentira
	
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------------	
	def getClass(self):
		classe = self.__class__.__name__
		
		if classe == "Cidadao":
			return "Cidadão"
		else:
			return classe
		
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------------			
	def __repr__(self):
		return self.nome + ' era ' + self.getClass()
	def __str__(self):
		return self.nome + ' era ' + self.getClass()