"""
etl.py — funciones para cargar, limpiar y normalizar datasets (IMF y otros).
"""
from pathlib import Path
import pandas as pd
from .io import path_raw, path_processed, ensure_dir
from .schemas import rename_columns, IMF_MAP
from .logging import get_logger

log = get_logger()

def load_imf_csv(filename: str) -> pd.DataFrame:
    """Carga un CSV exportado del IMF desde data/raw/."""
    fp = path_raw(filename)
    log.info(f"Cargando IMF CSV: {fp.name}")
    df = pd.read_csv(fp)
    return df

def clean_imf(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica: strip textos, convertir tipos, etc."""
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()
    return df

def normalize_imf(df: pd.DataFrame) -> pd.DataFrame:
    """Renombra columnas IMF a nombres canónicos usando IMF_MAP."""
    if IMF_MAP:
        df = rename_columns(df, IMF_MAP)
    else:
        log.warning("IMF_MAP está vacío; define los mapeos en schemas.py")
    return df

def save_processed(df: pd.DataFrame, name: str) -> Path:
    """Guarda un derivado en data/processed/ con nombre given."""
    out = ensure_dir(path_processed(name))
    df.to_csv(out, index=False)
    log.info(f"Guardado derivado: {out}")
    return out
