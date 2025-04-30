# 🤖``Meubot_TeamFuria - Telegram Bot da FURIA Esports: Desáfio estágio``

*MeubotFurioso é um bot desenvolvido em Python para o Telegram, voltado aos fãs da equipe de CS:GO da **FURIA Esports**. Ele oferece informações rápidas e atualizadas sobre o time, seus jogadores e próximos jogos, tudo com comandos simples e interativos.*

## 🚀``Funcionalidades``

- `/start` — Mensagem de boas-vindas com botões interativos.
- `/proximosjogos` — Exibe os próximos confrontos da FURIA.
- `/jogadores` — Lista os jogadores atuais da equipe.
- `/help` — Mostra todos os comandos disponíveis.
- Mensagens livres com o nome da FURIA também geram respostas automáticas.

## 📌``Demonstração``

➡️ Você pode conversar com o bot diretamente pelo Telegram:
[🔗 Clique aqui para testar o bot](https://t.me/**SEU_USERNAME_DO_BOT**)

> *(Substitua pelo @ do seu bot real no Telegram)*

## ⚙️``Tecnologias Utilizadas``

- Python 3.10+
- Biblioteca [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot)
- Hospedado em [PythonAnywhere](https://www.pythonanywhere.com/)

## 🧠``Motivação``

Este projeto foi desenvolvido como parte do meu portfólio pessoal, unindo minha paixão por programação e e-sports. É também uma forma de explorar integrações com APIs e bots de mensageria.

## 📂``Como rodar localmente``

1. Clone o repositório:
```bash
git clone https://github.com/amilcire/meubot_teamfuria.git
cd meubot_teamfuria 
```

2. Crie um ambiente virtual e ative:
- **Windows**:
```bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  
# No Windows: venv\Scripts\activate
````
 - **Linux/Mac**:

        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `config.py` com o seu **Token** do Bot (obtido no BotFather) e insira-o na variável `TOKEN`.

5. Execute o bot:

    ```bash
    python bot.py
    ```

### Comandos do Bot

- `/start`: Começa a interação com o bot.
- `/proximosjogos`: Mostra os próximos jogos da FURIA.
- `/jogadores`: Exibe a lista de jogadores da FURIA.
- `/ultimosjogos`: Exibe os últimos jogos e resultados da FURIA.
- `/noticias`: Mostra as últimas notícias sobre a FURIA.
- `/estatistica`: Exibe estatísticas do time FURIA.
- `/help`: Exibe a ajuda do bot.

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch para suas alterações: `git checkout -b feature/nova-funcionalidade`
3. Faça o commit das suas alterações: `git commit -m 'Adiciona nova funcionalidade'`
4. Envie para o repositório remoto: `git push origin feature/nova-funcionalidade`
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
