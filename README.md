# Limpieza-BDD-ecommerce-V2
# 🛒 Limpieza y preparación de datos de Ecommerce

Este proyecto consiste en la **limpieza y preparación de un dataset de transacciones de un ecommerce** (descargado de Kaggle).  
El objetivo es demostrar habilidades en **data wrangling, limpieza de datos y preparación para análisis exploratorio**.

---

## 📊 Dataset
- **Fuente:** Kaggle – Online Retail Dataset
- **Tamaño inicial:** 541,909 registros y 8 columnas
- **Campos principales:**
  - `InvoiceNo`: Número de factura
  - `StockCode`: Código de producto
  - `Description`: Descripción del producto
  - `Quantity`: Cantidad vendida
  - `InvoiceDate`: Fecha de la transacción
  - `UnitPrice`: Precio unitario
  - `CustomerID`: Identificador del cliente
  - `Country`: País

---

## 🧹 Proceso de limpieza

1. **Exploración inicial**
   - Revisión de nulos, duplicados y dimensiones.
   - Identificación de outliers en precios y cantidades.

2. **Tratamiento de valores nulos**
   - `Description` → se reemplazó por `"Unknown"`.
   - `CustomerID` → se mantuvo como `NaN` (cliente no identificado).

3. **Limpieza de texto en descripciones**
   - Eliminación de caracteres especiales y signos de interrogación.
   - Estandarización en formato `Title Case`.

4. **Manejo de duplicados**
   - Eliminación de filas duplicadas exactas.

5. **Valores anómalos**
   - `Quantity < 0` → registros de devoluciones (guardados en dataset aparte).
   - `UnitPrice <= 0` → registros anómalos considerados en data quality report.

6. **Normalización de columnas**
   - Conversión a `snake_case`.
   - Renombrado de columnas clave (ejemplo: `invoiceno → invoice_no`).

---

## 📂 Resultados

Se generaron 3 archivos principales:

- `ecommerce_clean_master.csv` → Dataset completo, limpio y normalizado.  
- `ecommerce_sales.csv` → Solo transacciones de ventas.  
- `ecommerce_returns.csv` → Solo devoluciones.  

---

## ⚙️ Tecnologías utilizadas
- Python 🐍
- Pandas
- Numpy
- Regex (expresiones regulares)

---

## 🚀 Próximos pasos
- Realizar **análisis exploratorio (EDA)** sobre ventas y devoluciones.
- Generar **dashboards en Power BI o Tableau** para visualizar métricas clave.
- Construir un **modelo de segmentación de clientes** (RFM Analysis).

---

## 📌 Autor
**Pedro Rodríguez**  
Apasionado por el análisis de datos y la visualización de información.  
📫 Conéctame en [LinkedIn](www.linkedin.com/in/pedrojrodriguezs) 
