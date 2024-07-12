import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app, db
from app.models import User, BlogPost

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    return app

@pytest.fixture
def client(app):
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_signup(client):
    response = client.post('/signup', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 201
    assert b'User created successfully' in response.data

def test_login(client):
    # First, create a user
    client.post('/signup', json={'username': 'testuser', 'password': 'testpass'})
    # Then try to log in
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_create_post(client):
    # First, create a user and log in
    client.post('/signup', json={'username': 'testuser', 'password': 'testpass'})
    login_response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    access_token = login_response.json['access_token']
    
    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.post('/posts', json={'title': 'Test Post', 'content': 'This is a test post'}, headers=headers)
    assert response.status_code == 201
    assert b'Post created successfully' in response.data

def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)

