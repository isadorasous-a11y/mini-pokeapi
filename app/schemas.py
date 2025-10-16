from pydantic import BaseModel, Field

class PokemonBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=80)
    height: int | None = None
    weight: int | None = None
    types: list[str] = []
    sprite: str | None = None
    external_id: int | None = None

class PokemonCreate(PokemonBase):
    pass

class PokemonUpdate(PokemonBase):
    pass

class PokemonOut(PokemonBase):
    id: int
    class Config:
        from_attributes = True
