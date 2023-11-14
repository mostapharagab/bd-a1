#!/bin/env python3
import pandas as pd
import sys
import subprocess

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.preprocessing import KBinsDiscretizer


def clean_iris_dataset(iris_data):
    #DATA CLEANING
    # Check for missing values and remove rows with missing values
    iris_data.dropna(inplace=True)
    # Remove duplicate rows
    iris_data.drop_duplicates(inplace=True)

    #DATA TRANSFORMATION

    # Standardize the numerical features (Z-score normalization)
    numerical_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    scaler = StandardScaler()
    iris_data[numerical_features] = scaler.fit_transform(iris_data[numerical_features])

    # Encode the 'species' column to numerical labels (0, 1, 2)
    label_encoder = LabelEncoder()
    iris_data['species'] = label_encoder.fit_transform(iris_data['species'])
    # Extract the feature columns (excluding 'species')
    X = iris_data.drop('species', axis=1)

    # Specify the number of principal components (PCs) you want to retain
    n_components = 2  # Adjust as needed

    # Initialize PCA with the number of components
    pca = PCA(n_components=n_components)

    # Fit and transform the data
    pca_result = pca.fit_transform(X)

    # Create a DataFrame with the principal components
    pca_df = pd.DataFrame(data=pca_result, columns=[f'PC{i + 1}' for i in range(n_components)])

    # Perform data discretization on the PCA result using the quantile-based strategy
    n_bins = 3  # Number of bins or intervals (adjust as needed)
    strategy = 'quantile'  # Binning strategy ('quantile' for quantile-based binning)

    discretizer = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy=strategy)
    discretized_pca_result = discretizer.fit_transform(pca_result)

    # Create a DataFrame with discretized PCA components
    column_names = [f'PC{i + 1}' for i in range(n_components)]
    discretized_pca_df = pd.DataFrame(data=discretized_pca_result, columns=column_names)

    # Add the 'species' column back
    discretized_pca_df['species'] = iris_data['species']
    discretized_pca_df.dropna(inplace=True)
    output_csv_path = 'res_dpre.csv'
    discretized_pca_df.to_csv(output_csv_path, index=False)

    return discretized_pca_df



iris_data = sys.argv[1]
df = clean_iris_dataset(iris_data)
sys.argv = ['eda.py', df]
exec(open('eda.py').read())








