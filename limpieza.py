#=======================================================================================================
# 1. Importar librerias
#=======================================================================================================
import pandas as pd
import numpy as np
import re
#=======================================================================================================
# 2. Cargar el conjunto de datos
#=======================================================================================================
df=pd.read_csv(r'C:\Users\pedro\OneDrive\Documentos\Proyectos finales\e-commerce\Base inicial\ecommerce.csv', encoding='latin-1')

print('Dimensiones iniciales:', df.shape)
df.head()
#=======================================================================================================
# 3. Exploración inicial
#=======================================================================================================
print("\nInformación general:")
df.info()

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nDuplicados exactos:", df.duplicated().sum())
#=======================================================================================================
# 4. Limpieza de valores nulos
#=======================================================================================================
# CustomerID tiene muchos nulos → se dejan como NaN (no se reemplazan con 0 porque son IDs)
# Description → reemplazar nulos con 'Unknown'
df["Description"].fillna("Unknown", inplace=True)

print("Nulos después de limpiar:")
print(df.isnull().sum())
#=======================================================================================================
# 5. Limpieza de texto (columna 'Description')
#=======================================================================================================
def clean_description(text):
    if pd.isna(text):
        return "Unknown"
    # Quitar signos de interrogación y caracteres extraños
    text = re.sub(r"[^\x00-\x7F]+", " ", str(text))   # elimina caracteres no ASCII
    text = re.sub(r"\?", "", text)                    # elimina "?"
    text = text.strip().title()                       # quita espacios y estandariza capitalización
    return text

df["Description"] = df["Description"].apply(clean_description)
#=======================================================================================================
# 6. Limpieza de duplicados 
#=======================================================================================================
print("Duplicados exactos:", df.duplicated().sum())

# Eliminar duplicados
df.drop_duplicates(inplace=True)
print("Duplicados después de limpiar:", df.duplicated().sum())
#=======================================================================================================
# 7. Valores anómalos en 'Quantity' y 'Price'
#=======================================================================================================
print("Cantidad de valores negativos en Quantity:", (df["Quantity"] < 0).sum())
print("Cantidad de precios <= 0:", (df["UnitPrice"] <= 0).sum())

# Registros negativos se consideran devoluciones → se guardan en dataset separado
returns = df[df["Quantity"] < 0]
sales = df[df["Quantity"] > 0]

print("Ventas:", sales.shape)
print("Devoluciones:", returns.shape)
#=======================================================================================================
# 8. Normalizar nombres de columnas
#=======================================================================================================
df.columns = df.columns.str.strip().str.lower()

df.rename(columns={
    "invoiceno": "invoice_no",
    "stockcode": "stock_code",
    "description": "product_description",
    "invoicedate": "invoice_date",
    "unitprice": "unit_price",
    "customerid": "customer_id",
    "country": "country"
}, inplace=True)

print("Columnas normalizadas:", df.columns.tolist())
#=======================================================================================================
# 9. Guardar datasets finales
#=======================================================================================================
df.to_csv("ecommerce_clean_master.csv", index=False) # Dataset completo, limpio y normalizado.
sales.to_csv("sales_data.csv", index=False) # Solo transacciones de ventas.
returns.to_csv("returns_data.csv", index=False) # Solo transacciones de devoluciones.

print("Archivos guardados con éxito:")
print("- ecommerce_clean_master.csv")
print("- sales_data.csv")
print("- returns_data.csv")