import pandas as pd
import pandera as pa
from pandera import DataFrameSchema, Column, Check
import pytest

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