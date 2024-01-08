import re
import discord
from requests import get
from bs4 import BeautifulSoup
from model import predict_image

cat_references = ["cat", "meow", "miau", "purr", "kitten"]

def tenor(content: discord.Message.content):
    pattern = r"https:\/\/tenor\.com\/view\/[-a-zA-Z0-9@:%._\+~#=?&\/]+"
    match = re.search(pattern, content)

    if match:
        url = match.group()
        html = get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('div', class_='RelatedTag')
        for reference in cat_references:
            if any(reference in tag.text.strip().lower() for tag in tags):
                return True
        
    return False

def image(url, my_model, classes, num_px):
    my_predicted_image = predict_image(url, my_model, classes, num_px)
    print(my_predicted_image)
    return "cat" == my_predicted_image

def text(user_message : discord.Message.content):
    if any(reference in user_message.lower() for reference in cat_references):
        return True
    return False

def cat_mentioned(message: discord.Message, my_model, classes, num_px):
    if "tenor.com" in message.content:
        return tenor(message.content)
    if any(image(attachment.url, my_model, classes, num_px) for attachment in message.attachments):
        return True
    return text(message.content)