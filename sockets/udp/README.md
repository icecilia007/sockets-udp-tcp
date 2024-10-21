### **Questão 2 (Comentários Diretos no Código)**

#### Explicação (Servidor UDP)

- `serverPort = 12000`: Define a porta onde o servidor ficará escutando.
- `serverSocket = socket(AF_INET, SOCK_DGRAM)`: Cria o socket UDP, que usa a família de endereços IPv4.
- `serverSocket.bind(('', serverPort))`: Liga o socket à porta 12000 para receber mensagens.
- `message, clientAddress = serverSocket.recvfrom(2048)`: Aguarda e recebe uma mensagem de até 2048 bytes de um cliente.
- `modifiedMessage = message.decode().upper()`: Converte a mensagem recebida para letras maiúsculas.
- `serverSocket.sendto(modifiedMessage.encode(), clientAddress)`: Envia a mensagem modificada de volta ao cliente.
- O loop `while True:` mantém o servidor ativo esperando novas mensagens.

#### Explicação (Cliente UDP)

- `serverName = 'localhost'`: Define o nome ou IP do servidor.
- `clientSocket = socket(AF_INET, SOCK_DGRAM)`: Cria o socket UDP para o cliente.
- `clientSocket.sendto(message.encode(), (serverName, serverPort))`: Envia a mensagem para o servidor.
- `modifiedMessage, serverAddress = clientSocket.recvfrom(2048)`: Aguarda e recebe a resposta do servidor.
- `print(modifiedMessage.decode())`: Exibe a mensagem convertida para maiúsculas.
- `clientSocket.close()`: Fecha o socket após a comunicação.

### Questão 3: Utilizando netstat para Verificar Conexões
Execute o Servidor UDP e, em seguida, o Cliente UDP.

Em uma terceira janela, rode o seguinte comando para verificar a conexão estabelecida:

`netstat -an | grep 12000`
Isso irá mostrar todas as conexões na porta 12000, confirmando que o cliente e o servidor estão conectados.