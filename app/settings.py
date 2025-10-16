from pydantic import BaseModel
import os

class Settings(BaseModel):
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    PAGE_SIZE_DEFAULT: int = int(os.getenv("PAGE_SIZE_DEFAULT", "20"))
    PAGE_SIZE_MAX: int = int(os.getenv("PAGE_SIZE_MAX", "50"))

settings = Settings()
