from fastapi import FastAPI
from app.routes import auth

app = FastAPI()

# Routers
app.include_router(auth.router)

@app.get("/health")
async def root():
    return {"status": "ok"}