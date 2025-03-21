from functools import wraps
from flask import request, jsonify
import os

def get_api_key():
    """Get the API key from environment variables"""
    return os.environ.get('API_KEY', 'default_api_key_for_development')

def token_required(f):
    """Decorator to require a valid API token for access"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        
        # Check if Authorization header exists and has the Bearer prefix
        if auth_header:
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'error': 'Authentication token is missing!'}), 401
        
        # Simple static token comparison
        if token != get_api_key():
            return jsonify({'error': 'Invalid authentication token!'}), 401
            
        return f(*args, **kwargs)
    
    return decorated
