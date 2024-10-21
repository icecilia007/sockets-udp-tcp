### **Questão 2 (Comentários Diretos no Código)**

### Explicação (Servidor TCP):
- `serverSocket = socket(AF_INET, SOCK_STREAM)`: Cria um socket TCP. `AF_INET` indica que estamos usando IPv4, e `SOCK_STREAM` indica que o socket usará o protocolo TCP.
- `serverSocket.bind(('', serverPort))`: Liga o socket à porta 12000 no servidor. O servidor usará essa porta para ouvir conexões de clientes.
- `serverSocket.listen(1)`: Coloca o socket no modo de escuta, esperando conexões. O número `1` define o tamanho da fila de conexões pendentes.
- `connectionSocket, addr = serverSocket.accept()`: Aceita uma conexão de um cliente. Isso cria um novo socket `connectionSocket` exclusivo para se comunicar com esse cliente.
- `sentence = connectionSocket.recv(1024).decode()`: Recebe dados do cliente, até 1024 bytes. A função `recv()` aguarda até que os dados sejam recebidos.
- `capitalizedSentence = sentence.upper()`: Converte a mensagem recebida para maiúsculas.
- `connectionSocket.send(capitalizedSentence.encode())`: Envia a mensagem de volta ao cliente.- **`connectionSocket.close()`**: Fecha o socket de comunicação com o cliente, encerrando essa conexão. O servidor continua escutando novas conexões.


### Explicação (Cliente TCP):
- `clientSocket = socket(AF_INET, SOCK_STREAM)`: Cria um socket TCP para o cliente, usando IPv4 (`AF_INET`) e TCP (`SOCK_STREAM`).
- `clientSocket.connect((serverName, serverPort))`: Conecta o cliente ao servidor, usando o endereço IP ou nome do servidor e a porta (12000). A conexão TCP é estabelecida nesse ponto.
- `sentence = input('Input lowercase sentence: ')`: Pede ao usuário para inserir uma frase. Essa frase será enviada ao servidor.
- `clientSocket.send(sentence.encode())`: Envia a mensagem digitada pelo usuário para o servidor. O método `encode()` transforma a string em bytes, já que o socket trabalha com bytes.
- `modifiedSentence = clientSocket.recv(1024)`: Recebe a resposta do servidor. O método `recv()` espera até receber dados do servidor (no máximo 1024 bytes).
- `print('From Server:', modifiedSentence.decode())`: Exibe a mensagem recebida do servidor (que agora está em maiúsculas), convertendo os bytes de volta para string com `decode()`.
- `clientSocket.close()`: Fecha o socket e encerra a conexão com o servidor.

### Questão 3: Utilizando netstat para Verificar Conexões
Execute o Servidor TCP e, em seguida, o Cliente TCP.

Em uma terceira janela, rode o seguinte comando para verificar a conexão estabelecida:

`netstat -an | grep 12000`
Isso irá mostrar todas as conexões na porta 12000, confirmando que o cliente e o servidor estão conectados.