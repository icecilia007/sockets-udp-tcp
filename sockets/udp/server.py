from socket import *

# Definindo a porta do servidor
serverPort = 12000

# Criando o socket UDP. AF_INET é a família de endereços (IPv4), SOCK_DGRAM é o tipo de socket (UDP).
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Ligando o socket à porta especificada para que ele possa receber mensagens.
serverSocket.bind(('', serverPort))

# Informando que o servidor está pronto para receber mensagens
print("The server is ready to receive")

# Loop infinito para que o servidor fique sempre ativo e aguardando mensagens
while True:
    # Recebendo a mensagem do cliente e o endereço do cliente (IP e porta)
    message, clientAddress = serverSocket.recvfrom(2048)

    # Convertendo a mensagem para maiúsculas
    modifiedMessage = message.decode().upper()

    # Enviando a mensagem modificada de volta ao cliente
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
