#!/bin/env python3
import pandas as pd
import sys



def generate_eda_insights(data, output_file):

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Insight 1: Summary statistics
        insight_1 = data.describe()
        f.write("Insight 1: Summary Statistics\n")
        f.write(insight_1.to_string())
        f.write("\n\n")

        # Insight 2: Unique values in each column
        insight_2 = data.nunique()
        f.write("Insight 2: Unique Values in Each Column\n")
        f.write(insight_2.to_string())
        f.write("\n\n")

        # Insight 3: Data types of columns
        insight_3 = data.dtypes
        f.write("Insight 3: Data Types of Columns\n")
        f.write(insight_3.to_string())
    print("EDA insights have been generated and saved in a single text file.")



df = sys.argv[1]
generate_eda_insights(df , 'eda-in-1.txt')
sys.argv = ['vis.py', df]
exec(open('vis.py').read())

