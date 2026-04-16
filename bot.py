import random
import os
import discord
from discord.ext import commands

def run_discord_bot():

  TOKEN = os.environ.get(DISCORD_BOT_TOKEN) #Put your token in an enviorment variable
  
  intents = discord.Intents.default()
  intents.message_content= True
    
  client = discord.Client(intents=intents)
  
  @client.event
  async def on_ready():
    print(f"{client.user}i)
  
  bot = commands.Bot(command_prefix="!" , intents=intents)
  
  banned_words = ["Fuck","Bitch","Shit"]
  
  Dad_jokes = [
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "why did the math book look so sad? Becuase it has too many problems!",
    "I only know 25 letters of the alphabet. I don't know y!",
    "why did the bike fall down? Because it was too tired!",
    "What do you call an American bee? A USB!",
    "what type of shoes do ninja's wear? Sneakers!",
    "What do you call a cute door? Adorable!",
    "what do you call a man with no body or nose? Nobody knows!",
    "what do you call an alligater that wants to be a detective? An investigater!",
  ]
  
  Roasts = [
    " I'd agree with yoy,but then we'd both be wromg.",
    "You're not stupid, you just have bad luck thinking.",
    "You bring everyone so much joy... when you leave.",
    "your'e like a cloud-when you disapear, it's a beautiful day.",
    "yo mama so old she knew Mr.clean when he had hair.",
    "yo mama so fat she's on both sides on the family.",
    "yo mama so stupid she went to the apple store to get a Big mac!"
    "yo mama so stupid she thought twitter was social media for birds!",
    "yo mama so fat she brouvght a spoon to the super bowl!",
  ]
  
  Riddles = [
    "The more you take the more you leave behind what am I? Footsteps.",
    " David's father has 3 sons: snap,crackle,and___? David.",
    " what is more useful when it's broken? An egg",
    " I'm easy to lift but hard to throw what am I? A feather.",
    " which fish costs the most? A goldfish.",
    " what goes up but never comes down? Age.",
    " A cowboy rode into town om friday.He stayed for 3 nights and outrode on friday.How is this possible? The horses name is Friday.",
    " What has a neck but no head? A bottle.",
    " whar 5 letteer word typed in all capital letters can be read the same upsidedown? SWIMS!",
  ]
  
  @bot.event
  async def on_ready():
      print(f"Logged in as {bot.user}")
  
  @bot.event

  aync def on_message(message):
    if content.startswith("Welcome"):
      await message.channel.send ("Whale hello there! Welcome to the sever")
      Joke = random.choice(Dad_jokes)  
      await message.channel.send(Joke)

    if content.startswith("Riddles"):
      Riddle= random.choice(Riddles)
      await message.channel.send(Riddle)
 
       
       
