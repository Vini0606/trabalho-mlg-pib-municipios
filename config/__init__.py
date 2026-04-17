"""Config package for easy imports"""
from .settings import (
    PROJECT_ROOT,
    DATA_DIR,
    DATA_RAW_DIR,
    DATA_PROCESSED_DIR,
    PIB_MUNICIPIOS_RAW,
    PIB_MUNICIPIOS_PROCESSED,
    REPORTS_DIR,
    FIGURES_DIR,
    NOTEBOOKS_DIR,
    SRC_DIR,
    get_data_files,
)

__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR",
    "DATA_RAW_DIR",
    "DATA_PROCESSED_DIR",
    "PIB_MUNICIPIOS_RAW",
    "PIB_MUNICIPIOS_PROCESSED",
    "REPORTS_DIR",
    "FIGURES_DIR",
    "NOTEBOOKS_DIR",
    "SRC_DIR",
    "get_data_files",
]
