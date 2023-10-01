import discord
import csv
from webscrap import scrap

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.content.startswith('!livescore'):
        t1, t2, status, r1, r2 = scrap()  
        await message.channel.send(f'Status: {status}\n{t1} : {r1}\n{t2} : {r2}')
        with open('history.csv', mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            data = scrap()
            csv_writer.writerow([data[0], data[1], data[2], data[3], data[4]])
    if message.content.startswith('!generate'):
        await message.channel.send(file=discord.File("history.csv"))
    if message.content.startswith('!help'):
        await message.channel.send('For livescores: !livescore\nFor the CSV file: !generate')
        
bot.run('MTE1NjMwMjUxNTQ1MzgzNzQwMw.Gww-TY.fhHl_5rYUY82-F4FwDeAMtzqNq_UxW8mwUYh5U')

