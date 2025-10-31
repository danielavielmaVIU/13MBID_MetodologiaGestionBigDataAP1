import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

INPUT_CSV = 'data/raw/bank-additional-full.csv'
OUTPUT_DIR = 'data/processed/'

def preprocess_data(input_path=INPUT_CSV, output_dir=OUTPUT_DIR):

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path, sep=';')
    
    # Adaptar nombres de columnas
    df.columns = df.columns.str.replace(".", "_")

    # Transformar los valores  "Unknown" a NaN
    df.replace ("unknown", np.nan , inplace=True)

    # Se elimina variable Default ya que tiene muchos valores desconocidos
    df.drop(columns=["default"], inplace=True)

    # Se hace un filtro para eliminar las filas que tiene valores nulos
    df.dropna(inplace=True)

    # Se hace filtro para elimnar las filas duplicadas
    df.drop_duplicates(inplace=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{output_dir}/bank-processed-full_{timestamp}.csv"

    df.to_csv(output_path, index=False)

    return df.shape

if __name__ == "__main__":
    dimensiones = preprocess_data()
    with open('docs/transformations.txt', 'w') as f:
        f.write("Transformaciones realizadas:\n")
        f.write("Se reemplazaron los valores 'unknown' por NaN\n")
        f.write("Se eliminaron filas con valores nulos\n")
        f.write("Se eliminaron filas duplicadas\n")
        f.write("Se elimino la variable default debido a la alta cantidad de valores nulos\n")
        f.write(f" Cantidad de filas finales: {dimensiones[0]}\n")
        f.write(f" Cantidad de columnas finales: {dimensiones[1]}\n")