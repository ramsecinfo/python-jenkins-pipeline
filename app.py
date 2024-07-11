from my_flask_app import app  # Ensure this import matches your app's structure
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_Home(client):
    response = client.get('/')
    assert b"<body style='background-color: #9dffff; height=100%; display:flex;'><div style='font-family: Poppins; display:flex; flex-direction: column; align-self: center; width: 100%'><h1 style='text-align:center'>Welcome to Jenkins CI/CD Pipeline for Python Application</h1><h2 style='text-align:center'>Also with SAST Security Scan</h2></div></body>" in response.data
