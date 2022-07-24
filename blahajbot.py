# Import packages
import os
import random
import signal
import discord
import requests
from discord.ext import commands

# SIGINT handler
def signal_handler(signal, frame):
    # Log out the bot
    print("\nStopping Blahajbot")
    client.logout()
    client.close()

    # Save the comms variable
    with open("comms.txt", "w") as f:
        f.write(str(comms))

    # Exit
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Function to get the current amount of messages sent
def get_comms():
    # Create the file if it doesn't exist
    if not os.path.exists("comms.txt"):
        with open("comms.txt", "w") as f:
            f.write("0")

    # Get the amount of messages sent
    with open("comms.txt", "r+") as f:
        comms = f.read()
        if not comms:
            comms = 0
        else:
            comms = int(comms)

    # Return the amount of messages sent
    return comms

# Initialise variables
comms = get_comms()
Blahajfoto = os.path.join(os.getcwd(), "Blahajfoto")

# Initialise bot
client = commands.Bot(command_prefix=["haj ", "Haj "])
client.remove_command("help")


@client.event
async def on_ready():
    print("Started Blahajbot")


@client.command()
async def blahaj(ctx):
    global comms
    filenames = os.listdir(Blahajfoto)
    selected_file = os.path.join(Blahajfoto, random.choice(filenames))
    embed = discord.Embed(title="Blåhaj!", description="Here is your Blåhaj", color=0x5866ef)
    embed.set_image(url="attachment://blahaj.png")
    await ctx.send(file=discord.File(selected_file, "blahaj.png"), embed=embed)
    comms += 1


@client.command()
async def howgay(ctx):
    global comms
    howgayp = random.randint(1, 101)
    await ctx.send(f"Blåhaj says you are {howgayp}% homosexual!")
    comms += 1


@client.command()
async def quote(ctx):
    global comms
    await ctx.send(random.choice(requests.get("https://raw.githubusercontent.com/PoggerCat/quote/main/alfieisberystopid").text.split("\n")))
    comms += 1

@client.command()
async def piss(ctx):
    global comms
    await ctx.send(":pleading_face:")
    comms += 1

@client.command()
async def help(ctx):
    global comms
    embed = discord.Embed(title="halp ples", colour=0x5866ef)

    embed.add_field(name="blahaj", value="Sends a random photo of Blåhaj")
    embed.add_field(name="howgay", value="Makes Blåhaj tell you how gay you are")
    embed.add_field(name="quote", value="Makes Blåhaj pick a random useless quote from a list")
    embed.add_field(name="lovetoshi", value="Express our love for our favourite catboy!")
    embed.add_field(name="uses", value="Shows how many commands have been used in total!")
    embed.add_field(name="cheese", value="Send a random phot of cheese (I hate you hoiboi)")
    await ctx.send(embed=embed)
    comms += 1


@client.command()
async def lovetoshi(ctx):
    global comms
    await ctx.send("We love you Toshi!!!!")
    await ctx.send(":pleading_face:")
    comms += 1


@client.command()
async def uses(ctx):
    global comms
    await ctx.send(f"{comms} commands have been used!")
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers!")
    comms += 1




@client.command()
async def cheese(ctx):
    r = requests.get("https://cheesepics.xyz/api")
    if (r.status_code == 200):
        cheese_id = r.json()["ID"]
        cheese_author = r.json()["author"]
        cheese_license = r.json()["license"]
        cheese_embed = discord.Embed(
        title="Cheese (go away hoiboi)", color=discord.Color.gold())
        cheese_embed.set_image(url=f"https://cheesepics.xyz/images/cheese/{cheese_id}")
        cheese_embed.set_footer(text=f"Lmao the guy that made it was {cheese_author}, they did the licency thing by {cheese_license}")
        await ctx.send(embed=cheese_embed)
    else:
        await ctx.send("hoiboi did a fucky wucky")

# Start the bot
client.run("")
