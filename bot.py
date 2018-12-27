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

general1=discord.Embed(title="Příkazy pro všechny!",description="``>cat`` +Ukáže ti random obrázek kočki! :D",color = 0x304FFE)
general1.set_footer(text="Stránka 1")
general1.add_field(name=">dog",value = "Ukáže ti random pejska",inline=False)
general1.add_field(name=">server info",value = "Ukáže ti info o serveru",inline=False)
general1.add_field(name=">meme",value = "Ukáže tu random meme xD",inline=False)

general2=discord.Embed(title="Připravuje se",description="``>zkouska`` +Dostanes zkousku z neceho. (Pouzit 1x za 7 dni. **__PRIPRAVUJEME__**)",color=0x304FFE)
general2.set_footer(text="Stránka 2")

mod1=discord.Embed(title="Příkazy pro moderátory+!",description="``>warn`` +Varuje hráče! | ``>ban`` +Banuje uživatele! | ``>kick`` +Vyhodí uživatele!", color = 0xFF3D00)
mod1.set_footer(text="Stránka 1")

mod2=discord.Embed(title="Připravuje se!",description="--------------------",color=0xFF3D00)
mod2.set_footer(text="Stránka 2")

wrong1=discord.Embed(title="Špatně!",description="Správná odpověď byla 3! (12)",color=0xF0F0F0)
wrong2=discord.Embed(title="Špatně!",description="Správná odpověď byla 3! (12)",color=0xF0F0F0)
right3=discord.Embed(title="Správně!",description="Majiteli je 12! (aspon tak píše v #ownerinfo xd)",color=0xF0F0F0)
wrong4=discord.Embed(title="Špatně!",description="Správná odpověď byla 3! (12)",color=0xF0F0F0)

gen_cmd = (general1, general2)
  
mod_cmd = (mod1, mod2)

#wrong_answ = (worng1, wrong2, right3, wrong3, worng4)

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
      if reaction.emoji == '🅰':
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
      if reaction.emoji == '🔨':
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
  if reaction.message.server is None:
      if reaction.emoji == '0⃣':
          index = 0
          while True:
              msg = await client.send_message(user, embed=wrong1)
      if reaction.emoji == '1⃣':
          index = 0
          while True:
              msg = await client.send_message(user, embed=wrong2)
	
      if reaction.emoji == '2⃣':
          index = 0
          while True:
              msg = await client.send_message(user, embed=right3)
      if reaction.emoji == '3⃣':
          index = 0
          while True:
              msg = await client.send_message(user, embed=wrong4)
	
              
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
            embed.add_field(name = 'React 🔨 ',value ='Ukáže ti příkazy pro Moderátory!.',inline = False)
            embed.add_field(name = 'React 🅰 ',value ='Ukáže ti příkazy pro všechny.',inline = False)
            dmmessage = await client.send_message(message.author, embed=embed)
            reaction1 = '🔨'
            reaction2 = '🅰'
      
            await client.add_reaction(dmmessage, reaction1)
            await client.add_reaction(dmmessage, reaction2)
		
            await client.send_message(message.channel, '📨 Podívej se do PM pro více informací {}'.format(message.author.mention))
        #if message.content.upper() == ">ZKOUSKA":
        
    
           # author = message.author
         #   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            #embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
   #         embed.set_author(name='Jak dobre znas majitele?')
 #           embed.add_field(name = 'React 0⃣ ',value ='Pokud si myslíš že je majiteli 13.',inline = False)
        #    embed.add_field(name = 'React 1⃣ ',value ='Pokud si myslíš že je majiteli 10',inline=False)
   #         embed.add_field(name = 'React 2⃣', value = 'Pokud si myslíš že je majiteli 12',inline=False)
#            embed.add_field(name = 'React 3⃣', value = 'Pokid si myslíš že je majiteli 11',inline=False)
#            dmmessage = await client.send_message(message.author, embed=embed)
 #           reaction1 = '0⃣'
         #   reaction2 = '1⃣'
       #     reaction3 = '2⃣'
            #reaction4 = '3⃣'
        #    await client.add_reaction(dmmessage, reaction1)
   #         await client.add_reaction(dmmessage, reaction2)
#            await client.add_reaction(dmmessage, reaction3)
   #         await client.add_reaction(dmmessage, reaction4)
      #      await client.send_message(message.channel, '📨 Podívej se do PM pro více informací {}'.format(message.author.mention))
        if message.content.upper() == ">CAT":
            colour = '0x' + '008000'
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.reddit.com/r/cat/random") as r:
                    data = await r.json()
                    embed = discord.Embed(title='Random Kočička 🐈', description='z redditu', color=discord.Color(int(colour, base=16)))
                    embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                    embed.set_footer(text=f'Requested by: {message.author.display_name}', icon_url=f'{message.author.avatar_url}')
                    embed.timestamp = datetime.datetime.utcnow()
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper() == "TEST":
            embed = discord.Embed(title="Pokud si dostal reakce na message", description="tak se tesy povedl!", color=0x0FF0F0)
            rea1='📠'
            rea2='💾'
            rea3='🆕'
            await client.add_reaction(message, rea1)
            await client.add_reaction(message, rea2)
            await client.add_reaction(message, rea3)
            await client.send_message(message.channel, embed=embed)
        if message.content.upper() == ">NSFW":
           async with aiohttp.ClientSession() as session:
                async with session.get("https://hentaicloud.com/r/random") as r:
                    data = await r.json()
                    embed = discord.Embed(title="NSFW!!", description="No nelíbí se ti to?", color=0xEC407A)
                    embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                    embed.set_footer(text=f"Na žádost {message.author.display_name}", icon_url=f"{message.author.avatar_url}")
                    embed.timestamp = datetime.datetime.utcnow()
                    await client.send_message(message.channel, embed=embed)
	
        if message.content.upper() == ">DOG":
           colour = '0x' + '008000'
           async with aiohttp.ClientSession() as session:
               async with session.get("https://api.reddit.com/r/dog/random") as r:
                   data = await r.json()
                   embed = discord.Embed(title='Random Pejsek 🐕', description='z redditu', color=discord.Color(int(colour, base=16)))
                   embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                   embed.set_footer(text=f'Requested by: {message.author.display_name}', icon_url=f'{message.author.avatar_url}')
                   embed.timestamp = datetime.datetime.utcnow()
                   await client.send_message(message.channel, embed=embed)
		
     
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
		
       #if message.content.upper() == ">CAT":
             
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def warn(ctx):
	
     channel = discord.utils.get(client.get_all_channels(), name='dogisek-bot-logs')
    
     
     embed = discord.Embed(color = 0xB22222, title = "Člověk Varován")
     embed.add_field(name = "Člověk Varován", value = "{0}".format(userName), inline=False)
      
     embed.add_field(name = "Moderator", value = "{0}".format(ctx.message.author), inline=False)
     embed.add_field(name = "Důvod", value = "{0}".format(ctx.message), inline=False)
 
     await client.send_message(channel, embed=embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    channel = discord.utils.get(client.get_all_channels(), name='dogisek-bot-logs')
    embed = discord.Embed(title = "Kick", color = 0xFF4500)
    embed.add_field(name = "Moderator", value = "{0}".format(ctx.message.author), inline=False)
    embed.add_field(name = "Hráč", value= "{0}".format(user), inline=False)
    

    if user.server_permissions.kick_members:
        await client.send_message(message.channel, '**On/Ona je mod/admin a nemuzu ho/ji vyhodit!**')
        return
    
    try:
        await client.kick(user)
        await client.send_message(channel, embed=embed)
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
    channel = discord.utils.get(client.get_all_channels(), name='dogisek-bot-logs')
    embed = discord.Embed(title = "Ban", color = 0xFF4500)
    embed.add_field(name = "Moderator", value = "{0}".format(ctx.message.author), inline=False)
    embed.add_field(name = "User", value = "{0}".format(user), inline=False)
    
    if user.server_permissions.ban_members:
        await client.say('**On/ona je Mod/Admin a nemužu ji/ho zabanovat!!**')
        return

    try:
        await client.ban(user)
        await client.send_message(channel, embed=embed)

    except discord.Forbidden:

        await client.send_message(message.channel, 'Permission denied.')
        return
    except discord.HTTPException:
        await client.send_message(message.channel, 'ban se nepovedl :(.')
        return	
    
client.run(os.getenv("BOT"))
