import discord
import os
from discord import app_commands
from dotenv import load_dotenv
from collections import defaultdict
from utils import cat_mentioned
from dataset import load_dataset
from model import model

train_set_x, train_set_y, test_set_x, test_set_y, classes, num_px = load_dataset()
my_model = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2000, learning_rate=0.005)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

oui_list = defaultdict(lambda: set())

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

@tree.command(name="add_oui", description="Adds this user to be Ouiiiii'd in future messages")
async def add_oui(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} has been added to the Oui list in {interaction.guild.name}", ephemeral=True)
    oui_list[interaction.guild.id].add(interaction.user.id)

@tree.command(name="remove_oui", description="Removes this user from being Ouiiiii'd")
async def remove_oui(interaction):
    await interaction.response.send_message(f"{interaction.user.mention} has been removed from the Oui list in {interaction.guild.name}!", ephemeral=True)
    if interaction.user.id in oui_list[interaction.guild.id]:
        oui_list[interaction.guild.id].remove(interaction.user.id)

@tree.command(name="get_invite_link", description="Sends the invite link of this bot")
async def get_invite_link(interaction):
    await interaction.response.send_message(f"https://discord.com/api/oauth2/authorize?client_id=1192236169728106656&permissions=292057902144&scope=bot", ephemeral=True)

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.guild.id in oui_list and message.author.id in oui_list[message.guild.id]:
        if cat_mentioned(message, my_model, classes, num_px):
            await message.channel.send("Cat mentioned")

load_dotenv()

client.run(os.getenv("DISCORD_BOT_TOKEN"))