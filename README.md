# Enterprise Chatbot

## Overview
This project is an AI-powered customer support chatbot for enterprises, leveraging Natural Language Processing (NLP) to analyze sentiment and provide responses to customer inquiries.

## Features
- Sentiment analysis of customer inputs (Positive, Negative, Neutral)
- REST API using Flask
- Model deployment and testing with pytest

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone your-repository
   cd repo
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the Flask application:
   ```bash
   python app.py
2. Test the API using curl or Postman:
   ```bash
   curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
## Testing
- To run tests, use the following command:
  ```bash
   pytest tests/test_app.py
## Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature-branch)
5. Create a new Pull Request
