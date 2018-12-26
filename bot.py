import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json

import aiohttp






client = commands.Bot(command_prefix = ">")

client.remove_command('help')

left = '⏪'
right = '⏩'

general1=discord.Embed(title="Příkazy pro všechny!",description="``>cat`` +Ukáže ti random obrázek kočki! :D | ``>dog`` + Ukáže ti random obrázek psa! :D | ``>server info`` + Ukáže ti info o serveru! | ``>meme`` + Ukáže ti random meme! xD",color = 0x304FFE)
general2=discord.Embed(title="Připravuje se",description="------------------",color=0x304FFE)
mod1=discord.Embed(title="Příkazy pro moderátory+!",description="``>warn`` +Varuje hráče! | ``>ban`` +Banuje uživatele! | ``>kick`` +Vyhodí uživatele!", color = 0xFF3D00)
mod2=discord.Embed(title="Připravuje se!",description="--------------------",color=0xFF3D00)

gen_cmd = (general1, general2)
  
mod_cmd = (mod1, mod2)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Řekni Dogisek Bot do chatu!"))
    print("The bot is online and connected with Discord!") 
   # await client.send_message(channel, "``Jsem tu a připraven!!``")
    
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await client.send_message(user, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await client.send_message(user, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)

@client.event
async def on_message(message):
         
	
	
        if message.content.upper() == "DOGISEK BOT":
            embed = discord.Embed(title = "Zdásemi že potřebuješ radu!", color = 0x311B92)
            embed.add_field(name = "Prefix:",value=">",inline=True)
            embed.add_field(name="Pro lepší pomoc kontaktuj:",value="@JustNela#6666",inline=True)
            embed.set_thumbnail(url = message.author.avatar_url)
            embed.set_footer(text = "Na žádost {}".format(message.author), icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)
        if message.content.upper() == ">HELP":
        
    
            author = message.author
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Potřebuješ pomoc?')
            embed.add_field(name = 'React 🇲 ',value ='Ukáže ti příkazy pro Moderátory!.',inline = False)
            embed.add_field(name = 'React 🇬 ',value ='Ukáže ti příkazy pro všechny.',inline = False)
            dmmessage = await client.send_message(message.author, embed=embed)
            reaction1 = '🇲'
            reaction2 = '🇬'
      
            await client.add_reaction(dmmessage, reaction1)
            await client.add_reaction(dmmessage, reaction2)
            await client.send_message(message.channel, '📨 Podívej se do PM pro více informací {}'.format(message.author.mention))
        
     
        if message.content.upper() == ">SERVER INFO":
      
          server = message.server
          roles = [x.name for x in server.role_hierarchy]
          role_length = len(roles)
          if role_length > 50: #Just in case there are too many roles...
              roles = roles[:50]
              roles.append('>>>> Displaying[50/%s] Roles'%len(roles))
          roles = ', '.join(roles);
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
          embed = discord.Embed(name="Informace o serveru {}".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_thumbnail(url = server.icon_url)
          embed.add_field(name="Jmeno Serveru", value=server.name, inline=True)
          embed.add_field(name="Owner", value=server.owner.mention)
          embed.add_field(name="Server ID", value=server.id, inline=True)
          embed.add_field(name="Role", value=len(server.roles), inline=True)
          embed.add_field(name="Kolik tu je hráčů?", value=len(server.members), inline=True)
          embed.add_field(name="Online", value=f"**{online}/{len(server.members)}**")
          embed.add_field(name="Server vytvořen", value=server.created_at.strftime("%d %b %Y %H:%M"))
          embed.add_field(name="Emoji", value=f"{len(server.emojis)}/100")
          embed.add_field(name="Server Region", value=str(server.region).title())
          embed.add_field(name="Total Channels", value=len(server.channels))
          embed.add_field(name="AFK Channel", value=str(server.afk_channel))
          embed.add_field(name="AFK Timeout", value=server.afk_timeout)
          embed.add_field(name="Verification Level", value=server.verification_level)
          embed.add_field(name="Role {}".format(role_length), value = roles)
          await client.send_message(message.channel, embed=embed)
        if message.content.upper() == ">MEME":
          colour = '0x' + '008000'
          async with aiohttp.ClientSession() as session:
              async with session.get("https://api.reddit.com/r/me_irl/random") as r:
                  data = await r.json()
                  embed = discord.Embed(title='Random Meme', description='z redditu', color=discord.Color(int(colour, base=16)))
                  embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                  embed.set_footer(text=f'Requested by: {message.author.display_name}', icon_url=f'{message.author.avatar_url}')
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(message.channel, embed=embed)
		
@client.command(pass_context=True)
async def warn(ctx):
	channel = discord.utils.get(client.get_all_channels(), name='warny-od-botu')
    
    
        embed = discord.Embed(color = 0xB22222, title = "Člověk Varován")
        embed.add_field(name = "Člověk Varován", value = "{0}".format(userName), inline=False)
        embed.add_field(name = "Moderator", value = "{0}".format(ctx.message.author), inline=False)
        embed.add_field(name = "Důvod", value = "{0}".format(ctx.message), inline=False)
 
        await client.send_message(channel, embed=embed)
   else:
        await client.send_message(message.channel, "Nemáš práva!")
               
client.run(os.getenv("BOT"))
