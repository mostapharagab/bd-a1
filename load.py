#!/bin/env python3
import sys
import pandas as pd
def read_dataset(dataset_path):
    dataset = pd.read_csv(dataset_path)
    return dataset

df = read_dataset('IRIS.csv')
sys.argv = ['dpre.py', df]
exec(open('dpre.py').read())

