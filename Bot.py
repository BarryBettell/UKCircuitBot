##Imports relivent info from discord API
import discord
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

###import oauth2
##import requests, json

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

##Sets activity to UkCircuit.Com
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='UKCircuit.com'))
    print('Ready, Freddy')

##User Join Message
@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the UK Circuit. Please make yourself familier with the rulebook before playing. https://goo.gl/s5fBoQ')
    print('Sent message to ' + member.name)


##Auto & Manual client responses
@client.event
async def on_message(message):
    ##print(message.content)
    
    ##Auto Responses 
    if '<@&472497704757493780>' in message.content: ##@Staff
        await client.send_message(message.channel,'A staff member will be with you ASAP but in the meantime if your question is regarding a report, dispute or make a suggestion the relevent forms can be found in <#389877171637714944>.')

    if '<@&503294719909036042>' in message.content: ##@ALStaff
        await client.send_message(message.channel,'A staff member will be with you ASAP but in the meantime if your question is regarding a report or a dispute the relevent forms can be found in <#389877171637714944>.')
        
    if '<@&472468000214089738>' in message.content: ##@Senior Moderator
        await client.send_message(message.channel,'A staff member will be with you ASAP but in the meantime if your question is regarding a report, dispute or make a suggestion the relevent forms can be found in <#389877171637714944>.')
        
    if '<@&472467435489067008>' in message.content: ##@Moderator
        await client.send_message(message.channel,'A staff member will be with you ASAP but in the meantime if your question is regarding a report, dispute or make a suggestion the relevent forms can be found in <#389877171637714944>.')
        
    if '<@&472468391941242900>' in message.content: ##@Junior Moderator
        await client.send_message(message.channel,'A staff member will be with you ASAP but in the meantime if your question is regarding a report, dispute or make a suggestion the relevent forms can be found in <#389877171637714944>.')
        
    if '<@&497349435744059402>' in message.content: ##@Admin
        await client.send_messag
        e(message.channel, 'Please use <@&472497704757493780> to notfiy all online staff members!')

    ##Manual Staff Commands
    if message.author.server_permissions.kick_members and message.content.lower() == '!need':
        await client.send_message(message.channel, 'Please only use this channel if you need a staff member!')
    
    if message.author.server_permissions.kick_members and message.content.lower() == '!suggest': 
        await client.send_message(message.channel, 'Please only use this channel if you have a genuine suggestion!')
        
    if message.author.server_permissions.kick_members and message.content.lower() == '!report':
        await client.send_message(message.channel, 'If you would like to submit a report the form can be found in <#389877171637714944>:\n- All reports will be dealt with by a staff member ASAP!\n- When submitting a report please make sure you include evidence of the infraction.\n - If submitting a demo as evidence please make sure to include the round numbers. ')        

    if message.author.server_permissions.kick_members and message.content.lower() == '!staffreport':
        await client.send_message(message.channel, 'If you would like to report a Staff member for an offence please use the form linked bellow:\n - https://goo.gl/NVTZuu \n - All reports involving a Staff member will only be viewed and dealt with by Head Admins and will be dealt with accordingly')
        
    if message.author.server_permissions.kick_members and message.content.lower() == '!dispute':
        await client.send_message(message.channel, 'If you would like to dispute a ban the form can be found in <#389877171637714944>:\n- All disputes will be reviewed with by a staff member ASAP!\n- You will be contacted once it has been reviewed with the outcome.\n - It is best practice to include counter evidence in your dispute.')
        
    if message.author.server_permissions.kick_members and message.content.lower() == '!apply':
        await client.send_message(message.channel, 'If you would like to apply to the staff team the form can be found in <#389877171637714944>:\n- Please remember we are not continuously in search for new staff members but your application may be re reviewed at a later date.\n - You will only be contacted if the decision is made to give you a trial period.')
        
    if message.author.server_permissions.kick_members and message.content.lower() == '!redeem':
        await client.send_message(message.channel, 'To redeem your prize please DM the official Twitter account:\n- https://goo.gl/1pd31p \n- Someone will be in contact with you ASAP but please bear in mind the owners can be very busy so response times may vary!')

    if message.author.server_permissions.kick_members and message.content.lower() == '!commands':
        await client.send_message(message.channel, 'The current commands are:\n - !Need\n - !Report\n - !Dispute\n - !Apply\n - !Redeem\n - !Discord\n - !Giveaway\n - !at\n - !AlApply')

    if message.author.server_permissions.kick_members and message.content.lower() == '!discord':
        await client.send_message(message.channel, 'https://discord.gg/BvVFEZf')
        
    if message.author.server_permissions.kick_members and message.content.lower() == '!giveaway':
        await client.send_message(message.channel, 'The current giveaway can be found here:\n - https://goo.gl/2MEg9F')

    if message.author.server_permissions.kick_members and message.content.lower() == '!at':
        await client.send_message(message.channel, '@ Here Ruling:\n - Only post @ here messages once every 10 mins.\n - Do not post them if there are less than 5 in queue')
    ##AL Commads
    if message.author.server_permissions.kick_members and message.content.lower() == '!alapply':
        await client.send_message(message.channel, 'Please apply via the UK AL hub\n - https://goo.gl/VyopHF')

    

client.run('NDk2OTczNzI1NDQzNTU1MzI4.DpaDTw.sxXRMrtDR4gVO-9FDJxf3hZPVK0')


