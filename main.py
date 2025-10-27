#Para começar a programar o bot eu vou usar uma API, e para usar esse API, preciso instalar uma biblioteca para comunicação entre o bot e o Discord (para isso, eu codei = py -m pip install discord.py)

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
async def ola(ctx): #ctx = advinha ? contexto
    await ctx.reply('Ola, Tudo bem??') #await = aguarda a entrada do user / ctx.reply = ele vai pegar o contexto do que o usuario digitou e reply o que eu mandar, no caso 'Ola, tudo bem'

#-----------------------FINAL-------------------------------------
bot.run("-----------------------------------------------------") #ULTIMO LINHA DO CODIGO, pois é quem executa meu bot, então ele precisa ler todo o código antes de iniciar