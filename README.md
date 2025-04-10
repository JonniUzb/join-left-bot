# Telegram Anti-Spam Bot

A modular Telegram bot for spam detection and group management.

## Features
- Spam message detection and deletion
- Join/leave message handling
- Role-based permissions (bot admin, group admin, regular users)
- Group statistics tracking
- Customizable welcome messages and group rules
- Reputation system for users
- Comprehensive logging

## Requirements
- Python 3.11
- python-telegram-bot 21.0.1

## Installation
1. Clone this repository
2. Install dependencies: `pip install python-telegram-bot==21.0.1`
3. Create a bot with BotFather and get your token
4. Replace `YOUR_BOT_TOKEN` in `main.py` with your actual token
5. Set your user ID as `INITIAL_BOT_ADMIN` in `main.py`

## Usage
1. Run the bot: `python main.py`
2. Add the bot to your group with admin privileges
3. Use `/settings` in a private chat with the bot to configure it

## Commands
### Bot Admin
- `/broadcast <message>` - Send message to all groups
- `/add_bot_admin <user_id>` - Add new bot admin
- `/settings` - Configure bot settings
- `/logs` - Export bot logs

### Group Admin
- `/mute <user_id> <minutes>` - Mute a user
- `/ban <user_id>` - Ban a user
- `/grant <permission>` - Grant permission to user (reply to user)
- `/revoke <permission>` - Revoke permission from user (reply to user)
- `/stats` - View group statistics

### All Users
- `/rules` - View group rules
- `/reputation` - View your reputation
- `/stats` - View group statistics#   j o i n - l e f t - b o t  
 #   j o i n - l e f t - b o t  
 