"""
schemas.py — nombres canónicos y mapeos de columnas por fuente.
Sirve para normalizar datasets heterogéneos (IMF, WB, OWID...).
"""
from typing import Dict

CANON = {
    "country": "country",
    "iso3": "iso3",
    "year": "year",
    "indicator": "indicator",
    "value": "value",
    # añade aquí otros campos canónicos (region, unit, source...)
}

IMF_MAP: Dict[str, str] = {
    # "Country Name": "country",
    # "ISO3": "iso3",
    # "Year": "year",
    # "Indicator Name": "indicator",
    # "Value": "value",
    # Ajusta cuando sepamos los nombres reales de tu CSV
}

def rename_columns(df, mapping: Dict[str, str]):
    return df.rename(columns=mapping)
