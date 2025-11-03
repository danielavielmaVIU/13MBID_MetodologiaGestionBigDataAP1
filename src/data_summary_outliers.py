import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def resume_outliers(fuente: str = "data/raw/bank-additional-full.csv", 
                    log_path: str = "docs/resumen_outliers.txt"):
    """
    Genera gráficos sobre el dataset para outliers y los exporta en el directorio indicado.
    Args: 
        fuente (str): ruta al archivo de datos.
        log_path (str): ruta al archivo de texto d
        onde se guardará el resumen.
    """

    # Crear directorio de salida si no existe
    Path(log_path).parent.mkdir(parents=True, exist_ok=True)

    # Leer archivo de datos
    df = pd.read_csv(fuente, sep=';')

    # --- Análisis de outliers ---
    variables_con_outliers = []
    log_lines = []  # acumulador de mensajes

    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1  # rango intercuartílico

        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        outliers = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]

        if not outliers.empty and col != 'y':
            msg = f"{col}: {len(outliers)} outliers encontrados"
            log_lines.append(msg)
            variables_con_outliers.append(col)

    # --- Guardar log en archivo ---
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("Resumen de Outliers detectados:\n")
        f.write("--------------------------------\n")
        if log_lines:
            for line in log_lines:
                f.write(line + "\n")
        else:
            f.write("No se detectaron outliers en las variables numéricas.\n")

    print(f"\nResumen de detalle de outliers guardado en: {log_path}")

if __name__ == "__main__":
    resume_outliers()