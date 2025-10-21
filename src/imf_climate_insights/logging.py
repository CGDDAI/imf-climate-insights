"""
logging.py — configuración de logging uniforme para el proyecto.
"""
import logging
import sys

def get_logger(name: str = "imf_climate_insights", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s: %(message)s",
                            datefmt="%H:%M:%S")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
