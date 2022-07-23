import discord
from discord.ext import commands
import random
from discord.utils import get
from discord.ext.commands import bot
import os
import requests
comms = 0
Blahajfoto = os.path.join(os.getcwd(), "Blahajfoto")

client = commands.Bot(command_prefix = ["haj ", "Haj "])
client.remove_command("help")

@client.event
async def on_ready():
    print("Working")
    

@client.command()
async def blahaj(ctx):
    global comms
    filenames = os.listdir(Blahajfoto)
    selected_file = os.path.join(Blahajfoto, random.choice(filenames))
    embed = discord.Embed(title="Blåhaj!", description="Here is your Blåhaj", color=0x5866ef)
    embed.set_image(url="attachment://blahaj.png")
    await ctx.send(file=discord.File(selected_file, "blahaj.png"), embed=embed)
    comms = comms + 1


@client.command()
async def howgay(ctx):
    global comms
    howgayp = random.randint(1,101)
    await ctx.send(f"Blåhaj says you are {howgayp}% homosexual!")
    comms = comms + 1

@client.command()
async def quote(ctx):
    global comms
    await ctx.send(random.choice(requests.get("https://raw.githubusercontent.com/PoggerCat/quote/main/alfieisberystopid").text.split("\n")))
    comms = comms + 1

@client.command()
async def help(ctx):
    global comms
    embed = discord.Embed(title = "halp ples", colour=0x5866ef)
    
    embed.add_field(name = "blahaj", value = "Sends a random photo of Blåhaj")
    embed.add_field(name = "howgay", value = "Makes Blåhaj tell you how gay you are")
    embed.add_field(name = "quote", value = "Makes Blåhaj pick a random useless quote from a list")
    embed.add_field(name = "lovetoshi", value = "Express our love for our favourite catboy!")
    embed.add_field(name = "uses", value = "Shows how many commands have been used in total! (resets when bot restarts)")
    embed.add_field(name = "suggestions", value = "writes the message after into a text file for suggestions!")
    embed.add_field(name = "cheese", value = "Send a random phot of cheese (I hate you hoiboi)")
    await ctx.send(embed = embed)
    comms = comms + 1

@client.command()
async def lovetoshi(ctx):
    global comms
    await ctx.send("We love you Toshi!!!!")
    comms = comms + 1


@client.command()
async def uses(ctx):
    global comms
    await ctx.send(f"{comms} commands have been used!")
    comms = comms + 1

@client.command()
async def suggestions(ctx, *, suggestions):
    await ctx.send("suggestion noted!")
    open("suggestions.txt", "ab").write(f"""{suggestions}
    """.encode("utf-8"))

@client.command()
async def cheese(ctx):
    r = requests.get("https://cheesepics.xyz/api")
    if (r.status_code == 200):
        cheese_id = r.json()["ID"]
        cheese_author = r.json()["author"]
        cheese_license = r.json()["license"]
        cheese_embed = discord.Embed(title="Cheese (go away hoiboi)", color=discord.Color.gold())
        cheese_embed.set_image(url=f"https://cheesepics.xyz/images/cheese/{cheese_id}")
        cheese_embed.set_footer(text=f"Lmao the guy that made it was {cheese_author}, they did the licency thing by {cheese_license}")
        await ctx.send(embed=cheese_embed)
    else:
        await ctx.send("hoiboi did a fucky wucky")



    
    


    
client.run("
