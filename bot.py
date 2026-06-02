import discord
from discord.ext import commands
from python_aternos import Client

# Initialize Discord Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize Aternos Client (Replace with your actual Aternos credentials)
# Note: Using your password directly can trigger captcha issues. 
# Advanced setups extract the ATERNOS_SESSION cookie instead.
atclient = Client()
atclient.login('YOUR_ATERNOS_USERNAME', 'YOUR_ATERNOS_PASSWORD')
aternos_server = atclient.list_servers()[0] # Selects your first server

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def status(ctx):
    """Checks if the server is online or offline."""
    aternos_server.fetch() # Refresh server status
    await ctx.send(f"The server is currently: **{aternos_server.status}**")

@bot.command()
async def startserver(ctx):
    """Attempts to start the server."""
    try:
        aternos_server.start()
        await ctx.send("Starting the Aternos server! It may take a few minutes if there is a queue.")
    except Exception as e:
        await ctx.send(f"Could not start server. Error: {e}")

# Run the Discord Bot (Replace with the token from Step 1)
bot.run('YOUR_DISCORD_BOT_TOKEN')