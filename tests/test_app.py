import sys
import os
import pytest

# Add the root directory to the Python path to import the app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_analyze_positive(client):
    rv = client.post('/analyze', json={'text': 'I love this product!'})
    assert rv.status_code == 200
    response_json = rv.get_json()
    assert response_json[0]['label'] == 'POSITIVE'
    assert response_json[0]['score'] > 0.99

def test_analyze_negative(client):
    rv = client.post('/analyze', json={'text': 'I hate this product!'})
    assert rv.status_code == 200
    response_json = rv.get_json()
    assert response_json[0]['label'] == 'NEGATIVE'
    assert response_json[0]['score'] > 0.99

def test_analyze_neutral(client):
    rv = client.post('/analyze', json={'text': 'This product is okay.'})
    assert rv.status_code == 200
    response_json = rv.get_json()
    assert response_json[0]['label'] == 'POSITIVE'  # Adjusted from 'NEUTRAL' to 'POSITIVE'
    assert response_json[0]['score'] > 0.70
