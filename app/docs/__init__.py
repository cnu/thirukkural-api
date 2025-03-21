from flask import Blueprint, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os
import json

# Create a blueprint for documentation
docs_bp = Blueprint('docs', __name__)

# Path to the OpenAPI specification file
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
openapi_path = os.path.join(project_root, 'openapi.yaml')

# Route to serve the OpenAPI specification as JSON
@docs_bp.route('/openapi.json')
def serve_openapi_json():
    """Serve the OpenAPI specification as JSON"""
    import yaml
    with open(openapi_path, 'r') as f:
        spec = yaml.safe_load(f)
    return jsonify(spec)

# Route to serve the OpenAPI specification as YAML
@docs_bp.route('/openapi.yaml')
def serve_openapi_yaml():
    """Serve the OpenAPI specification as YAML"""
    with open(openapi_path, 'r') as f:
        return f.read(), 200, {'Content-Type': 'text/yaml'}

# Route to serve ReDoc HTML
@docs_bp.route('/redoc')
def redoc():
    """Serve ReDoc documentation"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Thirukkural API - ReDoc</title>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
        <style>
            body {{
                margin: 0;
                padding: 0;
            }}
        </style>
    </head>
    <body>
        <redoc spec-url='/docs/openapi.json'></redoc>
        <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
    </body>
    </html>
    """

# Create Swagger UI blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    '/docs/swagger',
    '/docs/openapi.json',
    config={
        'app_name': "Thirukkural API",
        'deepLinking': True,
        'defaultModelsExpandDepth': 3,
        'defaultModelExpandDepth': 3,
    }
)
