from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_register_user():
    """Test user registration"""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword123",
        "full_name": "Test User"
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login_user():
    """Test user login"""
    # Register first
    user_data = {
        "username": "logintest",
        "email": "login@example.com",
        "password": "password123",
        "full_name": "Login Test"
    }
    client.post("/auth/register", json=user_data)
    
    # Login
    login_data = {
        "username": "logintest",
        "password": "password123"
    }
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_invalid_login():
    """Test invalid login"""
    login_data = {
        "username": "nonexistent",
        "password": "wrongpassword"
    }
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 401

def test_list_products():
    """Test list products endpoint"""
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
