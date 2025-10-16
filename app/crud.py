from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app import models, schemas

def list_pokemons(db: Session, skip: int, limit: int, q: str | None = None):
    stmt = select(models.Pokemon)
    if q:
        stmt = stmt.filter(models.Pokemon.name.ilike(f"%{q}%"))
    return db.execute(stmt.offset(skip).limit(limit)).scalars().all()

def count_pokemons(db: Session, q: str | None = None) -> int:
    stmt = select(func.count(models.Pokemon.id))
    if q:
        stmt = stmt.filter(models.Pokemon.name.ilike(f"%{q}%"))
    return db.execute(stmt).scalar_one()

def get_pokemon(db: Session, id_: int):
    return db.get(models.Pokemon, id_)

def create_pokemon(db: Session, payload: schemas.PokemonCreate):
    p = models.Pokemon(
        name=payload.name,
        height=payload.height,
        weight=payload.weight,
        types=",".join(payload.types) if payload.types else None,
        sprite=payload.sprite,
        external_id=payload.external_id,
    )
    db.add(p); db.commit(); db.refresh(p)
    return p

def update_pokemon(db: Session, id_: int, payload: schemas.PokemonUpdate):
    p = get_pokemon(db, id_)
    if not p:
        return None
    data = payload.model_dump()
    if isinstance(data.get("types"), list):
        data["types"] = ",".join(data["types"]) if data["types"] else None
    for k, v in data.items():
        setattr(p, k, v)
    db.commit(); db.refresh(p)
    return p

def delete_pokemon(db: Session, id_: int) -> bool:
    p = get_pokemon(db, id_)
    if not p:
        return False
    db.delete(p); db.commit()
    return True
