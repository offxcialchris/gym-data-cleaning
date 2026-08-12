import pandas as pd
from pandas import DataFrame

# Mantiene 'object' en vez de 'str'
# (se explica en una clase futura)
pd.options.future.infer_string = False


# ==========================================
# PASO 1 — CARGAR Y EXPLORAR EL DATASET
# ==========================================

# El archivo .py está dentro de notebooks/
# El dataset está dentro de data/
df: DataFrame = pd.read_csv('../data/clientes_gimnasio.csv')

print('Forma del dataset:', df.shape)

print('\nPrimeras filas:')
print(df.head())

print('\nTipos de datos:')
print(df.dtypes)


# ==========================================
# PASO 2 — DIAGNOSTICAR VALORES NULOS
# ==========================================

print('\nValores nulos:')
print(df.isnull().sum())

print('\nPorcentaje de valores nulos:')
print((df.isnull().sum() / len(df) * 100).round(2))


# ==========================================
# PASO 3 — TRATAR LOS VALORES NULOS
# ==========================================

# Edad:
# Es una variable numérica.
# Utilizamos la mediana para rellenar los valores nulos.

df['Edad'] = df['Edad'].fillna(df['Edad'].median())


# Sucursal:
# Es una variable categórica.
# Tiene pocos valores nulos.
# Utilizamos la moda, es decir, el valor más frecuente.

df['Sucursal'] = df['Sucursal'].fillna(df['Sucursal'].mode()[0])


# Email:
# Tiene demasiados valores nulos.
# No podemos adivinar correos que nunca fueron registrados.
# Por eso eliminamos la columna completa.

df = df.drop(columns=['Email'])


# Verificamos los nulos restantes

print('\nNulos restantes:')
print(df.isnull().sum())

print('\nTotal de nulos restantes:', df.isnull().sum().sum())

print('\nForma después de tratar los nulos:', df.shape)


# ==========================================
# PASO 4 — ELIMINAR DUPLICADOS
# ==========================================

print('\nFilas antes:', len(df))

df = df.drop_duplicates()

print('Filas después:', len(df))


# ==========================================
# PASO 5 — CORREGIR TIPO DE DATOS
# ==========================================

# Plan tiene valores 1, 2 y 3.
# Aunque aparecen como números, representan categorías:
# 1 = Básico
# 2 = Premium
# 3 = VIP
#
# Por eso lo convertimos a category.

df['Plan'] = df['Plan'].astype('category')

print('\nTipos de datos después de convertir Plan:')
print(df.dtypes)


# ==========================================
# REFLEXIÓN 1 — MEDIA Y MEDIANA
# ==========================================

# Calculamos la media y mediana de Edad
# incluyendo a todos los clientes.

print('\n===== EDAD CON TODOS LOS CLIENTES =====')

media = df['Edad'].mean()
mediana = df['Edad'].median()

print('Media:', media)
print('Mediana:', mediana)


# Ahora creamos un DataFrame temporal
# sin clientes mayores de 85 años.
#
# IMPORTANTE:
# No modificamos df.
# Solo creamos df_sin_outliers para hacer la comparación.

df_sin_outliers = df[df['Edad'] <= 85]

print('\n===== EDAD SIN CLIENTES MAYORES DE 85 =====')

media_sin_outliers = df_sin_outliers['Edad'].mean()
mediana_sin_outliers = df_sin_outliers['Edad'].median()

print('Media sin >85:', media_sin_outliers)
print('Mediana sin >85:', mediana_sin_outliers)


# ==========================================
# GUARDAR DATASET LIMPIO
# ==========================================

# Guardamos el DataFrame limpio.
# index=False evita guardar el índice de pandas
# como una columna adicional.

df.to_csv(
    '../data/clientes_gimnasio_limpio.csv',
    index=False
)

print('\n==========================================')
print('DATASET LIMPIO GUARDADO CORRECTAMENTE')
print('==========================================')

print('Forma final:', df.shape)
print('Archivo: ../data/clientes_gimnasio_limpio.csv')
print('Nulos restantes:', df.isnull().sum().sum())