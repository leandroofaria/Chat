# **Projeto Final: Chat em Tempo Real**

---

## **Descrição do Projeto**
Este projeto implementa um sistema de chat em tempo real que utiliza **sockets** para comunicação entre múltiplos dispositivos. A arquitetura inclui um **servidor** para gerenciar conexões e múltiplos **clientes** que interagem em um ambiente de chat. O sistema suporta **mensagens broadcast**, **mensagens privadas (unicast)** e **comando para sair do chat**. Ele também possui **tratamento de erros** para garantir uma experiência estável.

---

## **Funcionalidades Principais**

1. **Comunicação entre Múltiplos Dispositivos**
   - Suporta comunicação simultânea entre diversos clientes conectados a um servidor.
   - Conexão realizada por meio de uma **VPN** (Radmin VPN).

2. **Mensagens Broadcast**
   - Todos os participantes recebem mensagens públicas enviadas por qualquer cliente.
   - O servidor notifica os clientes quando um novo usuário entra ou sai do chat.

3. **Mensagens Unicast**
   - Envio de mensagens privadas para um cliente específico, utilizando o formato:
     ```
     @nome_do_cliente mensagem
     ```

4. **Comando para Sair do Chat**
   - O cliente pode digitar `/sair` para encerrar sua conexão.
   - O servidor notifica os demais clientes sobre a saída.

5. **Tratamento de Erros**
   - **Nomes Inválidos:** Nomes com espaços ou caracteres inválidos são rejeitados.
   - **Formato de Mensagem Inválido:** Notifica o cliente se a mensagem privada estiver incorreta.
   - **Desconexão Abrupta:** Remove clientes desconectados e evita travamentos.
   - **Erro de Conexão:** Detecta falhas ao conectar ao servidor e informa o usuário.

6. **Mensagens em Tempo Real**
   - Utiliza threads para garantir comunicação simultânea e contínua entre clientes e servidor.

---

## **Configurações Necessárias**

### **1. Instalar Python**
Certifique-se de que o Python está instalado em todos os dispositivos que executarão o servidor ou clientes. Adicione o Python ao PATH durante a instalação.

### **2. Baixar e Configurar Radmin VPN**
- Instale o **Radmin VPN** em todos os dispositivos.
- Conecte-se à rede VPN:
  - **Nome da rede:** Projeto Final – Chat  
  - **Senha:** 123456
- Teste a conectividade entre os dispositivos utilizando o comando `ping`.

### **3. Executar o Servidor**
1. No dispositivo que rodará o servidor:
   - Abra o terminal (cmd).
   - Navegue até o diretório onde o arquivo `servidor.py` está salvo.
   - Execute o comando:
     ```
     python servidor.py
     ```

2. O servidor estará escutando conexões na porta 9999.

### **4. Executar os Clientes**
1. No dispositivo de cada cliente:
   - Abra o terminal (cmd).
   - Navegue até o diretório onde o arquivo `cliente.py` está salvo.
   - Execute o comando:
     ```
     python cliente.py
     ```

2. Digite o nome do cliente ao entrar no chat (o nome deve ser único e sem espaços).

---

## **Como Usar**

### **Mensagens Broadcast**
- Qualquer mensagem enviada sem o prefixo `@` será enviada para todos os participantes do chat.

### **Mensagens Privadas (Unicast)**
- Para enviar uma mensagem privada: @nome_do_cliente mensagem
- Exemplo: @Maria Oi, tudo bem?

  
### **Sair do Chat**
- Digite `/sair` para sair do chat.
- Os demais participantes serão notificados.

---

## **Requisitos Funcionais**

1. **Comunicação Simultânea:** Permitir múltiplos dispositivos conectados ao mesmo tempo.
2. **Mensagens Broadcast:** Notificar todos os clientes sobre mensagens públicas e eventos de entrada/saída.
3. **Mensagens Unicast:** Implementar envio de mensagens privadas para clientes específicos.
4. **Comando de Saída:** Notificar a saída de um cliente.
5. **Tratamento de Erros:** Garantir estabilidade e evitar falhas na comunicação.

---

## **Como o Projeto Funciona**

### **1. Utilização de Sockets**
- Os **sockets** são utilizados para gerenciar a comunicação TCP entre o cliente e o servidor:
- **Servidor:** Configurado para escutar conexões na porta 9999 e gerenciar os clientes conectados.
- **Cliente:** Conecta ao servidor utilizando o IP e a porta.

### **2. Threads**
- **No Servidor:** Cada cliente conectado é gerenciado por uma thread separada.
- **No Cliente:** Uma thread adicional é utilizada para receber mensagens do servidor enquanto o cliente envia mensagens.

### **3. Comunicação**
- **Envio de Mensagens:** Utiliza `sendall` para garantir que todos os dados sejam enviados.
- **Recepção de Mensagens:** Utiliza `recv` para processar mensagens recebidas do servidor.

### **4. Broadcast**
- Implementado no servidor por meio da função `broadcast`:
- Envia mensagens para todos os clientes conectados, exceto o remetente.
- Remove clientes desconectados automaticamente.

---

## **Tratamento de Erros Implementado**
1. **Nomes Inválidos:**
 - O servidor valida que o nome deve conter apenas letras, números e `_`.
2. **Formato de Mensagem Inválido:**
 - Notifica o cliente se a mensagem unicast não seguir o formato correto.
3. **Erro de Conexão:**
 - Captura falhas ao conectar ao servidor ou enviar mensagens.
4. **Desconexão Abrupta:**
 - Remove clientes desconectados e evita que o servidor trave.

---


