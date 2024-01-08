# OuiBot - The Cat-Loving Discord Bot

## Introduction
OuiBot is a charming and interactive Discord bot inspired by a cat-enthusiast, "Ouiiiiii". It enhances Discord servers by detecting cat-related content in messages, responding with delightful interactions whenever cats are mentioned, or cat images and GIFs are shared.

## Features
- **Cat Detection**: Detects mentions of cats in text messages, using keyword matching.
- **Cat GIFs Response**: Automatically identifies a cat GIF from Tenor by leveraging web scraping techniques to look at image tags.
- **Image Recognition**: Identifies cat images in JPG or PNG format using a custom logistic regression model, and responds accordingly.

## Technical Overview
OuiBot is developed in Python, using several libraries to handle various functionalities:
- **Discord Interaction**: Uses `discord.py` for seamless interaction with the Discord API.
- **Image Recognition**: Employs a logistic regression model, built with `numpy`, for recognizing cat images.
- **GIF Retrieval**: Fetches cat-related GIFs from Tenor, utilizing `requests` and `beautifulsoup4` for web scraping.
- **Environmental Variables**: Manages API keys and sensitive data using `python-dotenv`.
- **Image Processing**: `Pillow` library is used for image data handling, crucial for the image recognition feature.

## Setup and Installation
1. Install Python `3.11` on your system.
2. Clone the repository and navigate to the project directory.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up a `.env` file containing Discord API token.
5. Run the bot:
   ```
   python oui.py
   ```

## Dataset and Model Training
The logistic regression model is trained on a dataset of cat images. The model is implemented using `numpy` to employ the vector operations involved in training. The model distinguishes between cat and non-cat images, which is central to the bot's image recognition feature.

## Acknowledgements
A special shoutout to Daniel Kang for his expert advice on the Discord API, significantly contributing to OuiBot's development.