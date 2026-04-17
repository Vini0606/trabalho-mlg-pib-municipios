"""
Configuration and path settings for the project.
All data file paths are defined here for easy access from notebooks and scripts.
"""

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# ====== DATA PATHS ======
DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"

# ====== RAW DATA FILES ======
PIB_MUNICIPIOS_RAW = DATA_RAW_DIR / "PIB dos Municípios - base de dados 2010-2023.xlsx"

# ====== PROCESSED DATA FILES ======
PIB_MUNICIPIOS_PROCESSED = DATA_PROCESSED_DIR / "pib_municipios_limpo.csv"

# ====== REPORTS PATHS ======
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ====== NOTEBOOKS PATHS ======
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# ====== SOURCE CODE PATHS ======
SRC_DIR = PROJECT_ROOT / "src"


def get_data_files():
    """
    Returns a dictionary with all data file paths.
    Useful for quick reference in notebooks.
    """
    return {
        "pib_municipios_raw": PIB_MUNICIPIOS_RAW,
        "data_raw_dir": DATA_RAW_DIR,
        "data_processed_dir": DATA_PROCESSED_DIR,
    }


if __name__ == "__main__":
    # Quick test to verify all paths
    print("=" * 50)
    print("PROJECT PATHS CONFIGURATION")
    print("=" * 50)
    print(f"\nProject Root: {PROJECT_ROOT}")
    print(f"\nDATA DIRECTORIES:")
    print(f"  Raw Data: {DATA_RAW_DIR}")
    print(f"  Processed Data: {DATA_PROCESSED_DIR}")
    print(f"\nRAW DATA FILES:")
    print(f"  PIB Municipios: {PIB_MUNICIPIOS_RAW}")
    print(f"  File exists: {PIB_MUNICIPIOS_RAW.exists()}")
    print(f"\nOTHER DIRECTORIES:")
    print(f"  Reports: {REPORTS_DIR}")
    print(f"  Notebooks: {NOTEBOOKS_DIR}")
    print(f"  Source: {SRC_DIR}")
