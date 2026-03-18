from fastapi import FastAPI
from app.routes import auth, test

app = FastAPI()

# Routers
app.include_router(auth.router)
app.include_router(test.router)


@app.get("/health")
async def root():
    return {"status": "ok"}