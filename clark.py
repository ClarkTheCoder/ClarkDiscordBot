import discord
import asyncio
import random
import pickle
import os
import time
import sys
from discord import Game

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

	#heads or tails
	if message.content.upper().startswith('!FLIP'):
		flip = random.choice(['heads', 'tails'])
		await client.send_message(message.channel, flip)

	#display thots NSFW (limited to only mods and admins)
	elif message.content.upper().startswith('!THOT'):
		if message.author.id == "140582689651687424" or message.author.id == "239907769317195777" or message.author.id == "166392135699005441" or message.author.id == "140374213042110464":
			thot = random.choice(['https://f4.bcbits.com/img/a4093565357_10.jpg', 'https://imgur.com/AJ1ybgC', ': https://cdn.discordapp.com/attachments/255678709393129472/373487680719421441/20446197_1489906441074593_1780441816_o.jpg', 
				'https://cdn.discordapp.com/attachments/255678709393129472/373486342153306112/19576202_1463637137034857_776903082_n.gif', ': https://giant.gfycat.com/AdolescentCandidCoypu.webm', 
				'http://i.imgur.com/NU5jC1l.jpg', 'https://cdn.discordapp.com/attachments/376887816581414922/376889614574813186/BOOTY.jpg',
				'http://naijaultimate.com/wp-content/uploads/2017/08/Nicki-Minaj-MTV.jpg', 'https://gfycat.com/DarlingInconsequentialAustralianshelduck',
				'https://cdn.discordapp.com/attachments/316399433736650752/351902439739490305/Nicki-Minaj-and-her-nipples-5.jpg', 
				'https://cdn.discordapp.com/attachments/316399433736650752/347940166658424843/16123113_1807447696139564_7777549271787634688_n.png', 'http://i.imgur.com/1RzCaQ9.jpg',
				'https://cdn.discordapp.com/attachments/316399433736650752/327319394294431744/20170621_222956.png', 'https://cdn.discordapp.com/attachments/316399433736650752/327319394294431744/20170621_222956.png',
				'https://cdn.discordapp.com/attachments/316399433736650752/336752102711885824/unknown.png', 'http://www.gotceleb.com/wp-content/uploads/photos/danielle-bregoli/out-for-lunch-in-beverly-hills/Danielle-Bregoli-out-for-lunch--02.jpg',
				'https://cdn.discordapp.com/attachments/316399433736650752/334875903387762688/fft20_mf5544431.png', 'https://cdn.discordapp.com/attachments/316399433736650752/334195557792743435/image.jpg',
				'http://s8.favim.com/610/150227/black-beauty-black-girls-cool-girl-Favim.com-2515598.jpg', 'https://i.imgur.com/4aiX25b.jpg', 'http://ic.pics.livejournal.com/dringen/63450085/20640/20640_600.jpg', 
				'https://i.imgur.com/0pgjkR2r.jpg', 'http://cdn2.cagepotato.com/wp-content/uploads/gallery/jennifer-nguyen/jennifer-nguyen-photos-sexy-ufc-ring-girl-01.jpg'])
			await client.send_message(message.channel, thot)
		else:
			await client.send_message(message.channel, "Sorry, you must be an admin or moderator to use that command OR have special permission.")


	#I do not associate with 
	elif message.content.upper().startswith('NIGGER'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Do NOT be racial on my server." % (userID))

	#quote someone and store all quotes in quote_file.pk1
	elif message.content.upper().startswith('!ADDQUOTE'):
		if not os.path.isfile("quote_file.pk1"):
			disc_quotes = []
		else:
			with open("quote_file.pk1", "rb") as quote_file:
				disc_quotes = pickle.load(quote_file) 
		disc_quotes.append(message.content[9:])
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Your quote has been added :D" % (userID))
		with open("quote_file.pk1", "wb") as quote_file:
			pickle.dump(disc_quotes, quote_file)

	#display quote from quote_file.pk1
	elif message.content.upper().startswith("!QUOTE"):
		with open("quote_file.pk1", "rb") as quote_file:
				disc_quotes = pickle.load(quote_file)
		await client.send_message(message.channel, random.choice(disc_quotes))


#changes playing message to greet the newest member	and sends a PM to whomever joined! 
@client.event
async def on_member_join(member):
    await client.change_presence(game=discord.Game(name='Hi %s' % (member)))
    await client.send_message(member, "Hi %s, Welcome to Clark's Discord Server! Clark's server is fairly NSFW; just a warning. Enjoy your stay :)" % (member))

#changes playing message to a good bye
@client.event
async def on_member_remove(member):
    await client.change_presence(game=discord.Game(name='Bye %s' % (member)))
	

#needed to run bot 
client.run('NDA2NjA5OTgzOTQyMTY0NDgw.DU7JXQ.myF4O104lZBGNYCsBLDeE9qQ6us')
