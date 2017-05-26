#!/usr/bin/python
#coding=utf8

# -----------------------------------------------------------------------------------------------------------------------------------------------------
from Assassino	import	Assassino
from Anjo		import	Anjo
from Detetive	import	Detetive
from Cidadao	import	Cidadao
from Jogador	import	Jogador

from random		import	choice

from sys		import	platform

import os

# ----------------------------------------------------------------------------------------------------------------------------------------------------
if platform == "win32" or platform == 'cygwin':
	limpar = 'cls'
else:
	limpar = 'clear'

"""
.---------------------.----------.
| System              | Value    |
|---------------------|----------|
| Linux (2.x and 3.x) | linux2   |		'cls'
| Windows             | win32    |		'clear'
| Windows/Cygwin      | cygwin   |		'clear'
| Mac OS X            | darwin   |		'cls'
| OS/2                | os2      |		'cls'
| OS/2 EMX            | os2emx   |		'cls'
| RiscOS              | riscos   |		'	'
| AtheOS              | atheos   |		'	'
| FreeBSD 7           | freebsd7 |		'cls'
| FreeBSD 8           | freebsd8 |		'cls'
'---------------------'----------'

"""
	
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Funções auxiliares:
	
def distribuirCartas(nomeBOTS,qtdBOTS,qtdAssassinos,qtdAnjos, jogadores):
	auxAss	= qtdAssassinos
	auxAnj	= qtdAnjos
	auxCid	= qtdBOTS - qtdAssassinos - qtdAnjos
	cartas	= ['Assassino','Anjo','Cidadão',]

	assassinos 	= {}
	anjos		= {}
	cidadaos	= {}
	
	
	for nomeKey, jogador in jogadores.items():
		tentarDeNovo = True
		while tentarDeNovo:													# Enquanto ele não conseguir atribuir uma carta a esse BOT, tentará de novo...

			nome 		= jogador.nome
			saude 		= jogador.saude
			honestidade	= jogador.honestidade
			analisado 	= jogador.analisado
		
			carta = choice(cartas)

			if carta == 'Assassino':
				if auxAss > 0:
					auxAss -= 1
					jogadores[nomeKey]	= Assassino (nome,'Vivo', honestidade, analisado)		# -1, 0 ou 1 para honestidade
					assassinos[nomeKey]	= jogadores[nomeKey]
					tentarDeNovo 		= False
				else:
					cartas.remove('Assassino')
				
			elif carta == 'Anjo':
				if auxAnj > 0:
					auxAnj -= 1
					jogadores[nomeKey]			= Anjo (nome,'Vivo', honestidade, analisado)	# -1, 0 ou 1 para honestidade
					jogadores[nomeKey].jaSalvo	= False 										# Cada anjo só pode ser salvo uma única vez por partida
					anjos[nomeKey]				= jogadores[nomeKey]
					tentarDeNovo				= False
				else:
					cartas.remove('Anjo')

			elif carta == 'Cidadão':
				if auxCid > 0:
					auxCid -= 1
					jogadores[nomeKey]	= Cidadao (nome,'Vivo', honestidade, analisado)			# -1, 0 ou 1 para honestidade
					cidadaos[nomeKey]	= jogadores[nomeKey]
					tentarDeNovo		= False
			else:
				cartas.remove('Cidadão')
	return (jogadores,assassinos,anjos,cidadaos)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Variáveis e Constantes
usuario			= Detetive()					# O usuário será sempre detetive

qtdAnjos		= 2 							# Constante, por enquanto...
qtdAssassinos	= 2 							# Constante, por enquanto...
qtdBOTS			= 9 							# Constante, por enquanto...

jogadores 		= {}
nomeBOTS 		= {}							# Lista de nomes que o usuário irá fornecer

qtdBemVivos		= qtdBOTS - qtdAssassinos		# Do Bem = Total + Detetive (não contaremos) - assassinos
qtdKillersVivos	= qtdAssassinos

tamMaiorNome	= 10

perguntas 		= {1: 'Assassino',2: 'Anjo', 3: 'Cidadão'}

ptAssassinos	= 0
ptUsuario		= 0

try:
	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Imprimindo regras do jogo:
	import codecs
	regras = codecs.open('README','r',encoding='utf8')		# regras = open('README','r')
	print( regras.read() )
	regras.close()

	input('\n>>> Aperte <ENTER> para continuar <<<\n')
	os.system(limpar)


	# ---------------------------------------------------------------------------------------------------------------------------------------------------
	# Recebendo o nome dos BOTS e criando BOTS:
	for i in range(qtdBOTS):
		nome = input('Digite o nome do BOT %i: ' %(i))

		while nome.lower() in nomeBOTS or nome == '' or nome == 'REVISAR':									# REVISAR é uma palavra reservada
			nome = input('Digite outro nome: ')

		jogadores[nome.lower()]	= Jogador( nome, 'Vivo', choice( [-2, -1, 0, 1, 2] ), dict() ) 		# Criando BOTS, ainda sem cartas
		nomeBOTS[nome.lower()]	= nome 																# nomeBOTS[vinicius] = ViNiCiUs, por exemplo

		tamMaiorNome = max( [len(nome) for nome in nomeBOTS] ) 										# recebendo o tamanho do maior nome

	# ----------------------------------------------------------------------------------------------------------------------------------------------------
	# Iniciando partida:
	partida	= 1
	sair	= False

	while not sair: 											# Enquanto usuário não decidir sair
		#os.system(limpar)
		#print('Partida:',partida)
		#print('Usuário',ptUsuario,'vs',ptAssassinos,'Assassinos')
		# -------------------------------------------------------------------------------------------
		# Distribuindo cartas:
		(jogadores,assassinos,anjos,cidadaos) = distribuirCartas(nomeBOTS, qtdBOTS, qtdAssassinos, qtdAnjos,jogadores)

		# -------------------------------------------------------------------------------------------
		# TODO: Excluir, pois não usamos para nada '-' kkkkkkkkkkk
		# Assassinos se conhecendo:
		for assassino in assassinos.values():
			assassino.assassinos = assassinos

		# Anjos se conhecendo:					
		for anjo in anjos.values():
			anjo.anjos = anjos

		# -------------------------------------------------------------------------------------------
		# Rodadas:
		rodada = 0
		while qtdBemVivos > 0 and qtdKillersVivos > 0:	# A partida continuará até existirem pessoas boas vivas ou até o usuário advinhar todos assassinos
			os.system(limpar)
			rodada += 1
			print('Partida:',partida)
			print('Rodada:',rodada)
			print('Assassinos Vivos:',qtdKillersVivos)
			print('Usuário',ptUsuario,'vs',ptAssassinos,'Assassinos')
			print ('\n-------------- // -------------- //-------------- //-------------- //-------------- //-------------- // \n')
			#[print(jogador.nome,jogador.saude,jogador.honestidade,jogador.getClass()) for jogador in jogadores.values()]	# DEBUG
			#print()																										# DEBUG

			# ----------------------------------------------
			# Assassinos escolhem alguém para tentar matar:

			tentarMatar = ''
			for bossKiller in assassinos.values():
				if bossKiller.saude == 'Vivo':
					tentarMatar = bossKiller.escolherAlguem(jogadores, partida)
					break

			# TODO, a lista 'tentativas' e o 'cntMilagres' podiam ser STATIC para que não precisassemos iterar
			for assassino in assassinos.values():
				if assassino.nome != bossKiller.nome:						# Para não duplicar o registro
					assassino.tentativas.append(bossKiller.tentativas[-1])	# Todos assassinos precisam ter a lista de tantativas

			"""
				bossKiller será sempre o primeiro killer vivo encontrado,
				e ele é "boss" porque ele quem manda entre os assassinos,
				ou seja, que ele decidirá quem os assassinos tentarão matar!
			"""

			# ----------------------------------------------
			# Anjos escolhem alguém para tentar salvar:
			# TODO: Inteligência artificial dos anjos

			tentarSalvar = ''
			for bossAngel in anjos.values():
				if bossAngel.saude == 'Vivo':
					tentarSalvar = bossAngel.escolherAlguem(jogadores, partida)
					break

			"""
				bossAngel será sempre o primeiro angel vivo encontrado,
				e ele é "boss" porque ele quem manda entre os anjos,
				ou seja, que ele decidirá quem os anjos tentarão salvar!	
			"""

			# ----------------------------------------------
			# Detetive, ACORDE:
			if usuario.saude == 'Vivo': 							# Usuário só pode influênciar no jogo se ele não morreu

				# -----------------------
				# Detentive perguntando:
				entrada = 'REVISAR'
				while entrada == 'REVISAR':
					[print('%*s %s' %(tamMaiorNome,jogador.nome,jogador.saude)) for jogador in jogadores.values()]
					entrada 	= input('\nDetetive, escolha alguém (ou digite REVISAR): ')
					
					if entrada == 'REVISAR':
						print()
						for nomeKey,respostas in usuario.jogadoresConhecidos.items():
							print(nomeBOTS[nomeKey],':',sep='')
							for resposta in respostas:
								print('\t',resposta)
						print()

				# Detetive não pode perguntar pra alguém que está morto, nem pra alguém que não existe:
				nomeKey = entrada.lower()
				while nomeKey not in jogadores or jogadores[nomeKey].saude == 'Morto':
					print("\n*** OPÇÃO INVÁLIDA ***\n")
					[print('%*s %s' %(tamMaiorNome,jogador.nome,jogador.saude)) for jogador in jogadores.values()]
					entrada 	= input('\nDetetive, escolha alguém: ')
					nomeKey = entrada.lower()

				escolha = 0
				while escolha not in perguntas:
					print("\n1) " + entrada + " você é Assassino? \n2) " + entrada + " você é Anjo? \n3) " + entrada + " você é Cidadão?" )
					try:
						escolha = int( input('Escolha uma pergunta: ') )
					except ValueError:
						print('\n*** Digite apenas o número da pergunta ***')

				# -----------------------
				# BOT respondendo o Detetive:
				jogador		= jogadores[ nomeKey ]
				resposta	= jogador.responder( perguntas[escolha] )

				if nomeKey not in usuario.jogadoresConhecidos:									# Caso seja a primeira pergunta feita a esse BOT...
					usuario.jogadoresConhecidos[ nomeKey ] = list()								# ... criamos uma lista das respostas desse BOT

				usuario.jogadoresConhecidos[ nomeKey ].append(resposta)							# Lista de respostas do BOT

				# ----------------------------------------------
				# Atualizando Inteligência
				"""
					Para que o jogo fique mais frenético,
					a inteligência dos BOTs será atualizada
					a cada rodada ao invés de cada partida.
					Pois, do jeito que estava tinhamos um "deadlock"
				"""

				for jogador in jogadores.values():
					jogador.analisarRespostasPorRodada(jogadores, nomeKey, resposta)
				#print(jogador.analisado)											# DEBUG

			# ----------------------------------------------
			# Locutor conta uma história:

			# print('\nKiller Chose:',tentarMatar, '\nAngel Chose:', tentarSalvar)	# DEBUG

			if (tentarMatar == tentarSalvar):										# Se assassinos e anjos escolheram a mesma pessoa, temos um milagre!
				print("\n\n!!! MILAGRE !!!\n")

				# TODO: a lista 'tentativas' e o 'cntMilagres' podiam ser STATIC para que não precisassemos iterar
				for assassino in assassinos.values():
					assassino.cntMilagres += 1

			else:
				# TODO: tem que reiniciar o 'cntMilagres' de todos os assassinos '-'
				# TODO: a lista 'tentativas' e o 'cntMilagres' podiam ser STATIC para que não precisassemos iterar

				print("\n\n!!! " + nomeBOTS[tentarMatar] + " MORREU !!!\n")
				jogadores[tentarMatar].saude = 'Morto'
				qtdBemVivos -= 1																# Os assassinos nunca se matarão !

				#for assassino in assassinos.values():											# DEBUG
					#print('Killers', assassino.nome, assassino.cntMilagres, assassino.tentativas)	# DEBUG

			# ----------------------------------------------
			# Conhecidos do Detetive:
			print()
			for nomeKey,respostas in usuario.jogadoresConhecidos.items():
				print(nomeBOTS[nomeKey],':',sep='')
				for resposta in respostas:
					print('\t',resposta)
			print()
			# ----------------------------------------------
			# Detetive tem a chance de matar um dos assassinos:
			if qtdBemVivos > 0:	# Na última rodada, todos do bem estavam mortos e só sobrava os killers, então bastava o usuário acusá-los
				escolha = 0
				while escolha != 'n' and escolha != 's':
					escolha = input('Detetive, você quer arriscar (s/n)?\nR: ').lower()

					if escolha == 's':
						acertou,acertos = usuario.arriscar(jogadores, tamMaiorNome, perguntas)
						print ('\n\n\n\n-------------- // -------------- //-------------- //-------------- //-------------- //-------------- // \n\n\n')
						if acertou:
							for nomeKey,jogador in acertos.items():
								print('*** Assassino descoberto:',jogador.nome,'***')
								jogador.saude = 'Morto'
								qtdKillersVivos -= 1
								print('\n\n\n')
								_ = input('<ENTER> para continuar')
						else:
							print('*** ERROU ***\n\n\n')
							qtdBemVivos = 0
					elif escolha == 'n':
						print("\nOkay")
					else:
						print('\nOpção inválida\n')

		# -------------------------------------------------------------------------------------------
		# Revelando cartas:
		print('\n\nFim de Jogo:')
		[print(jogador) for jogador in jogadores.values()]

		#for jogador in jogadores.values():
			#jogador.analisarRespostas(jogadores, usuario.jogadoresConhecidos)

		"""
			No jogo de verdade, ninguém teria as informações que o detetive obteve,
			mas para deixar o jogo mais divertido, no final de cada PARTIDA,
			todos terão acesso a essas informações,
				para que os próximos anjos e assassinos possam aprender sobre a personalidade de cada BOT.
		"""
		
		if qtdKillersVivos > 0:
			ptAssassinos += 1
		elif qtdBemVivos > 0:
			ptUsuario += 1
		
		# -------------------------------------------------------------------------------------------
		# Jogar novamente?
		escolha = 0
		while escolha != 'n' and escolha != 's':
			escolha = input('\nJogar uma nova partida (s/n)?\nR: ').lower()

			if escolha == 'n':
				sair = True

			elif escolha == 's':
				qtdKillersVivos = qtdAssassinos 			# Assassinos voltam a viver
				qtdBemVivos 	= qtdBOTS - qtdAssassinos	# Galera do bem volta a viver
				usuario.jogadoresConhecidos.clear() 		# Limpando o dicionário dos conhecidos do usuário
				usuario.saude 	= "Vivo" 					# Caso o usuário tenha morrido, vamos revivê-lo

				partida += 1

			else:
				print('\nOpção inválida\n')

except KeyboardInterrupt:
	print('\n\nTCHAU TCHAU')
	input('Aperte <ENTER> ')
