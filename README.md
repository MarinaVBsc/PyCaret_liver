# PyCaret_liver
Predicción de enfermedad hepática mediante modelos automáticos de Machine Learning con Pycaret

# Descripción 
El proyecto consiste en utilizar un dataset clínico de pacientes con posibles alteraciones hepáticas para construir modelos predictivos con PyCaret que clasifiquen si un paciente presenta enfermedad hepática o no.

# Objetivos
- Analizar datos clínicos relacionados con funciones hepáticas (ALT, AST, bilirrubina, albúmina, etc.).
- Entrenar modelos de Machine Learning con PyCaret.
- Comparar automáticamente decenas de algoritmos.
- Seleccionar y exportar el mejor modelo.
- Generar isights clínicos con interpretabilidad SHAP.

# Flujo del proyecto
1. Carga del dataset (CSV)
2. Preprocesamiento automático con PyCaret
3. Setup de clasificación (pycaret.classification)
4. Comparación de modelos (compare_models())
5. Tuning del mejor modelo
6. Interpretabilidad SHAP (intepret_model())
7. Exportación del modelo final
