import json
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
server.listen()
print('Server Rodando...')
print('Aguardando conexão...')
try:
    client, addr = server.accept()
    print(f'Servidor conectado a {addr}')
except:
    print('Servidor não conectado!')

def getting():
   recvd = client.recv(1024)
   recvd = recvd.decode('utf-8')
   recvd = json.loads(recvd)
   return recvd

def sending(valor):
   valor = json.dumps(valor).encode('utf-8')
   client.send(valor)

while True:
   try:
      lista = getting()
      print(lista)
      print('Usuário escolheu opção ', lista)


      #CALCULO TEMPERATURA
      if lista[0] == 1:
         if lista[2] == 1:
            kelvin = lista[1] + 273
            sending(kelvin)

         elif lista[2] == 2:
            faren = lista[1] * 1.8 + 32
            sending(faren)

         elif lista[2] == 3:
            faren = (lista[1] - 273) * (9/5) + 32
            sending(faren)

         elif lista[2] == 4:
            celsius = lista[1] - 273
            sending(celsius)

         elif lista[2] == 5:
            celsius = (lista[1] - 32) * (5/9)
            sending(celsius)

         elif lista[2] == 6:
            kelvin = (lista[1] - 32) * (5/9) + 273
            sending(kelvin)


      #CALCULO COMPRIMENTO
      elif lista[0] == 2:

         if lista[2] == 1:
            km = lista[1] / 1000
            sending(km)

         elif lista[2] == 2:
            cm = lista[1] * 100
            sending(cm)

         elif lista[2] == 3:
            cm = lista[1] * 100000
            sending(cm)

         elif lista[2] == 4:
            m = lista[1] * 1000
            sending(m)

         elif lista[2] == 5:
            cm = lista[1] / 100000
            sending(cm)

         elif lista[2] == 6:
            m = lista[1] / 1000
            sending(m)

      elif lista[0] == 3:
         raise Exception

   except:
      print('Conexão encerrada!')
      client.close()
      print('Aguardando conexão...')
      client, addr = server.accept()
      print(f'Servidor conectado a {addr}')
