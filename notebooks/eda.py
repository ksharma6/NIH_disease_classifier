import marimo

__generated_with = "0.2.5"
app = marimo.App(width="full")


@app.cell
def __():
    import matplotlib.pyplot as plt
    import pandas as pd

    #pandas settings
    pd.set_option('display.max_rows', 500)
    return pd, plt


@app.cell
def __(pd):
    #read in data
    path = '/home/kishen/documents/projects/python_projects/nih_chest_xrays/data/'
    raw_df = pd.read_csv(path + 'labels.csv')
    return path, raw_df


@app.cell
def __():
    # about the data
    return


@app.cell
def __(raw_df):
    raw_df.head()
    return


@app.cell
def __(raw_df):
    raw_df.info()
    return


@app.cell
def __(raw_df):
    raw_df.nunique()
    return


@app.cell
def __():
    # data cleaning - headers
    import re
        
    def snake_case(string):
        return '_'.join(
        re.sub('([A-Z][a-z]+)', r' \1',
        re.sub('([A-Z]+)', r' \1',
        string.replace('-', ' '))).split()).lower()

    #data cleaning - data types
    return re, snake_case


@app.cell
def __(raw_df):
    ## how best to split labels
    # split on '|'; how many unique labels are there?
    raw_df['Finding Labels'].unique()

    return


@app.cell
def __():
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
