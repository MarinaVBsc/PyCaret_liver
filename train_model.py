from pycaret.classification import *
import pandas as pd

# Cargar el dataset
df= pd.read_csv("liver_patient_data.csv)

# Iniciar entorno

clf = setup(
      data=df,
      target='Liver_Disease',
      normalize=True,
      session_id=42
)

# Comparar modelos
best_model = compare_models()

# Afinar mejor modelo
tuned_model = tune_model(best_model)

# Intepretabilidad
interpret_model(tuned_model)

# Guardar_modelo
save_model(tuned_model), "models/modelo_hepatico_pycaret")
