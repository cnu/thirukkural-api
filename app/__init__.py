from flask import Flask
from app.api.routes import api_bp

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return {
            "name": "Thirukkural API",
            "description": "API for accessing Thirukkural couplets",
            "endpoints": {
                "GET /api/kurals": "Get all kurals",
                "GET /api/kurals/<numbers>": "Get kurals by number(s), where numbers can be a single number (e.g., 1) or comma-separated numbers (e.g., 1,2,3)",
                "GET /api/chapters": "Get all chapter details",
                "GET /api/chapters/<chapter_number>/kurals": "Get all kurals from a specific chapter"
            }
        }
    
    return app

app = create_app()