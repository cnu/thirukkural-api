# Thirukkural API

A Flask-based RESTful API for accessing Thirukkural couplets. Thirukkural is a classic Tamil Sangam literature consisting of 1330 couplets or Kurals, authored by Thiruvalluvar.

## Features

- Get all Thirukkural couplets
- Get a specific Thirukkural couplet by number
- Get multiple Thirukkural couplets by providing a comma-separated list of numbers
- Get all Thirukkural couplets from a specific chapter
- Bearer token authentication for API security
- API documentation with Swagger UI and ReDoc
- Pagination support for retrieving large datasets

## API Endpoints

- `GET /api/kurals` - Get all kurals (with pagination support)
  - Query parameters:
    - `page` - Page number (default: 1)
    - `per_page` - Number of items per page (default: 10, max: 100)
- `GET /api/kurals/<numbers>` - Get kurals by number(s), where numbers can be a single number (e.g., 1) or comma-separated numbers (e.g., 1,2,3)
- `GET /api/chapters` - Get all chapter details
- `GET /api/chapters/<chapter_number>/kurals` - Get all kurals from a specific chapter

## Authentication

This API uses Bearer token authentication. You must include an `Authorization` header with a valid API key in all requests.

Example:
```
Authorization: Bearer your_api_key_here
```

The API key is stored as an environment variable (`API_KEY`). Make sure to set this variable in your environment or in a `.env` file.

## API Documentation

The API documentation is available at:

- Swagger UI: `/docs/swagger/`
- ReDoc: `/docs/redoc`

These interactive documentation interfaces allow you to explore the API endpoints and even test them directly from your browser.

## Local Development

1. Clone the repository:
```
git clone https://github.com/yourusername/thirukkural.git
cd thirukkural
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example` and set your API key:
```
cp .env.example .env
# Edit the .env file to set your API_KEY
```

5. Run the application:
```
flask run
```

6. Access the API at `http://localhost:5000`

## Running Tests

To run the tests for this application:

```
# Activate the virtual environment if not already activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run a specific test file
pytest tests/test_api.py

# Run tests with coverage
pytest --cov=app tests/

# Generate HTML coverage report
pytest --cov=app --cov-report=html tests/
# This will create a htmlcov directory with an HTML report that you can open in a browser
```

## Deployment to Heroku

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku:
```
heroku login
```

3. Create a new Heroku app:
```
heroku create your-app-name
```

4. Set the API key as a Heroku config variable:
```
heroku config:set API_KEY=your_secret_api_key_here
```

5. Push to Heroku:
```
git push heroku main
```

6. Access your API at `https://your-app-name.herokuapp.com`

## Data Source

The Thirukkural data is sourced from [tk120404/thirukkural](https://github.com/tk120404/thirukkural) GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
