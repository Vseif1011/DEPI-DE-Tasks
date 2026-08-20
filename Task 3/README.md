# Task 3: Supermarket Sales Analysis

## Project Overview

This task focuses on profiling and analyzing the `SuperMarket.csv` dataset using Python and Pandas. The work was completed in `Task_3.ipynb`, where the dataset was explored, cleaned, and summarized to better understand its structure and quality before any business analysis.

The notebook demonstrates a practical data-profiling workflow, including checking the dataset schema, identifying missing values, detecting duplicates, and reviewing descriptive statistics. It also includes basic data exploration to support further analysis of supermarket sales performance and customer behavior.

## Dataset

The analysis is based on:

- `SuperMarket.csv`

## Tools Used

- Python
- Pandas
- Jupyter Notebook

## What Was Done in `Task_3.ipynb`

The notebook covers the following steps:

1. Loaded the supermarket sales dataset into a Pandas DataFrame.
2. Displayed a preview of the data to understand the available columns and sample records.
3. Inspected column names, data types, and non-null counts using `df.info()`.
4. Checked the number of missing values in each column.
5. Identified duplicate rows in the dataset.
6. Generated descriptive statistics for the numeric columns using `df.describe()`.
7. Explored the distribution of categorical values such as customer type.

## Data Quality Observations

During profiling, a few data quality issues were identified, including:

- Missing values in some columns such as `Unit price` and `Date`
- Inconsistent column formatting and spacing in some column names
- Duplicate records present in the dataset
- Mixed data types in columns that may require further cleaning

These observations help establish the next steps for cleaning and preparing the dataset for analysis.

## Outcome

By the end of this task, the dataset had been profiled and its quality issues were clearly identified. This provides a solid foundation for any future cleaning, transformation, and analysis work in the supermarket sales project.
