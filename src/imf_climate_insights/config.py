"""
config.py — configuración central del proyecto.
Lee variables desde el entorno y .env cuando exista.
"""
from dataclasses import dataclass
from pathlib import Path
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

@dataclass(frozen=True)
class Settings:
    PROJECT_NAME: str = "IMF Climate Insights"
    ENV: str = os.getenv("ENV", "dev")
    IMF_API_KEY: str = os.getenv("IMF_API_KEY", "")
    WB_API_BASE: str = "https://api.worldbank.org/v2/"
    ROOT: Path = Path(__file__).resolve().parents[2]
    DATA: Path = ROOT / "data"

settings = Settings()
