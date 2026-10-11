# practica_talendig_mes4_sem2_gimnasio

# Gym Data Cleaning and Exploratory Data Analysis

A Python data analysis project focused on data cleaning, missing-value treatment, duplicate detection, statistical analysis, and exploratory data analysis (EDA) using a gym customer dataset.

This project was developed as part of my Python and data analysis training at **Talendig** (Month 4, Week 2) and further organized and documented for my learning portfolio.

## Project Overview

The dataset contains customer records from a gym with three branches in Santo Domingo, Dominican Republic: Naco, Piantini, and Gazcue.

Like many real-world datasets, it contains missing values, duplicate records, and a numeric column that represents a category rather than a continuous measurement.

The project explores how to identify these issues, clean the data, and justify preprocessing decisions.

## Objectives

- Inspect the dataset's structure and data types.
- Identify and quantify missing values.
- Handle missing values according to the meaning and usefulness of each column.
- Detect and remove duplicate records.
- Convert the `Plan` column into a categorical data type.
- Compare the mean and median of customer ages.
- Analyze how customers older than 85 affect descriptive statistics.
- Discuss precautions required before using the data for a future machine learning model.

## Project Structure

```text
gym-data-cleaning-eda/
├── data/
│   ├── clientes_gimnasio.csv
│   └── clientes_gimnasio_limpio.csv
├── notebooks/
│   ├── 01_limpieza_datos.ipynb
│   └── 02_analisis_y_reflexiones.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

## Data Cleaning Process

### 1. Initial inspection

Examined the dataset's dimensions, first rows, data types, and general structure.

### 2. Missing values

- **`Edad`:** missing values were filled using the median.
- **`Sucursal`:** missing values were filled using the most frequent category (mode).
- **`Email`:** excluded from the analytical dataset because a large proportion of values were missing and the project context explains that email collection started later.

These decisions were made for this exercise and should be reconsidered if the dataset is used for a different business objective.

### 3. Duplicate records

Identified and removed duplicate rows from the dataset.

### 4. Data types

Converted `Plan` into a categorical data type because its values represent membership categories rather than continuous numerical measurements.

### 5. Statistical analysis

Compared the mean and median of customer ages, including all customers and excluding those older than 85 for a separate sensitivity analysis. The older customers were not automatically classified as invalid records.

## Key Questions

- How sensitive are the mean and median to extreme age values?
- Why should missing values in `Sucursal` and `Email` be treated differently?
- What precautions are necessary before using customer data to predict membership cancellations?

The findings are documented in the notebooks and should be interpreted using the actual outputs produced by running the analysis.

## Technologies Used

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/offxcialchris/gym-data-cleaning-eda.git
cd gym-data-cleaning-eda
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

On Ubuntu/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks inside the `notebooks/` directory and execute their cells in order.

**Note:** The notebooks expect the CSV files to be available in the `data/` directory. If you change the directory structure, update the file paths accordingly.

## Limitations and Future Improvements

- Validate whether missing branch values should be imputed or investigated further.
- Reassess the treatment of `Email` if it becomes relevant to a future business question.
- Investigate unusual age values using domain knowledge rather than removing them automatically.
- Develop a documented preprocessing pipeline if the dataset is later used for machine learning.
- Obtain reliable historical cancellation labels before attempting to train a membership-churn prediction model.

## Learning Context

This project originated as an academic exercise in the Talendig training program. It is part of my ongoing learning journey in Python, data analysis, and machine learning.

## Author

**Chris Nelson**

GitHub: [@offxcialchris](https://github.com/offxcialchris)