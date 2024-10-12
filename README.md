# Telegram Bot  and Python

# Telegram Bot

This project is a simple Telegram bot that sends messages to a specified channel using the Telegram Bot API. The bot uses environment variables to store sensitive information such as the bot token and channel ID.

## Features

- Sends messages to a Telegram channel using curl.
- Loads configuration from a `.env` file.

## Prerequisites

- Python 3.x
- `requests` and `python-dotenv` libraries.
- Docker (optional, if you want to run it in a container).

## Creating a Telegram Bot and Channel

### Step 1: Create a Telegram Bot

1. **Open Telegram**: You can use either the mobile app or the desktop version.
   
2. **Find the BotFather**: Search for `@BotFather` in the Telegram search bar. This is the official bot for creating new bots.

3. **Start a chat with BotFather**: Click the "Start" button or type `/start`.

4. **Create a new bot**:
   - Type the command `/newbot`.
   - Follow the prompts to give your bot a name and username. The username must end with "bot" (e.g., `mybot`).

5. **Get your bot token**: After creating the bot, BotFather will provide you with a token. **Keep this token safe**, as you will need it for your bot configuration.

### Step 2: Create a Telegram Channel

1. **Open Telegram**: Use the same Telegram app.

2. **Create a new channel**:
   - Tap the menu (three horizontal lines) in the top-left corner.
   - Select "New Channel".
   - Follow the prompts to create your channel, including giving it a name and description.

3. **Add your bot to the channel**:
   - Open your channel.
   - Tap on the channel name at the top to access channel settings.
   - Select "Members" or "Administrators".
   - Search for your bot by its username and add it to the channel.
   - Make sure to grant it permissions to send messages (it should be an admin).

### Step 3: Obtain Credentials

1. **Bot Token**: Copy the token you received from BotFather when you created your bot. This is your `TELEGRAM_TOKEN`.

2. **Chat ID**: To get the `CHAT_ID` and `CANAL_ID`, follow these steps:
   - **Get Chat ID**: Start a conversation with your bot by searching for its username and sending any message.
   - Open your browser and visit the following URL (replace `YOUR_TELEGRAM_TOKEN` with your actual token):

     ```
     https://api.telegram.org/botYOUR_TELEGRAM_TOKEN/getUpdates
     ```

   - Find the JSON response. Look for `"chat": {"id": ...}` in the output. The `id` value is your `CHAT_ID`.

   - **Get Canal ID**: The `CANAL_ID` for channels typically starts with `-100` followed by a series of digits. You can find it similarly by looking for your channel's messages or using the same `getUpdates` endpoint.

### Step 4: Configure the Bot

1. **Create a `.env` file** in the root directory and add your Telegram bot token, chat ID, and channel ID:

   ```env
   TELEGRAM_TOKEN=your_bot_token
   CHAT_ID=your_chat_id
   CANAL_ID=your_channel_id
   
### Step5: Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/telegram-bot.git
   cd telegram-bot
2. Install the required packages:
   pip install requests python-dotenv
   Usage
   To send a message to the Telegram channel, run the following command:python telegram-bot.py
3. Docker Usage
   Build the Docker image : sudo docker build -t telegram-bot .
   Run the Docker container with the environment variables:
   sudo docker run --env-file .env telegram-bot
   This will execute the script inside the Docker container, sending a message to your specified Telegram channel.
Enjoy!!
