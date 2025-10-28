#Para começar a programar o bot eu vou usar uma API, e para usar esse API, preciso instalar uma biblioteca para comunicação entre o bot e o Discord (para isso, eu codei = py -m pip install discord.py)

import os
from dotenv import load_dotenv
load_dotenv()

import discord #importar todo o conteudo da API do Discord
from discord.ext import commands, tasks
from datetime import time

intents = discord.Intents.all() #Guardando todas as permissões que o bot usa pra funcionar
bot = commands.Bot(".", intents=intents) #Objeto com todas as propriedades do meu bot, depois no intents eu passo todas as informações que eu quero acessar para intents 'suas permissões são as permissões definidas'

#-------------------------EVENTOS------------------------------------
@bot.event
async def on_ready():
    sincs = await bot.tree.sync() # variavel que inicia os comandos sincronizados
    print(f"{len(sincs)} Comandos sincronizados") #contador de comandos sincronizados
    print("Bot inicializado com sucesso!!!") #🔝 Define uma função, e add um evento, e on_ready - quando o bot estiver ready ele run a function e printa
    enviar_mensagem_teste.start()
    enviar_mensagem_manha.start()
    enviar_mensagem_noite.start() #INICIANDO A TASK, TASKS PRECISAM SER INICIALIZADAS
    

# @bot.event (LER A MENSAGEM E DE ONDE ELA VEIO)
# async def on_message(msg:discord.Message): #o msg é o obj mensagem que o usuario envia
#     if msg.author.bot:
#         return # aqui eu verifico que se a msg vier de algum bot ele vai encerrar a funcao usando return, se não for bot, ele vai executar o await
#     await msg.reply(f"Nova Mensagem do Usuário: {msg.author.mention} \n Canal: {msg.channel.name}") # Aqui eu uso o .mention no lugar do .name pra ele mencionar o nome do Usuário, acho mais util

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1432471524257955870) #Bot pegando o id do canal e guardando na var CANAL
    await canal.send(f"{membro.mention} Entrou no servidor \nUse o comando .comandos para ver comandos disponiveis") # usando a var pra mandar uma mensagem

@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f"{membro.name} reagiu a mensagem com {reacao.emoji}")



#-------------------------COMANDOS------------------------------------
@bot.command()
async def comandos(ctx:commands.Context):
    await ctx.send('--------COMANDOS DO BOT----------\n' 
                   'COMANDO .ola - Sauda o usuario \n' 
                   'COMANDO .falar - repete a frase que o usuario digitou \n' 
                   'COMANDO .duasMensagens - repete as duas mensagens do usuario \n' 
                   'COMANDO .somar - soma os numeros digitados pelo usuario \n')

@bot.command()
async def ola(ctx:commands.Context): #ctx = contexto, e depois eu digo pra ele que eu estou colocando o comando para ele analisar contexto, quem enviou, em qual canal, etc...
    nome = ctx.author.name #Aqui eu armazeno na var nome, o nome do autor do contexto, ou seja, eu falo pra ele pegar o nickname do autor da msg em contexto
    await ctx.reply(f'Ola, {nome}!!! Tudo bem??') #await = aguarda a entrada do user / ctx.reply = ele vai pegar o contexto do que o usuario digitou e reply(ou posso usar o send, mas a diferença é que com reply ele seleciona a mensagem e responde, por ser um servidor com mais gente, é melhor o reply) o que eu mandar, no caso 'Ola, tudo bem'... Uso o F antes da string pra concatenar variavel com string fixa.

@bot.command()
async def falar(ctx:commands.Context, *,texto): #aqui ele esta pegando o que eu mando pra ele, armazena em 'texto' e me manda de novo, perceba que ele me envia(send), não responde(reply), e uso o * antes do texto pra fazer com que ele pegue todas as palavras digitadas
    await ctx.send(texto)

@bot.command()
async def duasMensagens(ctx:commands.Context, mensagem1, mensagem2):
    await ctx.send(mensagem1)
    await ctx.send(mensagem2)

@bot.command()#calculadora basica
async def somar(ctx:commands.Context, num1:float, num2:float):
    resultadoSoma = num1 + num2
    await ctx.reply(f'O resultado da sua soma é = {resultadoSoma}')

@bot.command()
async def enviar_embed(ctx:commands.Context): #Embed é aquela mensagem com fundo bonitinha com tudo incorporado (Embed = incorporado)
    minha_embed = discord.Embed()
    minha_embed.title = "Titulo"
    minha_embed.description = "Descricao"

    imagem = discord.File("imgs\hello-world.png", "hw.png") #atribuindo a imagem na VAR imagem
    minha_embed.set_image(url="attachment://hw.png") #imagem grande
    minha_embed.set_thumbnail(url="attachment://hw.png") #Thumb pequena

    minha_embed.set_footer(text="Footer")

    minha_embed.set_author(name=ctx.author.name)

    await ctx.reply(embed=minha_embed, file=imagem)

#-------------------------SLASH COMMANDS------------------------------------
@bot.tree.command()
async def ola2(interact:discord.Interaction):
    await interact.response.send_message(f"Olá, {interact.user.name}!!!")
    # após o fechamento das aspas duplas, mas ainda dentro dos parenteses, eu posso colocar o termo ephemeral=true, isso significa que só quem vai ver a mensagem é quem mandou o comando

@bot.tree.command()
async def falar2(interact:discord.Interaction, texto:str):
    await interact.response.send_message(texto)

@bot.tree.command()
async def somar2(interact:discord.Interaction, num3:int, num4:int):
    resultadoSoma2 = num3 + num4
    await interact.response.send_message(f"resultado da soma: {resultadoSoma2}")

@bot.tree.command()
async def selecionar_membro(interact:discord.Interaction, membro:discord.Member):
    await interact.response.send_message(f"Membro selecionado: {membro.mention}")

#-------------------------TASKS------------------------------------
@tasks.loop(seconds=0.5)
async def enviar_mensagem_teste():
    canal = bot.get_channel(1174937371104514060)
    await canal.send("TESTEEEEEEEE")

@tasks.loop(time=time(21, 0, 0))
async def enviar_mensagem_noite():
    canal = bot.get_channel(1174937371104514060) #Bot pegando o id do canal e guardando na var CANAL
    await canal.send("BOA NOITEEEE🌕🌚")

@tasks.loop(time=time(11, 0, 0))
async def enviar_mensagem_manha():
    canal = bot.get_channel(1174937371104514060) #Bot pegando o id do canal e guardando na var CANAL
    await canal.send("Bom Dia ⛅⛅")







#-----------------------FINAL-------------------------------------
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN) 
#ULTIMO LINHA DO CODIGO, pois é quem executa meu bot, então ele precisa ler todo o código antes de iniciar