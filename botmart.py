import discord
import asyncio
import sys

sys.path.append('./bots')
import fleek
from fleek import *
import kilo
from kilo import *

sys.path.append('./groups')
import cookology
from cookology import *
import alerts
from alerts import *
import northcop
from northcop import *
import resellaio
from resellaio import *

token = 'YOUR TOKEN HERE'
client = discord.Client()

@client.event
async def on_ready():
	print('----------')
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('----------')

@client.event
async def on_message(message):
	if message.content.startswith('!help'):
		embed = discord.Embed(title="Help", url="https://botmart.io/", color=0x000000)
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1267863044945838081/n6LkbAGd_400x400.jpg")
		embed.add_field(name="Commands:", value="!fleek\n!kilo\n!resellaio\n!northcop\n!alerts\n!cookology")
		embed.set_footer(text="Created by @Aqyl_")
		await message.channel.send(embed=embed)
	if message.content.startswith('!fleek'):
		embed = discord.Embed(title="{}".format(name), url="https://botmart.io/product-details/fleek14065", description="{}".format(description), color=0x00E5FF)
		embed.set_thumbnail(url="{}".format(picture))
		embed.add_field(name="Supports:", value=f"{' | '.join([x for x in supports])}", inline=False)
		embed.add_field(name="Lowest Ask (Lifetime):", value="${}".format(lifetime), inline=False)
		embed.add_field(name="Lowest Ask (Renewal):", value="${}".format(lowestask), inline=False)
		embed.set_footer(text="@{} | Created by @Aqyl_".format(twitter))
		await message.channel.send(embed=embed)
	if message.content.startswith('!kilo'):
		embed = discord.Embed(title="{}".format(name1), url="https://botmart.io/product-details/kilo11635", description="{}".format(description1), color=0x000000)
		embed.set_thumbnail(url="{}".format(picture1))
		embed.add_field(name="Supports:", value=f"{' | '.join([x for x in supports1])}", inline=False)
		# embed.add_field(name="Lowest Ask (Lifetime):", value="${}".format(lifetime1), inline=False)
		embed.add_field(name="Lowest Ask (Renewal):", value="${}".format(lowestask1), inline=False)
		embed.set_footer(text="@{} | Created by @Aqyl_".format(twitter1))
		await message.channel.send(embed=embed)
	if message.content.startswith('!cookology'):
		embed = discord.Embed(title="{}".format(name2), url="https://botmart.io/product-details/cookology04688", description="{}".format(description2), color=0x7051C6)
		embed.set_thumbnail(url="{}".format(picture2))
		embed.add_field(name="Supports:", value=f"{' | '.join([x for x in supports2])}", inline=False)
		embed.add_field(name="Lowest Ask (Renewal):", value="${}".format(lowestask2), inline=False)
		embed.set_footer(text="@{} | Created by @Aqyl_".format(twitter2))
		await message.channel.send(embed=embed)
	if message.content.startswith('!alerts'):
		embed = discord.Embed(title="{}".format(name3), url="https://botmart.io/product-details/alerts86061", description="{}".format(description3), color=0x5DB4CA)
		embed.set_thumbnail(url="{}".format(picture3))
		embed.add_field(name="Supports:", value=f"{' | '.join([x for x in supports3])}", inline=False)
		embed.add_field(name="Lowest Ask (Renewal):", value="${}".format(lowestask3), inline=False)
		embed.set_footer(text="@{} | Created by @Aqyl_".format(twitter3))
		await message.channel.send(embed=embed)
	if message.content.startswith('!northcop'):
		embed = discord.Embed(title="{}".format(name4), url="https://botmart.io/product-details/thenorthcop67022", description="{}".format(description4), color=0xDF1414)
		embed.set_thumbnail(url="{}".format(picture4))
		embed.add_field(name="Supports:", value=f"{' | '.join([x for x in supports4])}", inline=False)
		embed.add_field(name="Lowest Ask (Renewal):", value="${}".format(lowestask4), inline=False)
		embed.set_footer(text="@{} | Created by @Aqyl_".format(twitter4))
		await message.channel.send(embed=embed)
	if message.content.startswith('!resellaio'):
		embed = discord.Embed(title="{}".format(name5), url="https://botmart.io/product-details/resell-aio20373", description="{}".format(description5), color=0x299DF3)
		embed.set_thumbnail(url="{}".format(picture5))
		embed.add_field(name="Supports:", value=f"{' | '.join([x for x in supports5])}", inline=False)
		embed.add_field(name="Lowest Ask (Lifetime):", value="${}".format(lifetime2), inline=False)
		embed.add_field(name="Lowest Ask (Renewal):", value="${}".format(lowestask5), inline=False)
		embed.set_footer(text="@{} | Created by @Aqyl_".format(twitter5))
		await message.channel.send(embed=embed)
client.run(token)