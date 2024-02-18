import discord
from scraper import get_cricket_data

TOKEN = 'MTIwNTU1MzE2NjYwMzY1MzEyMA.GhahAN.VXr5N4OmoCQaRx6LrSa4uLMC1M3ZKzm4uiaqcI'

# Define the intents for your bot
intents = discord.Intents.all()
intents.message_content = True

# Create a Discord client with intents
client = discord.Client(intents=intents)

# List to store live scores data
live_scores_data = []

@client.event
async def on_message(message):
    # ... (other parts of your code)

    if message.content.startswith('/livescore'):
        # Fetch live cricket data using the scraper function from scrapper.py
        data = get_cricket_data()

        if data:
            response = f"Team 1: {data['team1']}\nTeam 2: {data['team2']}\nStatus: {data['status']}"
            # Send the live score response
            await message.channel.send(response)

            # Write the data to the CSV file
            generate_live_scores_csv()

        else:
            response = "No live scores available! Please come back later :)"
            # Send the no live scores available response
            await message.channel.send(response)
    
    elif message.content.startswith('/generate'):
        # Generate a CSV file with live scores
        generate_live_scores_csv()

        # Send the generated CSV file
        with open('live_scores.csv', 'rb') as file:
            await message.channel.send("Here's the generated live scores CSV file:", file=discord.File(file, 'live_scores.csv'))

    elif message.content.startswith('/help'):
        # Provide information about available commands
        help_message = """
    Available commands:
    /livescore   : Get live cricket match data.
    /generate    : Generate a CSV file with live scores.
    /help        : Show this help message.
    """
        await message.channel.send(help_message)

import csv

def generate_live_scores_csv():
    # Fetch live cricket data using the scraper function from scrapper.py file
    data = get_cricket_data()

    if data:
        # Open the CSV file in append mode and write the data as separate columns
        with open('live_scores.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data['team1'], data['team2'], data['status']])

# Run the bot
client.run(TOKEN)
