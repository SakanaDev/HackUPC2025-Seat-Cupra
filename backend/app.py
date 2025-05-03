from flask import Flask, request, jsonify
from flask_cors import CORS
from google import generativeai as genai
import pathlib
import json
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.get_json()
        user_input = data.get('question', '').strip()

        if not user_input:
            return jsonify({'error': 'Question is required'}), 400

        filepath = pathlib.Path(__file__).parent / 'manual_cupra.pdf'
        if not filepath.exists():
            return jsonify({'error': 'PDF file not found'}), 500

        model = genai.GenerativeModel("models/gemini-1.5-flash")

        contents = [
            {
                "mime_type": "application/pdf",
                "data": filepath.read_bytes()
            },
            {
                "text": f"""You're a virtual assistant specialized in helping customers understand the Cupra TAVASCAN owner's manual.
Please answer this question clearly and concisely:
{user_input}"""
            }
        ]

        response = model.generate_content(contents)
        os.makedirs('chatbot', exist_ok=True)
        with open('chatbot/data.json', 'w') as f:
            json.dump({'response': response.text}, f)

        return jsonify({'status': 'success', 'response': response.text})

    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
