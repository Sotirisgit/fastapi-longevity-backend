from fastapi import FastAPI
from app.routes import users

app = FastAPI()

# Register the /users route
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI with Supabase is running 🚀"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

