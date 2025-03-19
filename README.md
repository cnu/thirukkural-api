# Thirukkural API

A Flask-based RESTful API for accessing Thirukkural couplets. Thirukkural is a classic Tamil Sangam literature consisting of 1330 couplets or Kurals, authored by Thiruvalluvar.

## Features

- Get all Thirukkural couplets
- Get a specific Thirukkural couplet by number
- Get multiple Thirukkural couplets by providing a comma-separated list of numbers
- Get all Thirukkural couplets from a specific chapter

## API Endpoints

- `GET /api/kurals` - Get all kurals
- `GET /api/kurals/<numbers>` - Get kurals by number(s), where numbers can be a single number (e.g., 1) or comma-separated numbers (e.g., 1,2,3)
- `GET /api/chapters` - Get all chapter details
- `GET /api/chapters/<chapter_number>/kurals` - Get all kurals from a specific chapter

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

4. Run the application:
```
flask run
```

5. Access the API at `http://localhost:5000`

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

4. Push to Heroku:
```
git push heroku main
```

5. Access your API at `https://your-app-name.herokuapp.com`

## Data Source

The Thirukkural data is sourced from [tk120404/thirukkural](https://github.com/tk120404/thirukkural) GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
