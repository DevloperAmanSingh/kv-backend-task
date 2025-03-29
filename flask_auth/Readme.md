# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python flask_app.py

#Testing API

Using `curl`
- `curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "user1", "password": "password123"}'`