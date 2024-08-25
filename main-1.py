import discord
from discord.ext import commands
import openai

openai.api_key = "api key"


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():   
    print(f'prazer sou {bot.user.name}')

@bot.command(name="gpt")
async def ask_question(ctx, *, question):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=question,
        max_tokens=100
    )

    answer = response.choices[0].text.strip()

    await ctx.send(answer)


@bot.command(name="start")
async def start(ctx):
    await ctx.send('Estou aqui, pronto para lhe servir!')

@bot.command(name="cachorro")
async def imagem(ctx):
    embed= discord.Embed(
        title="Esse é um Cachorro",
        description="O golden retriever é uma raça canina do tipo retriever originária da Grã-bretanha, e foi desenvolvida para a caça de aves aquáticas. ",
        color=discord.Color.blue()
    )

    embed.set_image(url="https://github.com/campoix/banco-de-imagens/blob/main/1200px-Goldensondika.jpg?raw=true")

    await ctx.send(embed=embed)

@bot.command(name="gato")
async def imagem(ctx):
    embed= discord.Embed(
        title="Esse é um gato",
        description="os gatinhos sao fofos S2",
        color=discord.Color.blue()
    )

    embed.set_image(url="https://github.com/campoix/banco-de-imagens/blob/main/e478854320a9f35efb15a9b19e64a98d.jpg?raw=true")

    await ctx.send(embed=embed)
    
bot.run("token")
