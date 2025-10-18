import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from matplotlib.ticker import MultipleLocator

def visualizar_datos(fuente: str = "data/raw/bank-additional-full.csv", 
                     salida: str = "docs/figures/"):
    
    """Genera gráficos sobre el dataset y los exporta en directorio indicado
    Args: 
        fuente: (str, opcional): ruta al archivo de datos. Defaults to "/data/raw/bank-additional-full.csv".
        salida: (str, optcional): ruta al directorio de salida para los gráficos. Defaults to "/dodc/figures/".
    """
    # Crea directorio de salida si no existe
     
    Path(salida).mkdir(parents=True, exist_ok=True)

    # Leer archivo de datos
    datos = pd.read_csv(fuente, sep=';')

    #for var in datos.select_dtypes(include=['float64', 'int64']).columns.difference(['duration', 'euribor3m']):
    for var in datos.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure(figsize=(8,6))
        col = var
        order = datos[col].value_counts().index
        sns.countplot(x=col, data=datos)
        plt.title(f"Distribución de {col}")
        plt.xlabel(col)
        plt.ylabel("Cantidad")
        plt.xticks(fontsize=6, rotation=90)
        plt.yticks(fontsize=6)
        plt.savefig(f"{salida}/Distribucion_{col}.png")
        plt.close()    


    # Grafica Distribución de euribor3m
    dur = datos["duration"]             
    plt.figure(figsize=(8,6))
    sns.histplot(dur, bins=50, kde=False)
    plt.title("Distribución de duration (s)")
    plt.xlabel("Distribución de duration (s)")
    plt.ylabel("Cantidad", fontsize=10)
    ax = plt.gca()
    ax.tick_params(labelsize=8)
    plt.xticks(fontsize=6, rotation=90)
    plt.yticks(fontsize=6)
    ax.xaxis.set_major_locator(MultipleLocator(60)) 
    plt.tight_layout()
    plt.savefig(f"{salida}/Distribucion_duration")
    plt.close()

     # Gráfico Distribución de la variable euribor3m
    plt.figure(figsize=(8,6))
    sns.histplot(datos['euribor3m'], bins=50, kde=True, color='steelblue')
    plt.title("Distribución de euribor3m")
    plt.xlabel("Tasa EURIBOR a 3 meses")
    plt.ylabel("Cantidad", fontsize=10)
    plt.tick_params(axis='x', labelsize=8)
    plt.tight_layout()
    plt.savefig(f"{salida}/Distribucion_euribor3m.png")
    plt.close()

    # Gráfico Distribución de la variable objetivo
    plt.figure(figsize=(6,4))
    sns.countplot(x="y", data=datos)
    plt.title("Distribución de la variable objetivo (suscripción al depósito)")
    plt.xlabel("¿Suscribió un depósito a plazo?")
    plt.ylabel("Cantidad de clientes")
    plt.savefig(f"{salida}/Distribución_target.png")
    plt.close()


    matriz = datos.select_dtypes(include=['number']).corr()
    # Grafica de la matriz
    plt.figure(figsize=(10, 5))
    sns.heatmap(matriz, annot=True, fmt=".2f", cmap='coolwarm', square=True, annot_kws={"size": 6}, cbar_kws={'shrink': 0.8})
    plt.title('Matriz de Correlación entre variables numéricas')
    plt.tight_layout()
    plt.savefig(f"{salida}/Distribución_target.png")
    plt.close()


if __name__ == "__main__":
    visualizar_datos()

