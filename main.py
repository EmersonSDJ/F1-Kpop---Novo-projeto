import discord
from discord.ext import commands
import os

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Configuração do bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🌐 {len(synced)} comandos de barra sincronizados.")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

# Exemplo de comando de barra
@bot.tree.command(name="ping", description="Verifica a latência do bot.")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! Latência: {latency}ms")

# Rodar o bot
bot.run(os.getenv("DISCORD_TOKEN"))
