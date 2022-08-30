


########### Reload - 08/2022 1.0 ############

# Drick Project

# Desenvolvido por Wandrew Tischler





import time
import random
import socket
import os
import requests
import threading
import hashlib
import string
import re
import urllib






############# Funções ################




####### Testar host ON/OFF

def ping():
	host = input("\n[#] Host >> ")
	response = os.system("ping -c 1 " +  host)
	print ("\n")
	if response == 0:
		fff = "\033[32m ✓ \033[0;0m"
		print (fff, host, "está online.\n")
	else:
		fff = "\033[31m X \033[0;0m"
		print (fff, host, "está offline ou inacessível.\n")
	
	
	
####### Capturar IP

def cap_ip():
	try:
		ent = input("\n[#] Host >> ")
		ip = socket.gethostbyname(ent)
		ip = "\033[32m" + ip + "\033[0;0m"
		capt = ("\nIP: ")
		print (capt, ip)
	except:
		print("\nComando inválido.")
	



####### Testar porta especifica


def cap_ban():
	host = input("\n[#] Host >> ")
	porta = int(input("[#] Porta >> "))

	
	if porta == 21:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")

	if porta == 22:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
	
	if porta == 25:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
	
		
	if porta == 80:
		s = socket.socket()
		s.connect((host, porta))
		s.send(b'GET /\n\n')
		print("\n")
		print(s.recv(10000))
	
		
	if porta == 443:
		try:
			s = socket.socket()
			s.connect((host, porta))
			s.send(b'GET /\n\n')
			print("\n")
			print(s.recv(10000))
		except:
			print("conexão não estabelecida.")
		
	else:
		print("  ")





def porth():
	try:
		host = input("\n[#] Host >> ")
		porta = int(input("[#] Porta >> "))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(4)
		result = sock.connect_ex((host, porta))
		if result == 0:
			str = "\033[32mestá aberta. \033[0;0m"
			print ("\nPorta", porta, str)
		else:
			str = "\033[31mestá fechada. \033[0;0m"
			print ("\nPorta", porta, str)
	except:
		print("\nComando inválido.")
    	
    	


####### Localizador de IP



def geo_ip():
	try:
		lista1 = []
		host = input("\n[#] Host >> ")
		host = socket.gethostbyname(host)
		host1 = "\033[32m" + host + "\033[0;0m"
		host1 = "   IP: " + host1
		lista1.append(host1)
		################        
		pais = "https://ipapi.co/" + host + "/country_name/"
		pais = requests.get(pais)
		pais = pais.text
		pais = "\033[32m" + pais + "\033[0;0m"
		pais = "   Pais: " + pais
		lista1.append(pais)
        #####################
		estado = "https://ipapi.co/" + host + "/region/"
		estado = requests.get(estado)
		estado = estado.text
		estado = "\033[32m" + estado + "\033[0;0m"
		estado = "   Estado: " + estado
		lista1.append(estado)
		#####################
		cidade = "https://ipapi.co/" + host + "/city/"
		cidade = requests.get(cidade)
		cidade = cidade.text
		cidade = "\033[32m" + cidade + "\033[0;0m"
		cidade = "   Cidade: " + cidade
		lista1.append(cidade)
		#####################
		latlong = "https://ipapi.co/" + host + "/latlong/"
		latlong = requests.get(latlong)
		latlong = latlong.text
		latlong = "\033[32m" + latlong + "\033[0;0m"
		latlong = "   Latitude e Longetude: " + latlong
		lista1.append(latlong)
		####################
		org = "https://ipapi.co/" + host + "/org/"
		org = requests.get(org)
		org = org.text
		org = "\033[32m" + org + "\033[0;0m"
		org = "   Organização: " + org
		lista1.append(org)
		####################
		asn = "https://ipapi.co/" + host + "/asn/"
		asn = requests.get(asn)
		asn = asn.text
		asn = "\033[32m" + asn + "\033[0;0m"
		asn = "   ASN: " + asn
		lista1.append(asn)
	
	
	except:
		print("Verifique sua conexão.")

	print("\n")
	for n in lista1:
		print(n)
	print("\n")



####### Capturar Banner

def cap_ban():
	host = input("\n[#] Host >> ")
	porta = int(input("[#] Porta >> "))

	if porta == 20:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
	
	
	if porta == 21:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")

	if porta == 22:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
		
	if porta == 80:
		s = socket.socket()
		s.connect((host, porta))
		s.send(b'GET /\n\n')
		print("\n")
		print(s.recv(10000))

		
	if porta == 443:
		try:
			s = socket.socket()
			s.connect((host, porta))
			s.send(b'GET /\n\n')
			print("\n")
			print(s.recv(10000))
		except:
			print("conexão não estabelecida.")
		
	else:
		print("  ")





#######  PSCAN   ###### Scanner de Portas:

def port_scan():
	print("\n\n      ∆ ---------- PSCAN PROJECT ---- 1.0 \n\n")
	
	#100.2.97.20 / portas 8000, 9000, 9090
	
	print("Tipos:\n\n[1] Scanner básico (0/2.000)\n[2] Scanner Mediano (0/10.000)\n[3] Scanner Completo (0/65535)\n\n")
	
	host = input("Host >> ")
	tipo_scan = input("Tipo >> ")
	print("\n\n")
	tipo_scan = int(tipo_scan)
	
	if tipo_scan == 1:
		finali = 2000
	elif tipo_scan == 2:
		finali = 10000
	elif tipo_scan == 3:
		finali = 65535
	else:
		print("entrada invalida.")
	
	global cont
	cont = 0
	
	port_on_list = []
	def thred():
				try:
					global cont
					cont += 1
					porta = cont
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.settimeout(4)
					result = sock.connect_ex((host, porta))
					if result == 0:
						print(host, " porta: ", porta, "\033[32m", "aberta", "\033[0;0m")
						port_on_list.append(porta)
					else:
						return
				except:
					return
					
	tru = False
	while tru == False:
					time.sleep(0.02)
					t = (threading.Thread(target=thred))
					t.start()
					if cont == finali:
						tru = True
	print("\n\n")
	



############# Elink

def link_extrator():

	print("\n\n\n          --------- E-Link | Extrator de links\n\n\n")
	host = input("[#] Site >> ")
	link1 = []
	host = "http://" + host
	response = requests.get(host)
	content = str(response.content)
	content = content.split(" ")
	cont = 0

	for n in content:
		if "http://"  in n:
			n = n
			if 'href="' in n:
				n1 = n.replace('href="', '')
				link1.append(n1)
				cont += 1
		if "https://"  in n:
			n = n
			if 'href="' in n:
				n2 = n.replace('href="', '')
				link1.append(n2)
				cont += 1


	print("\n\n\n")
	nn1 = 0
	linkz = []
	for link in link1:
		nn1 += 1
		g = 0

		for letra in link:
			g += 1
			if '"' in letra:
				nn = g
				nn = nn - 1
				final = (link[:nn])
				print(final)
				linkz.append(final)
	print ("\n\n", len(link1), "links indexados.\n\n\n")








######### PROJETO - HÓRUS ############



####### Função 1 #######

def hórus():
	
	def func1(porta, disp):
		global mediador1
		global x
		
		lista = []
		
		def test_b(host):
			global mediador1
			global x
			
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((host, porta))
			sock.settimeout(3)
			if result == 0:
				mediador1 += 1
				print("PORTA", porta, "\033[32m", "ABERTA", "\033[0;0m" ,"N","\033[33m", mediador1, "\033[0;0m", "  IP:", host)
				if mediador1 == disp:
					x = False
				lista.append(host)

		
		def capturarh():
			a = (random.randint(1,220))
			b = (random.randint(1,200))
			c = (random.randint(1,200))
			d = (random.randint(1,200))
			soma = a,b,c,d
			soma = str(soma)
			host = soma.replace(",", ".")
			host = host.replace(' ', '')
			host = host[1:-1]
			try:
				test_b(host)
			except:
				print("NOVO ERRO")
		

		mediador1 = 0
		x = True
		threads = []
		
		while x == True:
			time.sleep(0.000000005)
			try:
				t = threading.Thread(target=capturarh)
				try:
					threads.append(t)
					t.start()
				except:
					continue
			except:
				continue

		
		time.sleep(10)
		print("\n\n\n\n")
		print("Dispositivos Rastreados")
		print("\n\n")
		dg = 0
		for l  in lista:
			dg += 1
			l = "\033[32m" + l + "\033[0;0m"
			print("IP: ", l, " N°", dg)
			

													
																							
	################ FUNCAO 2 ##########
	listah = []    #   !!!!!!
	
	
	global tru
	tru = True
	
	global contador
	contador = 0
		
	
	######## 4 etapa #######
	
	def bannner(host, porta):
		global tru
		global contador
		
		host = host
		porta = porta
		
					
		######### FTP ########
		if porta == 21:
			s = socket.socket()
			s.settimeout(2)
			s.connect((host, porta))
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner capturado" + "\033[0;0m", rf, "\n")
			
			rf = str(rf)
			programa = servico.upper()
			banner = rf.upper()
			
			tkx = programa.split(" ")
			software = tkx[0]

			
			if versao == "0" or "x":
				if software in banner:
					contador += 1
					print("Software: ", software, " encontrado ✓", "N° ", contador)
					finali = host + " - " + banner
					listah.append(finali)
					if contador == disp:
						tru = False
			else:
				if software in banner:
					if versao in banner:
						contador += 1
						print("Versão: ", versao, " encontrado do software: ", software, "N° ", contador)
						finali = host + " - " + banner
						listah.append(finali)
						if contador == disp:
							tru = False
			
		
			
		#### Secure Shell [SSH]
		
		if porta == 22:
			s = socket.socket()
			s.settimeout(2)
			s.connect((host, porta))
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner capturado" + "\033[0;0m", rf, "\n")
			
			rf = str(rf)
			programa = servico.upper()
			banner = rf.upper()
			
			tkx = programa.split(" ")
			software = tkx[0]

			
			if versao == "0" or "x":
				if software in banner:
					contador += 1
					print("Software: ", software, " encontrado ✓", "N° ", contador)
					finali = host + " - " + banner
					listah.append(finali)
					if contador == disp:
						tru = False
			else:
				if software in banner:
					if versao in banner:
						contador += 1
						print("Versão: ", versao, " encontrado do software: ", software, "N° ", contador)
						finali = host + " - " + banner
						listah.append(finali)
						if contador == disp:
							tru = False


			
		
		###### HTTP / HTTPS
		if porta == 80 or 443:
			s = socket.socket()
			s.settimeout(2)
			s.connect((host, porta))
			s.send(b'GET /\n\n')
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner ca777pturado " + "\033[0;0m", "IP: ", host, "   ", rf, "\n")
			
			
			rf = str(rf)
			programa = servico.upper()
			banner = rf.upper()
			
			tkx = programa.split(" ")
			software = tkx[0]

			
			if versao == "0":
				if software in banner:
					contador += 1
					print("Software: ", software, " encontrado ✓", "N° ", contador)
					finali = host + " - " + banner
					listah.append(finali)
					if contador == disp:
						tru = False
			else:
				if software in banner:
					if versao in banner:
						contador += 1
						print("Versão: ", versao, " encontrado do software: ", software, "N° ", contador)
						finali = host + " - " + banner
						listah.append(finali)
						if contador == disp:
							tru = False
					
				
					
	####### 3 etapa #######
	def test_bc(host):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2) #### [ ! ]
		result = sock.connect_ex((host, porta))
		if result == 0:
			print(host, "porta", porta, "\033[32m", "aberta", "\033[0;0m")
			bannner(host, porta)
		elif result == 101:
			print(host, "porta", porta, "\033[33m", "rede inacessivel", "\033[0;0m codigo:", result)
		elif result == 111:
			print(host, "porta", porta, "\033[34m", "conexão recusada", "\033[0;0m codigo:", result)
		elif result == 113:
			print(host, "porta", porta, "\033[35m", "host inacessivel", "\033[0;0m codigo", result)
		else:
			print(host, "porta", porta, "\033[35m", "fechada", "\033[0;0m", result)

	
	
		
	######## 2 etapa ######
	def capturarh():
		a = (random.randint(1,250))
		b = (random.randint(1,200))
		c = (random.randint(1,200))
		d = (random.randint(1,200))
		soma = a,b,c,d
		soma = str(soma)
		host = soma.replace(",", ".")
		host = host.replace(' ', '')
		host = host[1:-1]
		try:
			test_bc(host)
		except:
			return
	
	
	####### 1 etapa #######
	def func2(servico, porta, disp, versao):
		threads = []
		
		
		while tru == True:
			time.sleep(0.05)
			try:
				t = threading.Thread(target=capturarh)
				t.start()
			except:
				continue
		
		
		
		
		##### Printar resultado da busca
		time.sleep(7)
		xxc = "          " * 30
		print(xxc)
				
		for n in listah:
			print("\nIP: ", "\033[33m" + n + "\033[0;0m")




    ###### Final das Funcoes
	
	rt52 = "\033[36m" + "HÓRUS" + "\033[0;0m"
	print("\n*   *  *    *     *      *   *       *      *      *     *  ")
	print(" *  *      *  [][][][]--(((̲̅=̲̲̅̅̅̅●̲̅̅))))--[][][][]  *  *   *   *")
	print("   *         *           .  .  .   *       *      *     * ")
	print("      *  *       *      .   .   .     *   *    *  *   *")
	print("  *     *    *  *      .    .    .  *   *   *       *    *")
	print("\n_---_-___---_-___--_-- _---_---_---_-___-- _---_-___---__--")
	print("_---_-_-___---_--_--_-_-_-", rt52, "-___---_-______---_-____")
	print(" _---_-__- _-_ ---_ - _ __ -- ___ _---_- [BETA] _-- _---_-_-\n")
	print("             \033[36mEsse programa deveria ser secreto.\033[0;0m\n\n\n")
	
	xx = True
	while xx == True:
		inp = input("\n|______ : ")
		
		if inp == "sair":
			xx = False
			
		elif inp == "1":
			print("\n    LOCALIZADOR DE PORTAS ONLINE\n")
			porta = int(input("PORTA: "))
			disp = int(input("N° DE DISPOSITIVOS: "))
			print("\n\n")
			func1(porta, disp)
		
		elif inp == "2":
			print("\n    LOCALIZADOR DE SOFTWARE EM PORTA\n")
			print("Use ", "\033[32m[0] ou [x]\033[0;0m", "para não especificar uma versão\n\n")
			servico = input("SERVIÇO / S.O: ")
			porta = int(input("PORTA: "))
			disp = int(input("N° DE DISPOSITIVOS: "))
			versao = str(input("VERSÃO: "))
			print("\n\n")
			func2(servico, porta, disp, versao)


			
		elif inp == "4":
			break


		elif inp == " " or " ":
			print("\n\nESSE COMANDO NÃO EXISTE.\nEsta é a lista de comandos existentes:\n\n\n[ 1 ] Localizar portas abertas.\n[ 2 ] Localizar software / versão em porta\n[ 4 ] Sair do programa")









################################################################################################################################################
################################################################################################################################################






nomep = "\033[36m" + "DRICK FRAMEWORK" "\033[0;0m"



print("\n\n\n      ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄ ")
print("     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌")
print("     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌") 
print("     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌▐░▌")  
print("     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌          ▐░▌░▌")   
print("     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌          ▐░░▌")    
print("     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌          ▐░▌░▌")   
print("     ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌▐░▌")  
print("     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌") 
print("      ░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌")
print("      ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀ \n")
                                                            

print("\n\n############  ########  ##### ### ######  ########  ######## # ##  #####")
print ("####### ### ### ##### --|", nomep, "|-- #########\033[36m v[1.0] \033[0;0m#########")
print("######## ####  ####### ############ ######## # ## #####  # # #  #### ### \n\n")






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

listag = ["kkefkwfkwfgekgk ","Navegue com segurança muitos querem te ver exposto", "Não compre terrenos na lua.", "Olá meu nome é Wandrew e atualmente tenho 18 anos. Oi futuro.", "Não se julgue quando não precisa, tente se divertir quando possível.", "Use o camando /limpar.", "Se voce se torna um mago quando empunha uma varinha magica voce tambem vira um hacker de posse do programa Drick Framework.", "Obrigado pela preferência.", "Hackers gostam de feriados?", "Beba agua.", "Use o Hórus para adquirir endereços IP online com especificação de programas, portas e versões operando na rede de computadores privada ou global.", "777 ", "Não use com moderação.", "O código fonte está cheio de gambiarras, más está rodando.", "Cuidado voce pode estar sendo espionado(a) agora", "666", "888", "...", "Oi", "Preciso dizer que não nos responsabilizamos pelo uso indevido?"]

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


style = "\033[31m" + " [+]" + "\033[0;0m"
frase_random = random.choice(listag)

print(style, frase_random)

	
	
strr = "\033[33m" + "[+]" + "\033[0;0m"

print("\n\n")
print(" ", strr ,"Use (/c) para listar os comandos.")
print(" ", strr, "Use (/info) para mais informações.\n\n\n")



################################################################################################################################################



x = True

while x == True:
	
	y = input("\n\n[\033[33m#\033[0;0m] >> ")
	
	# Comando para fechar o programa
	if y == "/sair":		
		x = False
	
	# Trata entradas direras
	elif y[0] == "!":
		teste = y.replace(" ", ",")
		print(teste)
		
		
	elif y == "/c":
		print("\n\n\nPARA USAR UMA FERRAMENTA UTILIZE O COMANDO ENTRE PARENTESES.\n \n\n[#] COMANDOS USUAIS:\n\nPing Host                               (\033[32mping\033[0;0m)\nCapturar IP                             (\033[32mcap ip\033[0;0m)\nTestar porta                            (\033[32mtporta\033[0;0m)\nCapturar banner                         (\033[32mcbanner\033[0;0m)\nLocalizar IP                            (\033[32mlocip\033[0;0m)\nExtrator de Links                       (\033[32melink\033[0;0m)\nHórus                                   (\033[32mhorus\033[0;0m)\nEscaner de Portas                       (\033[32mpscan\033[0;0m)")


				
	elif y == "/info":
		print("\n\n                      \033[32mDRICK FRAMEWORK\033[0;0m")
		print("\n O software (Drick Framework) é um pacote com vários algoritimos essênciais para um bom pentesting e uma boa análise de um sistema ou rede, o nosso software busca sempre agrupar as melhores alternativas para uma boa análise e uma rede de testes.\n")
		print("\n\n                    \033[32mCOMANDOS ADICIONAIS\033[0;0m")
		print("\n1 - Caso queira consultar alguma informação a respeito de algum programa da plataforma use o comando (/info) + Programa, por exemplo (/info ping), este comando retornará as principais informações sobre o mesmo.\n\n2 - Caso deseje fechar a framework utilize o comando (/sair)\n\n3 - Utilize os comandos (/limpar),(/clear) ou (/cls) para limpar a tela.")
		
		
		
	##########################         requisitar informações de determinadas funções             ############################################
	
	elif y == "/info ping":
		print("\n\033[32m PING\n\033[0;0m\nPING é um algoritimo usado para testar uma máquina remota afim de determinar se ela está online ou offline e obter dados de sua requisição como tempo de resposta.")
	
	elif y == "/info cap ip":
		print("\n\033[32m CAP IP (CAPTURAR IP)\n\033[0;0m\nCAP IP tem como função obter o endereço remoto de uma determinada máquina na rede, o algoritimo captura o ip (Internet Protocol) através de uma requisição.")
	
	elif y == "/info tporta":
		print("\n\033[32m TPORTA (TESTAR PORTA)\n\033[0;0m\nTPORTA é um testador de porta específica nativo da plataforma, basicamente ele testa se uma determinada porta de um dispositivo na rede está aberta ou fechada.")
	
	elif y == "/info localizar ip":
		print("\n\033[32m LOCALIZAR IP\n\033[0;0m\nEsta função lhe permite rastrear um dispositivo e obter características de sua localização.")
	
	elif y == "/info cbanner":
			print("\n\033[32m CBANNER (CAPTURAR BANNER)\n\033[0;0m\nApartir de requisições ao alvo é possível obter o serviço e sua versão que está a rodar em uma determinada porta com esta informação é possível obter um exploit.")
	
	elif y == "/info elink":
		print("\n\033[32m ELINK (Extraidor de Link)\n\033[0;0m\nEsse algoritimo tem como função extrair links de uma determinada página na web.")
	
	elif y == "/info pscan":
		print("\n\033[32m PSCAN (Scanner de Portas)\n\033[0;0m\nPSCAN é um scanner de portas simples que tem o intuito de testar as principais portas de um host e determinar se as mesmas estão abertas ou fechadas.")
	
	elif y == "/info horus":
		print("\n\033[32m HÓRUS\n\033[0;0m\nHÓRUS é um programa desenvolvido para identificar e rastrear dispositivos, serviços e sistemas operacionais na rede de computadores privada e global.")
		
		
################################################################################################################################################



	# Teste ON/OFF Host
	elif y == "ping":
		ping()
	
	# Capturar IP
	elif y == "cap ip":
		cap_ip()
		
	# Testar porta
	elif y == "tporta":
		porth()
	
	# Localizar IP
	elif y == "locip":
		geo_ip()
	
	# Capturar banner
	elif y == "cbanner":
		cap_ban()
		
	# Extrator de links
	elif y == "elink":
		link_extrator()
	
	# Scanner de portas
	elif y == "pscan":
		port_scan()
			
	
	# PROJETO - HÓRUS
	elif y == "horus":
		hórus()

     # Nazos Project
	elif y == "nazos":
		nazos()
		
	
	########### Limpar o console

	elif y == "/limpar":
		a = "           " * 10000
		print(a)

	elif y == "/clear":
		a = "           " * 10000
		print(a)


	elif y == "/cls":
		a = "           " * 10000
		print(a)
	

		
		
	# Trata as exceções
	elif y == " " or " ":
		print("\nESSE COMANDO NÃO EXISTE.")
		









"""
...e viveram felizes para sempre, fim.

"""
