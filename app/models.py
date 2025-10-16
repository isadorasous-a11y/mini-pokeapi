from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Pokemon(Base):
    __tablename__ = "pokemons"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    external_id: Mapped[int | None] = mapped_column(Integer, index=True)  # id da PokeAPI 
    name: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    height: Mapped[int | None] = mapped_column(Integer, nullable=True)
    weight: Mapped[int | None] = mapped_column(Integer, nullable=True)
    types: Mapped[str | None] = mapped_column(String(120), nullable=True)  # "grass,poison"
    sprite: Mapped[str | None] = mapped_column(String(255), nullable=True)
