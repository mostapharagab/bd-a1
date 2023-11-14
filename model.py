#!/bin/env python3
import pandas as pd
import sys
from sklearn.cluster import KMeans

def apply_kmeans(data, columns, k, output_file):

    # Select the specified columns from the DataFrame
    selected_data = data[columns]

    # Initialize K-means with the specified number of clusters (k)
    kmeans = KMeans(n_clusters=k, random_state=0)

    # Fit the K-means model to the data
    kmeans.fit(selected_data)

    # Get cluster labels for each data point
    cluster_labels = kmeans.labels_

    # Count the number of records in each cluster
    cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

    # Save the cluster counts to a text file
    cluster_counts.to_csv(output_file, header=False, sep='\t', index_label='Cluster')

    print(f"K-means clustering completed. Cluster counts saved in '{output_file}'.")



dataset_path = sys.argv[1]
pca_data = pd.read_csv(dataset_path)
kmeans_columns = ['PC1', 'PC2']  
k = 3
output_file = 'k.txt'
apply_kmeans(pca_data, kmeans_columns, k, output_file)
