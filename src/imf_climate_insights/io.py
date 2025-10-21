"""
io.py — utilidades de entrada/salida y rutas de datos.
Centraliza paths para no hardcodear rutas en notebooks ni scripts.
"""
from pathlib import Path

# Ruta raíz del repo (dos niveles arriba de este archivo)
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

def path_raw(*parts) -> Path:
    return DATA / "raw" / Path(*parts)

def path_interim(*parts) -> Path:
    return DATA / "interim" / Path(*parts)

def path_processed(*parts) -> Path:
    return DATA / "processed" / Path(*parts)

def path_external(*parts) -> Path:
    return DATA / "external" / Path(*parts)

def ensure_dir(p: Path) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    return p
