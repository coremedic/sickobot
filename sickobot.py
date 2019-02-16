#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SickoBot.py
#  
#  Copyright 2019 coremed <coremed@cryptolab.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



# Only works with Python 3.x use "python3 ..." to compile or run
import discord
import asyncio
import aiohttp
import time
import json 
import random
import urllib
import requests
import base64
import sys
import subprocess 
from art import *
from discord import Game
from discord.ext.commands import Bot

def figlet(text):
	 result = subprocess.run(['figlet', text], stdout=subprocess.PIPE)
	 return result.stdout.decode('utf-8')

BOT_PREFIX = ("&", "?")

TOKEN = 'NTQxNjY0ODg2NjY1NzczMDU2.DzizFw.dQxtRL1vGoXZQOKkXv3BG9HtjyM'

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball','m8'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        "That is a stupid question",
		"Is your name Glade? because, that question was very stupid.",
		"Yes, Declan is fat",
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
@client.command(description="@s someone 20 times",
							brief="@s someone 20 times")
async def at(person):
	for x in range(0, 19):
		pid = "<@" + person + ">"
		await client.say(pid)
		time.sleep(0.75)
		
# Mentions people 20 times, working on making the user set the number of mentions
@client.command(brief="Square a number")
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
    
# Links to github repo
@client.command()
async def sourcecode():
	source_code = "https://github.com/coremedic/sickobot/tree/master"
	await client.say("Ok, " + str(source_code) + " my repo is updated weekly")
	
# Not yet working 	
@client.command(brief="NOT FUNCTIONAL")
async def waifu():
	await client.say("I am still working on this command. The goal is to have the bot be able to roll for waifu's")

# Sets playing status
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)
    
# Prints current BTC price
@client.command(brief="Prints current BTC to USD conversion")
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
   
# ASCII art maker. Work in progress    
#@client.command() 
#async def ascii(text):
#	url = 'https://artii.herokuapp.com/make?text=yeet'
#	async with aiohttp.ClientSession() as session:
#		raw_response = await session.get(url) # Raw http response
#		response = await raw_response.text() # Passing raw_response to text
#		await client.say(response)

# ASCII art maker version 2 NO SPACES
@client.command(brief="ASCII art maker NO SPACES")
async def ascii(input):
	await client.say('```' + figlet(input) + '```')
	
#PRAISE THE SUN
@client.command(brief="PRAISE THE SUN")
async def pts():
	channel = client.get_channel("409576030957731842")
	await client.send_file(channel, 'pts.jpg')	
	
	

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
