
idconta = 0

contador = 0

n_usuario = 0


saldo1 = 0
saldo2 = 0
saldo3 = 0
repetir = True
login = True
cadastro = True
n_transf = 1000
import os

while repetir == True:
  repetir = input("Iniciar?").lower()=='sim'
  if repetir == False:
    print("Encerrando programa!")
    login = False
  elif repetir == True:
    login = True
    
  while  login == True:
    
    login = input("Voce já possui cadastro em nosso aplicativo?").lower()=='sim'
    
    if login ==False:
      
      os. system ("clear")
      cadastro = input("gostaria de realizar seu cadastro agora?").lower()=='sim'
      if cadastro ==True:
        contador = contador+1
        os. system ("clear")
        
        nome = input("Por favor, informe seu nome: ")
        
        if contador == 1:
          nome1=nome
          
        if contador == 2:
          nome2=nome
          
        if contador ==3:
          nome3=nome
          
        
        
        if contador == 1:
         
          os. system ("clear")
         
          senha1 = input("Por favor, escolha uma senha para proteção de sua conta: ")
         
          
        if contador == 2:
          
          os. system ("clear")
          
          senha2 = input("Por favor, escolha uma senha para proteção de sua conta: ")
          
          
        if contador ==3:
          
          os. system ("clear")
          senha3= input("Por favor, escolha uma senha para proteção de sua conta: ")
          
        
        os. system ("clear")
        confirmasenha = input("Por favor, confirme sua senha: ")
        
        if contador == 1:
          
          while confirmasenha!=senha1:
            
            os. system ("clear")
            confirmasenha = input("Há algo errado, por favor, digite novamente sua senha:")
          
          
      
        elif contador == 2:
          
          while confirmasenha!=senha2:
            
            os. system ("clear")
            confirmasenha = input("Há algo errado, por favor, digite novamente sua senha:")
          
      
        
        elif contador == 3:
          
          while confirmasenha!=senha3:
           
            os. system ("clear")
           
            confirmasenha = input("Há algo errado, por favor, digite novamente sua senha:")
            
        os. system ("clear")
        
        
        print ("Senha cadastrada com sucesso", nome)
        
        
        email = input("Por favor, escolha um email para seu acesso: ")
        
        if contador == 1:
          email1=email
          
        elif contador == 2:
          email2=email
          
        elif contador ==3:
          email3=email
        os. system ("clear")
        confirmaemail = input("Por favor, confirme seu email: ")
        
        if contador == 1:
            
            while email1 != confirmaemail:
              
              os. system ("clear")
             
              confirmaemail = input("Há algo errado, por favor digite novamente seu email: ")
      
        elif contador == 2:
            
            while email2 != confirmaemail:
              
              os. system ("clear")
              
              confirmaemail = input("Há algo errado, por favor digite novamente seu email: ")
        elif contador == 3:
            
            while email3 != confirmaemail:
              
              os. system ("clear")
              
              confirmaemail = input("Há algo errado, por favor digite novamente seu email: ")
              
        os. system ("clear")            
        print("Email confirmado com sucesso!")
      
      
      
        idconta = idconta+1
      
        n_usuario = 100+idconta
        
        if n_usuario == 101:
          usuario = n_usuario
          os. system ("clear")
          deposito = float(input("Deposite algum valor para que possamos validar sua conta:"))
          saldo1 = saldo1+deposito
          os. system ("clear")
          print("Saldo atual de sua conta é de R$", saldo1)
          
        elif n_usuario == 102:
          usuario = n_usuario
          os. system ("clear")
          deposito = float(input("Deposite algum.valor para que possamos validar sua conta:"))
          saldo2 = saldo2+deposito
          os. system ("clear")
          print("Saldo atual de sua conta é de R$", saldo2)
          
        elif n_usuario == 103:
          usuario = n_usuario
          os. system ("clear")
          deposito=float(input("Deposite algum valor para que possamos validar sua conta: "))
          saldo3 = saldo3+deposito
          os. system ("clear")
          print("Saldo atual de sua conta é de R$", saldo3)
        
      
        print("O ID de sua conta é: ", n_usuario)
        print("Conta cadastrada com sucesso!")
        
        
        
      else :
        
        os. system ("clear")
        print("Que pena, fica para a proxima, até logo.")
        
    else:
      os. system ("clear")
      usuario = float(input("Por favor, digite o ID de sua conta: "))
      
      if usuario == 101:
        os. system ("clear")
        print( "Bem vindo a sua conta", nome1)
        
        senha = input ("Por favor, digite sua senha: ")
        if senha != senha1:
          while senha != senha1:
            os. system ("clear")
            senha= input("Por favor, tente novamente")
        os. system ("clear")
        print("Login efetuado com sucesso")
        print("Olá", nome1)
        print("O saldo em sua conta é de R$", saldo1)
        
        print("Para GERAR QRCODE selecione 1")
        print("Para PAGAMENTOS selecione 2")
        print("Para ENCERRAR, selecione 4")
        acao = float(input("Que ação gostatia de realizar agora?"))
        
        while acao != 4 :
          
          if acao ==2:
            n_transf = n_transf+1
            transferencia = pagamentos
            os. system ("clear")
            destinatario = float(input("Qual o ID da conta para quem sera o pagamento: "))
            
            if destinatario == 103:
              saldo3 = saldo3+transferencia
              saldo1 = saldo1-transferencia
              os. system ("clear")
              print("Pagamento realizado com sucesso para", destinatario ,nome3,transferencia, n_transf )
              print("Seu novo saldo é de R$", saldo1)
              acao = float(input("Que ação gostatia de realizar agora?"))
          
            
            
            
            if destinatario == 102:
              saldo2 = saldo2+transferencia
              saldo1 = saldo1-transferencia
              os. system ("clear")
              print("Pagamento realizado com sucesso para", destinatario, "/" ,nome2 ,"/",transferencia,"/", n_transf )
              print("Seu novo saldo é de R$", saldo1)
              acao = float(input("Que ação gostatia de realizar agora?"))
          
            
            
            
            
          
          if acao == 1:
            n_transf = n_transf+1
            os. system ("clear")
            devedor = float(input("Gerar QRCode para qual conta ?"))
            os. system ("clear")
            pagamento = float(input("De quanto será a cobrança?"))
            if devedor == 103:
            		os. system ("clear")
            		print("QRCode: ", devedor,";",nome3,";",pagamento,";", n_transf)
            if devedor == 102:
            		os. system ("clear")
            		print("QRCode: ", devedor ,";", nome2 ,";", pagamento ,";", n_transf)
            acao = float(input("Que ação gostatia de realizar agora?"))
            
        
      
        
      elif usuario == 102:
        os. system ("clear")
        print("Bem vindo a sua conta", nome2)
        
        senha = input ("Por favor, digite sua senha: ")
        if senha != senha2:
          while senha != senha2:
            os. system ("clear")
            senha= input("Por favor, tente novamente")
        os. system ("clear")
        print("Login efetuado com sucesso")
        print("Olá", nome2)
        print("O saldo em sua conta é de R$", saldo2)
        
        print("Para GERAR QRCODE selecione 1")
        print("Para PAGAMENTOS selecione 2")
        print("Para ENCERRAR, selecione 4")
        acao = float(input("Que ação gostatia de realizar agora?"))
        
        while acao != 4 :
          
          if acao ==2:
            os. system ("clear")
            destinatario = float(input("Qual o ID da conta para quem sera o pagamento: "))
            transferencia = pagamento
            
            if destinatario == 103:
              
              saldo3 = saldo3+transferencia
              saldo2 = saldo2-transferencia
              os. system ("clear")
              print("Pagamento realizado com sucesso para", destinatario, "/" ,nome3 ,"/",transferencia,"/", n_transf )
              print("Seu novo saldo é de R$", saldo2)
              acao = float(input("Que ação gostatia de realizar agora?"))
          
   
            
            
            if destinatario == 101:
              
              saldo1 = saldo1+transferencia
              saldo2 = saldo2-transferencia
              os. system ("clear")
              print("Pagamento realizado com sucesso para", destinatario, "/" ,nome1 ,"/",transferencia,"/", n_transf )
              print("Seu novo saldo é de R$", saldo2)
              acao = float(input("Que ação gostatia de realizar agora?"))
          
            
            
            
            
          
          if acao == 1:
            os. system ("clear")
            n_transf = n_transf+1
            
            devedor = float(input("Gerar QRCode para qual conta ?"))
            
            pagamento = float(input("De quanto será a cobrança?"))
            if devedor == 101:
            	
            	print("QRCode: ", devedor,";",nome1,";",pagamento,";", n_transf)
            if devedor == 103:
            	
            	print("QRCode: ", devedor,";",nome3,";",pagamento,";", n_transf)
            acao = float(input("Que ação gostatia de realizar agora?"))
            
        
    
        
      elif usuario == 103:
        os. system ("clear")
        print("Bem vindo a sua conta", nome3)
        senha = input ("Por favor, digite sua senha: ")
        if senha != senha3:
          while senha != senha3:
            os. system ("clear")
            senha= input("Por favor, tente novamente")
        os. system ("clear")
        print("Login efetuado com sucesso")
        print("Olá", nome3)
        print("O saldo em sua conta é de R$", saldo3)
        
        print("Para GERAR QRCODE selecione 1")
        print("Para PAGAMENTOS selecione 2")
        print("Para ENCERRAR, selecione 4")
        acao = float(input("Que ação gostatia de realizar agora?"))
        
        while acao != 4 :
          
          if acao ==2:
            os. system ("clear")
            destinatario = float(input("Qual o ID da conta para quem sera o pagamento: "))
            transferencia = pagamento
            
            if destinatario == 102:
              saldo2 = saldo2+transferencia
              saldo3 = saldo3-transferencia
              os. system ("clear")
              print("Pagamento realizado com sucesso para", destinatario, "/" ,nome2 ,"/",transferencia,"/", n_transf )
              print("Seu novo saldo é de R$", saldo3)
              acao = float(input("Que ação gostatia de realizar agora?"))
          
            
            
            
            if destinatario == 101:       
              saldo1 = saldo1+transferencia
              saldo3 = saldo3-transferencia
              os. system ("clear")
              print("Pagamento realizado com sucesso para", destinatario, "/" ,nome1 ,"/",transferencia, "/", n_transf )
              print("Seu novo saldo é de R$", saldo3)
              acao = float(input("Que ação gostatia de realizar agora?"))
          
            
            
            
            
          
          if acao == 1:
            n_transf = n_transf+1
            os. system ("clear")
            devedor = float(input("Gerar QRCode para qual conta ?"))
            os. system ("clear")
            pagamento = float(input("De quanto será a cobrança?"))
            if devedor == 101:
             	os. system ("clear")
             	print("QRCode: ", devedor,";",nome1,";",pagamento,";", n_transf)
            if devedor == 102:
            	 os. system ("clear")
            	 print("QRCode: ", devedor,";",nome2,";",pagamento,";", n_transf)
            acao = float(input("Que ação gostatia de realizar agora?"))
