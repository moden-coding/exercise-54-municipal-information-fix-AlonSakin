#!/usr/bin/env python3

from os import sep
import pandas as pd

def main():
    municipalInfo = pd.read_csv("src/municipal.tsv", sep="\t")

    shapeInfo = municipalInfo.shape
    print(f"Shape: {shapeInfo[0]},{shapeInfo[1]}")

    print("Columns:")
    columnInfo = municipalInfo.columns
    for columnName in columnInfo:
        print(columnName)


if __name__ == "__main__":
    main()
