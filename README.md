# Data Science Interview Chatbot

This repository contains the code for a Telegram chatbot powered by OpenAI's GPT-3.5 Turbo model. The chatbot is designed to help users practice data science interviews by asking relevant questions and providing a conversational experience.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Demo](#demo)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- Data science interview practice mode.
- General conversation mode.
- AI-powered responses using OpenAI's GPT-3.5 Turbo model.
- Easy-to-use Telegram interface.

## Requirements

- Python 3.7 or higher
- `aiogram` library
- `openai` library
- `python-dotenv` library

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/datascience-interview-chatbot.git
cd datascience-interview-chatbot
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Create a `.env` file and add your OpenAI API key and Telegram bot token:

```bash
echo "OPENAI_API_KEY=your_openai_api_key" > .env
echo "TOKEN=your_telegram_bot_token" >> .env
```

4. Run the chatbot:

```bash
python chatbot.py
```

## Usage

1. Start a conversation with the Telegram bot by sending the `/start` command.
2. Use the `/help` command to view available commands.
3. Enable data science interview mode by sending the `/interview` command.
4. Answer the questions provided by the bot and practice your data science interview skills.
5. Disable data science interview mode by sending the `/interview` command again.

## Demo

_TODO: https://youtu.be/afYWLFzlYJE

## Contributing

Feel free to submit pull requests for new features or improvements. When submitting a pull request, please make sure to describe the changes made and how they benefit the project.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
