#  Flask & FastAPI Authentication API
---

##  Setup Instructions

### 1️⃣ Create a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

##  Running the Application

### -> Flask Application
```sh
python flask_app.py
```

### -> FastAPI Application
```sh
uvicorn fastapi_app:app --host 127.0.0.1 --port 5000 --reload
```

---

##  Testing the API

###  Using `curl`
#### Flask
```sh
curl -X POST http://127.0.0.1:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username": "user1", "password": "password123"}'
```

#### FastAPI
```sh
curl -X POST http://127.0.0.1:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username": "user1", "password": "password123"}'
```

###  Using Postman
1. Open **Postman**.
2. Set **Method** to `POST`.
3. Enter URL:
   - Flask: `http://127.0.0.1:5000/login`
   - FastAPI: `http://127.0.0.1:5000/login`
4. Go to **Body** → **raw** → **JSON**.
5. Enter the following JSON:
   ```json
   {
       "username": "user1",
       "password": "password123"
   }
   ```
6. Click **Send** and check the response.



