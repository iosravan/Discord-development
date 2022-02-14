import discord
import numpy as np
import tensorflow as tf

class Meta:
  """ 
  To create a personalised bot for discord 
  requirements:
        collect words, used phrases to auto reply
        
  """
  pass
  
print(help(Meta))

client = discord.Client()
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
  pass
