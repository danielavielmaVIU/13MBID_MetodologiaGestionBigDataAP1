import pandas as pd
import pandera as pa
from pandera import DataFrameSchema, Column, Check
import pytest
import datetime


def datos():
    datos = pd.read_csv('data/raw/bank-additional-full.csv', sep=';')
    return datos


def test_esquema():
    df = datos()

    esquema = DataFrameSchema({
        "age": Column(pa.Int, nullable= False),
        "job": Column(pa.String, nullable= False),
        "marital": Column(pa.String, nullable= False),
        "education": Column(pa.String, nullable= False),
        "default": Column(pa.String, nullable= False),
        "housing": Column(pa.String, nullable= False),
        "loan": Column(pa.String, nullable= False),
        "contact": Column(pa.String, nullable= False),
        "month": Column(pa.String, nullable= False),
        "day_of_week": Column(pa.String, nullable= False),
        "duration": Column(pa.Int, nullable= False),
        "campaign": Column(pa.Int, nullable= False),
        "pdays": Column(pa.Int, nullable= False),
        "previous": Column(pa.Int, nullable= False), 
        "poutcome": Column(pa.String, nullable= False),
        "emp.var.rate": Column(pa.Float, nullable= False),
        "cons.price.idx": Column(pa.Float, nullable= False),
        "cons.conf.idx": Column(pa.Float, nullable= False),
        "euribor3m": Column(pa.Float, nullable= False),
        "nr.employed": Column(pa.Float, nullable= False),
        # target
        "y": Column(pa.String, Check.isin(["yes", "no"]), nullable=False),
    })
    
    esquema.validate(df, lazy=True)


    def test_basico(datos_banco):
        """Test inicial para verificar que el dataframe de datos_banco no esta vacío y contiene las columnas esperadas
        
        Agrs:
            datos_banco (pd.DataFrame): DataFrame que contiene los datos del banco.
        """
        df = datos_banco

        # Verficicar que el DataFRame no esta vacío
        assert not df.empty, "El DataFram está vacío."

        # Verficicar nulos
        assert df.isnull().sim().sum() == 0, "El DataFram contiene valores nulos."

        # Verificar cantidad de columnas
        assert df.shape[1] == 21, f"El DataFrame deberia tener 21 coumnas, pero tiene {df.shape}"

    if __name__ == "__name__":

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"docs/test_results/test_results_{timestamp}.txt"

        try:
            test_esquema(datos_banco())
            test_basico(datos_banco())
            print("Todos los tets pasaron exitosamente")
            with open(nombre_archivo, "w") as f:
                f.write("Todos los tets pasaron exitosamente \n")
        except AssertionError as e:
            print(f"Test fallido: {e}")
            with open(nombre_archivo, "w") as f:
                f.write("Test fallido: {e}\n")