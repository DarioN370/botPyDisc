#Para começar a programar o bot eu vou usar uma API, e para usar esse API, preciso instalar uma biblioteca para comunicação entre o bot e o Discord (para isso, eu codei = py -m pip install discord.py)

import os
from dotenv import load_dotenv
load_dotenv()

import discord #importar todo o conteudo da API do Discord
from discord.ext import commands

intents = discord.Intents.all() #Guardando todas as permissões que o bot usa pra funcionar
bot = commands.Bot(".", intents=intents) #Objeto com todas as propriedades do meu bot, depois no intents eu passo todas as informações que eu quero acessar para intents 'suas permissões são as permissões definidas'

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso!!!")
#🔝 Define uma função, e add um evento, e on_ready - quando o bot estiver ready ele run a function e printa

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

#-----------------------FINAL-------------------------------------
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN) 
#ULTIMO LINHA DO CODIGO, pois é quem executa meu bot, então ele precisa ler todo o código antes de iniciar