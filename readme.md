
# WattWise AI Assistant - Local

## Introduction

WattWise is your energy-awareness companion, leveraging AI technology to provide personalized insights into your daily energy consumption across food, transport, and home utilities. With real-time data and user inputs, Wattwise aids in visualizing your energy footprint and suggests actionable steps to foster sustainable living.

## Core Values

- **Sustainable Living**: Offering solutions that enable individuals to cultivate eco-friendly habits.
- **Knowledge Empowerment**: Encouraging education and growth through open-source design.
- **Energy Awareness**: Enhancing understanding of energy sources and their environmental impacts.

## About Us

We are Carlotta and Oliver, two former students of the Masters in Design for Emergent Futures at IAAC and ELISAVA. This project is the culmination of our Thesis research project, where we hope w've created the start of a new and more conversational approach to energy and carbon consumption tracking. With this tool we hope to inspire people to make sustianable habit changes that they feel they are able to do without compromising on quality of life.

- **Carlotta**: An industrial design engineer passionate about human-centered and sustainable design.
- **Oliver**: A product designer focusing on planet-centered design spanning both physical and digital domains.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TheWattWiseProject/WattWise-AI-Bot.git 
   cd WattWise-AI-Bot/WattWise\ General\ Chatbot
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Setup Environment Variables

- Ensure the following variables are set up in your environment or within a `.env` file:
  - `OPENAI_API_KEY`: Your OpenAI API key.
  - `TELEGRAM_TOKEN`: Your Telegram bot token.
  - `LANGCHAIN_API_KEY`: Your LangChain API key.

### Creating a Telegram Bot

1. Open Telegram and search for "BotFather."
2. Start a chat with BotFather and send the command `/newbot`.
3. Follow the prompts to set up your bot, including choosing a name and username.
4. Once created, BotFather will provide you with an API token. This token should be added as the `TELEGRAM_TOKEN` in your environment variables.

### Running the Application

- Start the application using Flask:
  ```bash
  python main.py
  ```

- The bot can be accessed via Telegram using your bot created with BotFather.

## Project Structure

- `assistant.py`: Manages the AI assistant's creation and updates, using GPT-4o from OpenAI.
- `core_functions.py`: Contains key functions utilized throughout the project.
- `main.py`: Central script to initialize all components and ensure the bot's operation.
- `integrations/Telegram_V3.py`: Manages Telegram bot interactions, including handling various input types and retrieving responses from OpenAI.
- `requirements.txt`: Lists all dependencies needed for the project.
- `resources/`: Contains datasets concerning energy and environmental impacts used by the assistant.
- `docs/static/`: Location for the vector store, optimizing document retrieval for responses.

## Instructions for the Assistant

The instructions for interacting with the assistant are detailed in `assistant/instructions.txt`, guiding the response mechanism for user queries.

## Vector Store

Data from the resources is compiled into a vector store (initialized in the `docs/static` directory), enabling efficient processing and response generation by retrieving relevant information swiftly.

## Contributing

We welcome and appreciate contributions! To learn more or get involved, please visit the [WattWise Website](#) or reach out through social media. Your support and collaboration play a crucial role in fostering sustainability and energy awareness globally.

## Credits

This project would not have been possible without the incredible work done by Jannis Moore, and his GPT Chatbot Framework 2.0, which provided much of the underlying architecture for this project and ensured we were able to stand on the shoulders of giants. 

To learn more about Jannis's work check out his youtube channel linked below:

[YouTube Channel](https://www.youtube.com/@jannismoore/featured)