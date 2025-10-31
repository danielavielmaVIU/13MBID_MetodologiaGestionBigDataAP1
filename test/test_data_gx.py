import pandas as pd

def test_great_expectation():
    
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep = ';')

    results = {
        "success": True,
        "expectations": [],
        "statistics": {"success_count": 0, "total_count": 0}
    }


    def add_expectation(expectation_name, condition, message=""):
        results["statistics"]["total_count"] += 1     
        if condition:      
            results["statistics"]["total_count"] += 1    
            results["expectations"].append({
                "expectation": expectation_name,
                "success": True
            })
        else:
            results["success"] = False
            results["expectations"].append({
                "expectation": expectation_name,
                "success": False,
                "message": message
            })

    add_expectation(
        "age_range",
        df["age"].between(18,100).all(),
        "La columna 'age' no está en el rango esperado (18-100)"
    )
                            
    add_expectation(
        "target_values",
        df["y"].isin(["yes", "no"]).all(),
        "La columna 'y' contiene vallores no válidos"
    ) 

    add_expectation(
        "pdays_positivos",
        (df["pdays"] >= 0).all(),
        "La columna 'pdays' contiene vallores negativos"
    )   
    add_expectation(
        "marital",
        df["marital"].isin(["married","divorced","single"]).all(),
        "La columna 'marital' contiene valores no válidos"
    )