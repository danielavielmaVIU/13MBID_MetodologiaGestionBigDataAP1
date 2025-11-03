import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path


def generate_eda_report():
    
    CSV_PATH = "data/raw/bank-additional-full.csv"  
    SEP = ";"                                       

    PROJECT_ROOT = Path(__file__).resolve().parents[1]  
    OUTPUT_DIR = PROJECT_ROOT / "docs" / "output" / "eda"
    OUTPUT_FILE = OUTPUT_DIR / "eda_report.html"

    df = pd.read_csv(CSV_PATH, sep=SEP)

    profile = ProfileReport(
        df,
        title="EDA – Análisis Exploratorio de Datos",
        explorative=True
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    profile.to_file(str(OUTPUT_FILE))

    print(f" Reporte EDA guardado en: {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    generate_eda_report()