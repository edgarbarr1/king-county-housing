# Exploratory Notebooks

This directory contains unpolished exploratory data analysis (EDA) notebooks.

## database.ipynb ##

This notebook joins the raw files **"EXTR_LookUp.csv, EXTR_Parcel.csv, EXTR_ResBldg.csv, EXTR_RPSale.csv"** located in `data/raw/` and creates a database containing a table per file.

## eda_notebook.ipynb ##

This notebook converts the database file `data.db` located in `data/processed` into a pandas DataFrame in order to more efficiently explore the data contained in the merged DataFrame. 

With the DataFrame I proceeded to start dropping columns and rows that either contained no data or did not provide value to the modeling that would subsequently be created after. The main columns that were kept were continuous data in order to find the ones that were the most correlated in the `stats.ipynb`