from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load personal information
def load_personal_info():
    try:
        with open('personal_info.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "No personal information available yet."

SYSTEM_PROMPT = """You are a personal chatbot assistant. Use the following information about the person to answer questions:

{personal_info}

Only answer questions based on the information provided above. If you don't have enough information to answer a question, 
politely say so and suggest asking something else."""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        personal_info = load_personal_info()
        
        # Create chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT.format(personal_info=personal_info)},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return jsonify({
            "response": response.choices[0].message['content']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
