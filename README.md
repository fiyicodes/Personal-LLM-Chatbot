# Personal Chatbot

A Flask-based personal chatbot that uses OpenAI's GPT to answer questions about you based on provided information.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

3. Edit the `personal_info.txt` file with your personal information. This is the knowledge base that the chatbot will use to answer questions about you.

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Start chatting! The chatbot will respond to questions based on the information provided in `personal_info.txt`

## Features

- Modern, responsive UI
- Real-time chat interface
- Typing indicators
- Error handling
- Mobile-friendly design

## Customization

You can customize the chatbot by:
1. Modifying the system prompt in `app.py`
2. Updating the UI in `templates/index.html`
3. Adjusting the OpenAI model parameters in the `/chat` endpoint
