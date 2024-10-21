### **Passo 3: Cliente Diferente Usando `netcat`**

#### **Cliente UDP com `netcat`**
No terminal, execute o seguinte comando:

```bash
echo "mensagem em minusculas" | nc -u localhost 12000
```

Isso enviará a mensagem para o servidor UDP na porta 12000.

#### **Cliente TCP com `telnet`**
Para TCP, use o **telnet**:

```bash
telnet localhost 12000
```

Após conectar, você pode digitar a mensagem que será enviada ao servidor TCP.

### **Passo 4: Desafio (Servidor Diferente com `netcat`)**

#### **Servidor UDP com `netcat`**
Substitua o servidor Python por um servidor UDP usando `netcat`:

```bash
nc -u -l 12000
```

Isso cria um servidor UDP escutando na porta 12000. Agora, você pode enviar mensagens com o cliente UDP.

#### **Servidor TCP com `netcat`**
Para TCP:

```bash
nc -l 12000
```

Isso cria um servidor TCP escutando na porta 12000. Agora, qualquer cliente TCP pode se conectar e enviar mensagens.
