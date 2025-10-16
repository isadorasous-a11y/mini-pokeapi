# app/routers/pokemons.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db import get_db
from app.settings import settings
from app import crud, schemas, models


router = APIRouter(prefix="/pokemons", tags=["pokemons"])


# --- Helper: converte ORM -> Schema (lista de tipos como array) ---
def to_schema(p: models.Pokemon) -> schemas.PokemonOut:
    return schemas.PokemonOut(
        id=p.id,
        name=p.name,
        height=p.height,
        weight=p.weight,
        types=p.types.split(",") if p.types else [],
        sprite=p.sprite,
        external_id=p.external_id,
    )


# --- Endpoints ---

@router.get("", response_model=dict)
def list_endpoint(
    db: Session = Depends(get_db),
    limit: int = Query(settings.PAGE_SIZE_DEFAULT, ge=1, le=settings.PAGE_SIZE_MAX),
    offset: int = Query(0, ge=0),
    q: str | None = None,
):
    data = crud.list_pokemons(db, skip=offset, limit=limit, q=q)
    total = crud.count_pokemons(db, q=q)
    results = [to_schema(d) for d in data]
    return {
        "metadata": {"count": total, "limit": limit, "offset": offset},
        "results": results,
    }


@router.get("/{pokemon_id}", response_model=schemas.PokemonOut)
def get_one(pokemon_id: int, db: Session = Depends(get_db)):
    p = crud.get_pokemon(db, pokemon_id)
    if not p:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return to_schema(p)


@router.post("", response_model=schemas.PokemonOut, status_code=201)
def create(payload: schemas.PokemonCreate, db: Session = Depends(get_db)):
    try:
        p = crud.create_pokemon(db, payload)
        return to_schema(p)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Nome já existente")


@router.put("/{pokemon_id}", response_model=schemas.PokemonOut)
def update(pokemon_id: int, payload: schemas.PokemonUpdate, db: Session = Depends(get_db)):
    p = crud.update_pokemon(db, pokemon_id, payload)
    if not p:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return to_schema(p)


@router.delete("/{pokemon_id}", status_code=204)
def delete(pokemon_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_pokemon(db, pokemon_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
