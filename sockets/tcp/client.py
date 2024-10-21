from socket import *

# Definindo o endereço e a porta do servidor
serverName = 'localhost'  # Use o IP do servidor se estiver em máquinas diferentes
serverPort = 12000

# Criando o socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Conectando ao servidor
clientSocket.connect((serverName, serverPort))

# Solicitando uma frase ao usuário
sentence = input('Input lowercase sentence: ')

# Enviando a mensagem ao servidor
clientSocket.send(sentence.encode())

# Recebendo a resposta do servidor
modifiedSentence = clientSocket.recv(1024)

# Exibindo a resposta
print('From Server:', modifiedSentence.decode())

# Fechando o socket
clientSocket.close()
