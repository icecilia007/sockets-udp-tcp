from socket import *

# Definindo o endereço do servidor e a porta
serverName = 'localhost'  # Use o IP real do servidor caso esteja em máquinas diferentes
serverPort = 12000

# Criando o socket UDP. AF_INET indica IPv4, SOCK_DGRAM indica UDP.
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Solicitando ao usuário que insira uma frase
message = input('Input lowercase sentence: ')

# Enviando a mensagem para o servidor
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Recebendo a resposta do servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Exibindo a mensagem modificada (em maiúsculas)
print(modifiedMessage.decode())

# Fechando o socket do cliente
clientSocket.close()
