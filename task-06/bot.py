import discord
from scraper import get_livescore
import csv


TOKEN = 'MTIwNTU1MzE2NjYwMzY1MzEyMA.GPJUze.gEktsNJ0XG8U2qtaprU2cLHtH1n-5oyUxNl_eU'

# defining the intents for Crickey bot
intents = discord.Intents.all()
intents.message_content = True

# creating a Discord client with intents0
client = discord.Client(intents=intents)

# list to store live scores data
live_scores_data = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/livescore'):
        # fetching live cricket data using my scraper fn from scraper.py
        data = get_livescore()

        if data:
            response = f"Team 1: {data['teamA']}\nTeam 2: {data['teamB']}\nStatus: {data['status']}"
        else:
            response = "No live scores available! Please come back later :)"

        await message.channel.send(response)

    elif message.content.startswith('/generate'):
        # generating a CSV file with the live scores
        generate_live_scores_csv()
        
        # senidng the generated CSV file
        with open('live_scores.csv', 'rb') as file:
            await message.channel.send("Here's the generated live scores CSV file:", file=discord.File(file, 'live_scores.csv'))

    elif message.content.startswith('/help'):
        # providing info to server members about available commands to use 
        help_message = """
    Available commands:
    /livescore   : Get live cricket match data.
    /generate    : Generate a CSV file with live scores.
    /help        : Show this help message.
    """
        await message.channel.send(help_message)

def generate_live_scores_csv():
    # fetching live cricket data using my scraper fn from scraper.py file
    data = get_livescore()

    if data:
        formatted_data = f"Team 1: {data['teamA']}\nTeam 2: {data['teamB']}\nStatus: {data['status']}"

        # writing the formatted data in the CSV file as a list
        with open('live_scores.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([formatted_data])

# running the Crickey bot :)
client.run(TOKEN)
