import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_ID = '1136522954105163816'
CHANNEL_ID = int('1134168460214153238')
MESSAGE_ID = int('1138679451425706096')
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

bot.run('TOKEN')
