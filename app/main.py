# app/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers import pokemons

app = FastAPI(
    title="Mini-PokeAPI",
    version="1.0.0",
)

@app.get("/", include_in_schema=False)
def root():
    return {"message": "Mini-PokeAPI online. Veja /docs para a documentação."}

@app.get("/healthz", include_in_schema=False)
def healthz():
    return {"status": "ok"}

# Rotas de negócio
app.include_router(pokemons.router)
