from fastapi import FastAPI
from app.db import Base, engine
from app.routers import pokemons

app = FastAPI(title="Mini PokeAPI EBAC", version="1.0.0")

app.include_router(pokemons.router)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

Base.metadata.create_all(bind=engine)
