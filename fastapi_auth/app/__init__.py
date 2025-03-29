from fastapi import FastAPI
from app.routes import auth_router

def create_app():
    app = FastAPI(title="Authentication API")
    
    # register your router here
    app.include_router(auth_router)

    return app
