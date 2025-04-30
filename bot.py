from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, ContextTypes, CallbackQueryHandler
import nest_asyncio
nest_asyncio.apply()
from telegram.ext import filters 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



# Meu token do BOTFATHER
TOKEN = "7841443022:AAEOKPA4b0h5ZVMcvkl7zLHsgO_C45U07ZM"
   
    # Função para retornar ao menu 
def menu_principal():
    keyboard = [
        [InlineKeyboardButton("Próximos jogos", callback_data='proximos_jogos'),
         InlineKeyboardButton("jogadores", callback_data='jogadores')],
        [InlineKeyboardButton("Últimos jogos", callback_data='ultimos_jogos'),
         InlineKeyboardButton('Notícias', callback_data='noticias')],
        [InlineKeyboardButton("Estatísticas", callback_data='estatistica'),
         InlineKeyboardButton("🔥 Ao Vivo", callback_data='ao_vivo')],
        [InlineKeyboardButton("Campeonatos🔥", callback_data='campeonatos')]
    ]
    return InlineKeyboardMarkup(keyboard)
    
    # Função para iniciar o chat, com mensagem de boas vindas
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Próximos jogos",callback_data='proximos_jogos'),
            InlineKeyboardButton("jogadores",callback_data='jogadores')
        ],
        [
            InlineKeyboardButton("Últimos jogos",callback_data='ultimos_jogos'),
            InlineKeyboardButton('Notícias',callback_data='noticias')
        ],
        [
            InlineKeyboardButton("Estatísticas",callback_data='estatistica'),
            InlineKeyboardButton("🔥 Ao Vivo",callback_data='ao_vivo')
        ],
        [   InlineKeyboardButton("Campeonatos🔥",callback_data='campeonatos')

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔥Faaala, FURIOSO Fan! Seja bem-vindo!\n Escolha uma opção abaixo:", reply_markup=reply_markup)
    
    # Função para lidar com os botões 
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    if query.data == 'proximos_jogos':
        await query.edit_message_text(text="Aqui estão os próximos jogos da FURIA!")
    elif query.data == 'jogadores':
        await query.edit_message_text(text="Aqui está a lista de jogadores da FURIA!")
    elif query.data == 'ultimos_jogos':
        await query.edit_message_text(text="Aqui estão os últimos jogos da FURIA!")
    elif query.data == 'noticias':
        await query.edit_message_text(text='Últimas notícias da FURIA')
    # Função para mostrar os proximos jogos
async def proximos_jogos(update, context): 
    link_proximos_jogos = "https://draft5.gg/equipe/330-FURIA/proximas-partidas" 
    keyboard =[
       [InlineKeyboardButton("VEJA OS PRÓXIMOS JOGOS",url=link_proximos_jogos)],
       [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text="Aqui estão os próximos jogos da FURIA:\n",reply_markup=reply_markup)

    # Função para mostrar os jogadores
async def jogadores(update: Update, context):
    jogadores_furia = [
        """*Line-up Titular*
        🇰🇿 MOLODOY\n
        🇱🇻 YEKINDAR\n
        🇧🇷 FalleN\n
        🇧🇷 KSCERATO\n
        🇧🇷 yuurih\n
        
        *Reservas*\n
        🇧🇷 skullz\n
        🇧🇷 chelo"""
    ]
    keyboard =[
     [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]
    ]
    jogadores_text = "\n".join(jogadores_furia)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(f"Aqui estão os jogadores da FURIA:\n{jogadores_text}",reply_markup=InlineKeyboardMarkup(keyboard))
    
    # Função para responder quando o fã enviar mensagens relacionadas a FURIA
async def resposta_generica(update: Update, context):
    await update.message.reply_text("FURIA é vida! 🔥 Vamos FURIA!")
    
    # Função para mostrar ultimos jogos do time FURIA
async def ultimos_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link_resultado = "https://draft5.gg/equipe/330-FURIA/resultados"
    keyboard =[
       [ InlineKeyboardButton("CONFIRA AGORA🔥",url=link_resultado)],
       [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]
    ]

    reply_markup=InlineKeyboardMarkup(keyboard)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text="Aqui estão os últimos jogos e resultados da FURIA:\n",reply_markup=reply_markup)
    
    # Função para mostrar os próximos campeonatos
async def campeonatos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link_campeonato = "https://draft5.gg/equipe/330-FURIA/campeonatos"
    keyboard =[
       [InlineKeyboardButton("CLIQUE AQUI PARA CONFERIR!🔥",url=link_campeonato)],
       [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text="Aqui estão os próximos campeonatos:\n",reply_markup=reply_markup)
    # Função para ultimas noticias da FURIA
async def noticias(update: Update,context):
    texto = """
  📰  <b> Últimas notícias da FÚRIA</b>\n
1. <a href="https://www.furia.gg/news/furia-vence-torneio">FURIA vence o último torneio!</a>
2. <a href="https://www.furia.gg/news/classificados-para-o-major">FURIA se classifica para o Major de CS!</a>
3. <a href="https://www.furia.gg/news/novo-jogador-anunciado">Novo jogador se junta à FURIA!</a>           
"""
    keyboard = [
    [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]
    ]
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=texto, parse_mode="HTML",reply_markup=InlineKeyboardMarkup(keyboard))
    # Função para Estatísticas do TIME
async def estatistica(update: Update, context):
    texto = """
📊 <b>Estatísticas da FURIA (HLTV)</b>

🔹 Ranking atual: <b>#16</b>
🔹 Ranking mais alto: <b>#3</b>
🔹 Winrate com coach atual (sidde): <b>49%</b>
🔹 Idade média do time: <b>26 anos</b>

👥 <b>Jogadores (Rating HLTV)</b>
• KSCERATO - Rating: 1.19 | Mapas: 1310
• yuurih - Rating: 1.17 | Mapas: 1335
• FalleN - Rating: 1.01 | Mapas: 309
• Chelo  - Rating: 1.00 | Mapas: 309
• Skullz - Rating: 0.99 | Mapas: 140
Fonte: <a href="https://www.hltv.org/team/8297/furia">HLTV.org</a>
"""
    keyboard = [[InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]]
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=texto, parse_mode="HTML",reply_markup=InlineKeyboardMarkup(keyboard))

    # Função para tratar o /help (ajuda)
async def ao_vivo(update: Update,context):
    link_ao_vivo =  "https://www.twitch.tv/furia"
    link_site_oficial = "https://www.furia.gg/"
    keyboard = [
        [ InlineKeyboardButton("🔥 ASSISTIR AGORA!🔥",url=link_ao_vivo),
          InlineKeyboardButton("Site OFICIAL!🔥",url=link_site_oficial)         
        ],
        [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_menu")]
]
            
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text="Clique no botão abaixo para acompanhar a FURIA ao vivo!", reply_markup=reply_markup)
async def help(update: Update, context):
    await update.message.reply_text("Comandos disponíveis:\n"
                                    "/start - Saudar\n"
                                    "/proximosjogos - Ver próximos jogos\n"
                                    "/jogadores - Ver jogadores da FURIA\n"
                                    "/help - Ver essa ajuda")
async def voltar_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    try:
        await query.edit_message_text(
            text="🔥Faaala, FURIOSO Fan! Escolha uma opção abaixo:",
            reply_markup=menu_principal()
        )
    except Exception as e:
        # Se não for possível editar, envia uma nova mensagem
        await query.message.reply_text(
            "🔥Faaala, FURIOSO Fan! Escolha uma opção abaixo:",
            reply_markup=menu_principal()
        )

async def main():
    # Criação do bot com o token
    application = Application.builder().token(TOKEN).build()

    # Criação do comando
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    #   handlers ao bot
    application.add_handler(CallbackQueryHandler(proximos_jogos,pattern='proximos_jogos'))
    application.add_handler(CallbackQueryHandler(noticias,pattern='noticias'))
    application.add_handler(CallbackQueryHandler(estatistica,pattern='estatistica'))
    application.add_handler(CallbackQueryHandler(ao_vivo,pattern='ao_vivo'))
    application.add_handler(CallbackQueryHandler(jogadores,pattern='jogadores'))
    application.add_handler(CallbackQueryHandler(ultimos_jogos,pattern='ultimos_jogos'))
    application.add_handler(CallbackQueryHandler(campeonatos,pattern='campeonatos'))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CallbackQueryHandler(voltar_menu, pattern='voltar_menu'))
    application.add_handler(CallbackQueryHandler(button))


    # Um handler para capturar mensagens
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, resposta_generica))


    
    # Iniciar o polling
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


