from socket import *

# Definindo a porta do servidor
serverPort = 12000

# Criando o socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associando o socket à porta 12000
serverSocket.bind(('', serverPort))

# Habilitando o servidor para escutar até 1 conexão pendente
serverSocket.listen(1)

# Informando que o servidor está pronto para receber
print('The server is ready to receive')

# Loop infinito para aceitar conexões de clientes
while True:
    # Aceitando a conexão de um cliente
    connectionSocket, addr = serverSocket.accept()

    # Recebendo os dados do cliente (até 1024 bytes)
    sentence = connectionSocket.recv(1024).decode()

    # Convertendo a mensagem para maiúsculas
    capitalizedSentence = sentence.upper()

    # Enviando a mensagem de volta ao cliente
    connectionSocket.send(capitalizedSentence.encode())

    # Fechando a conexão com o cliente
    connectionSocket.close()
