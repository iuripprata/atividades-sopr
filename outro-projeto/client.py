import socket
import json
import functions

socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socketclient.connect(('localhost', 7777))
except:
    print('Conexão não estabelecida')

comp = 0
temp = 0
lista = []

menu = 0
while menu != 5:
   menu = functions.menu()
   lista.append(menu)

   #CALCULO TEMPERATURA
   if menu == 1:
       valor = int(input("DIGITE O VALOR A SER CONVERTIDO:  "))
       print('\n')
       lista.append(valor)

       #MENU DE TEMPERATURAS
       menuT = functions.convTemp()
       lista.append(menuT)

       #ENVIO DE INFORMAÇÕES
       lista = json.dumps(lista)
       lista = lista.encode('utf-8')
       socketclient.send(lista)

       #ZERANDO A LISTA
       lista = json.loads(lista)
       lista.clear()

       #CELSIUS EM KELVIN
       if menuT == 1:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)
           print("VALOR EM KELVIN: %i" % int(temp))
           print('\n')

       #CELSIUS → FAHRENHEITS
       elif menuT == 2:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM FAHRENHEITS: %i" % int(temp))
           print('\n')

       #KELVIN → FAHRENHEITS
       elif menuT == 3:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM FAHRENHEITS: %i" % int(temp))
           print('\n')

       #KELVIN → CELSIUS
       elif menuT == 4:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM CELSIUS: %i" % int(temp))
           print('\n')

       #FAHRENHEITS → CELSIUS
       elif menuT == 5:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM CELSIUS: %i" % int(temp))
           print('\n')

       #FAHRENHEITS → KELVIN
       elif menuT == 6:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM KELVIN: %i" % int(temp))
           print('\n')


   # CALCULO COMPRIMENTO
   if menu == 2:
       valor = float(input("DIGITE O VALOR A SER CONVERTIDO:  "))
       print('\n')
       lista.append(valor)

       #MENU DE COMPRIMENTOS
       menuC = functions.convComp()
       lista.append(menuC)

       #ENVIO DE INFORMAÇÕES
       lista = json.dumps(lista)
       lista = lista.encode('utf-8')
       socketclient.send(lista)

       #ZERANDO A LISTA
       lista = json.loads(lista)
       lista.clear()

       #METROS → QUILÔMETROS
       if menuC == 1:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)
           print("VALOR EM QUILÔMETROS: %.5f" % float(temp))
           print('\n')

       #METROS → CENTÍMETROS
       elif menuC == 2:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM CENTÍMETROS: %.5f" % float(temp))
           print('\n')

       #QUILÔMETROS → CENTÍMETROS
       elif menuC == 3:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM CENTÍMETROS: %.5f" % float(temp))
           print('\n')

       #QUILÔMETROS → METROS
       elif menuC == 4:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM METROS: %.5f" % float(temp))
           print('\n')

       #CENTÍMETROS → QUILÔMETROS
       elif menuC == 5:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM QUILÔMETROS: %.5f" % float(temp))
           print('\n')

       #CENTÍMETROS → METROS
       elif menuC == 6:
           temp = socketclient.recv(1024)
           temp = json.loads(temp)

           print("VALOR EM METROS: %.5f" % float(temp))
           print('\n')

   elif menu == 3:
       print("Até a próxima, colega...")
       socketclient.close()
       break

   elif menu != 1 and menu != 2 and menu != 3:
       print("Digite um valor válido!")
   lista.clear()
