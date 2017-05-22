from Jogador import Jogador

class Detetive(Jogador):
	def __init__(self, nome = None, saude = 'Vivo', honestidade = 0, analisado = None):
		super().__init__(nome,saude,honestidade, analisado)
		self.jogadoresConhecidos = {} 											# Dicionário[jogador.nome] = objJogador
		
	def arriscar(self,jogadores, tamMaiorNome, perguntas):
		acusados 	= {}
		acertos 	= {}
		terminou 	= False
		
		cnt = 1
		
		# ------------------------------------------------------
		while terminou == False:
			
			print()
			[print('%*s %s' %(tamMaiorNome,jogador.nome,jogador.saude)) for jogador in jogadores.values()]
			print()
			nome 	= input('Escolha alguém para acusar: ')
			nomeKey = nome.lower()
			
			# Detetive não pode perguntar pra alguém que está morto, nem pra alguém que não existe:
			while nomeKey not in jogadores or jogadores[nomeKey].saude == 'Morto':
				print("\n*** OPÇÃO INVÁLIDA ***\n")
				[print('%*s %s' %(tamMaiorNome,jogador.nome,jogador.saude)) for jogador in jogadores.values()]
				print()
				nome 	= input('Escolha alguém para acusar: ')
				nomeKey = nome.lower()
			
			escolha = ''
			while escolha != 'n' and escolha != 's':
				escolha = input('Você está acusando %s de ser assassino, confirmar (s/n)?\nR: ' %(nome)).lower()
			
				if escolha == 's':
					acusados[nomeKey] = jogadores[nomeKey]
					terminou = True
				elif escolha == 'n':
					terminou = False
				else:
					print('\nOpção inválida\n')
			
			if terminou == True:
				escolha = ''
				while escolha != 'n' and escolha != 's':
					escolha = input( 'Adicionar outro na lista de acusados? (s/n)?\nR: ' ).lower()
			
					if escolha == 's':
						terminou = False
					elif escolha == 'n':
						terminou == True
					else:
						print('\nOpção inválida\n')
			
		# ------------------------------------------------------		
		for nomeKey,jogador in acusados.items():
			if jogador.getClass() == 'Assassino':
				acertos[nomeKey] = jogador
			else:
				return (False,jogador) 								# Irá retonar um booleano como FALSO para dizer que o detetive errou e o nome do BOT
			
		return (True, acertos)
				
			
				
			