import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_ID = '1171113887865765968'
CHANNEL_ID = int('1134168460214153238')
MESSAGE_ID = int('1171116141792477186')
REACTION_EMOJI = '✅'

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready.')
    channel = bot.get_channel(CHANNEL_ID)
    message = await channel.fetch_message(MESSAGE_ID)
    await message.add_reaction(REACTION_EMOJI)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != MESSAGE_ID:
        return
    
    if str(payload.emoji) == REACTION_EMOJI:
        guild = discord.utils.get(bot.guilds, id=payload.guild_id)
        role = discord.utils.get(guild.roles, id=int(ROLE_ID))
        member = discord.utils.get(guild.members, id=payload.user_id)
        
        await member.add_roles(role)
      
my_secret = os.environ['TOKEN']
bot.run(my_secret)

