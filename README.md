# 🏋️ Limpieza de datos — Clientes de un gimnasio

Práctica de **limpieza de datos y análisis exploratorio** sobre el registro de clientes de un gimnasio con tres sedes en Santo Domingo (**Naco, Piantini y Gazcue**). Desarrollada en el **Mes 4 · Semana 2** de *Data Science para IA* (Talendig).

El dataset llega con problemas típicos de datos reales: información incompleta, registros repetidos por error y una columna numérica que en realidad es una categoría. El objetivo es resolver cada uno **justificando la decisión**, no solo aplicando código.

## 📓 Notebook
👉 [`notebooks/01_limpieza_datos.ipynb`](notebooks/01_limpieza_datos.ipynb)

## 🔍 Qué se hace

| Problema | Decisión | Por qué |
|---|---|---|
| `Edad` con 17.46 % de nulos | Rellenar con la **mediana** | Es numérica y hay valores extremos (clientes de 90+ años); la mediana no se deja arrastrar por ellos |
| `Sucursal` con 3.17 % de nulos | Rellenar con la **moda** | Es categórica y solo faltan 2 filas |
| `Email` con 74.60 % de nulos | **Eliminar la columna** | Un correo no se puede deducir de otras columnas, y el vacío existe porque el gimnasio empezó a pedirlo hace poco |
| 3 filas duplicadas | `drop_duplicates()` | Se eliminan antes de imputar para no borrar filas por error |
| `Plan` guardada como `int64` | Convertir a `category` | Sus valores (1 = Básico, 2 = Premium, 3 = VIP) son etiquetas, no cantidades |

## 📊 Resultados

- **63 filas, 7 columnas** → **60 filas, 6 columnas**, sin nulos ni duplicados.
- Al excluir a los clientes mayores de 85 años, la **media de edad baja** (de 46.50 a 44.05) mientras que la **mediana no cambia** (47). La mediana es más robusta ante valores extremos.
- Incluye la reflexión final: por qué `Sucursal` y `Email` requieren estrategias distintas y qué precauciones tomar antes de usar estos datos para predecir cancelaciones (variable objetivo, imputación y *data leakage*).

## 📂 Estructura

```
gym-data-cleaning/
├── data/
│   ├── clientes_gimnasio.csv           # datos originales (63 filas, 7 columnas)
│   └── clientes_gimnasio_limpio.csv    # resultado final (60 filas, 6 columnas)
├── notebooks/
│   └── 01_limpieza_datos.ipynb
├── requirements.txt
└── README.md
```

## 🛠️ Tecnologías
Python 3 · pandas · Matplotlib · Jupyter

## ▶️ Cómo ejecutarlo

```bash
git clone https://github.com/offxcialchris/gym-data-cleaning.git
cd gym-data-cleaning
pip install -r requirements.txt
jupyter notebook notebooks/01_limpieza_datos.ipynb
```

## ⚠️ Limitaciones

- Rellenar edades con la mediana no recupera la edad real de cada cliente y suaviza la distribución.
- Rellenar sucursales con la moda asume que esos clientes pertenecen a la sede más frecuente.
- `drop_duplicates()` solo detecta filas **exactamente** iguales.
- Las edades mayores a 85 se usaron solo para comparar, no como regla de limpieza.

## 👤 Autor
**Chris Nelson** · [@offxcialchris](https://github.com/offxcialchris)