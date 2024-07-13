from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the pre-trained model
model_pipeline = pipeline('sentiment-analysis')

@app.route('/')
def home():
    return "Welcome to the AI-Powered Customer Support Chatbot!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    # Perform sentiment analysis
    results = model_pipeline(data['text'])
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

