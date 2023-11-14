#!/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import sys


def create_scatter_plot(datapath, output_path):
    data = datapath
    plt.figure(figsize=(8, 6))  # Set the figure size

    # Create a scatter plot of 'PC1' and 'PC2'
    plt.scatter(data['PC1'], data['PC2'], c=data['species'], cmap='viridis', alpha=0.5)

    # Set labels for the x and y axes
    plt.xlabel('PC1')
    plt.ylabel('PC2')

    # Set the title of the plot
    plt.title("Scatter Plot")

    # Save the plot as "vis.png"
    plt.savefig(output_path)


pca_data = sys.argv[1]
output_path = 'vis.png'
create_scatter_plot(pca_data, output_path)
sys.argv = ['model.py', 'res_dpre.csv']
exec(open('model.py').read())
