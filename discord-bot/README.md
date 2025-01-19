# Discord Bot to Send Annual Video

This project is a Discord bot that sends a specific video to a designated user every year on a specified date.

## Project Structure

```
discord-bot
├── src
│   ├── main.py          # Main entry point for the Discord bot
│   └── utils
│       └── __init__.py  # Utility functions for the bot
├── .env                 # Environment variables for sensitive information
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd discord-bot
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Discord bot token and designated user ID:
   ```
   DISCORD_TOKEN=your_bot_token
   USER_ID=designated_user_id
   ```

## Usage

Run the bot using the following command:
```
python src/main.py
```

The bot will send the specified video to the designated user on the specified date each year. Make sure to keep the bot running to ensure it can send the video on time.