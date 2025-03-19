import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route returns correct information"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'name' in data
    assert 'endpoints' in data

def test_get_all_kurals(client):
    """Test getting all kurals"""
    response = client.get('/api/kurals')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_kural(client):
    """Test getting a single kural"""
    response = client.get('/api/kurals/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['Number'] == 1

def test_get_multiple_kurals(client):
    """Test getting multiple kurals"""
    response = client.get('/api/kurals/1,2,3')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]['Number'] == 1
    assert data[1]['Number'] == 2
    assert data[2]['Number'] == 3

def test_get_kurals_by_chapter(client):
    """Test getting kurals by chapter"""
    response = client.get('/api/chapters/1/kurals')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'chapter' in data
    assert 'kurals' in data
    assert len(data['kurals']) > 0

def test_invalid_kural_number(client):
    """Test getting an invalid kural number"""
    response = client.get('/api/kurals/9999')
    assert response.status_code == 404

def test_invalid_kural_format(client):
    """Test getting kurals with invalid format"""
    response = client.get('/api/kurals/abc')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

def test_get_all_chapters(client):
    """Test getting all chapters"""
    response = client.get('/api/chapters')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, dict)
    assert len(data) > 0

def test_invalid_chapter_number(client):
    """Test getting kurals from an invalid chapter"""
    response = client.get('/api/chapters/999/kurals')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data
