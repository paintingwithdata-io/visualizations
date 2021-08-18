import os
import setup
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from importlib import import_module


def main():
    # Setting all the connection and config variables
    cfg = setup.read_yaml("config.yaml")  # Create a dictionary with all the yaml config info
    dsn = cfg["postgres"]  # Grab the dsn from the config dict

    # Initiating tkinter to later open a file dialog
    root = tk.Tk()
    root.withdraw()

    # Prompt to select which visualization should be generated based on the sql query selected
    # The query name must match the visualization module name exactly in order for this to work
    query = filedialog.askopenfilename(initialdir=cfg["filedir"])  # Selecting the sql query
    viz_name = (os.path.basename(query)).split('.')[0]  # Retrieving the query name only

    # Connecting to the postgres database and selecting the appropriate sql query
    conn = setup.connect(dsn)  # Creating the connection
    # Dynamically import the appropriate viz module
    try:
        viz = import_module("." + viz_name, "viz")
    except ModuleNotFoundError:
        print("A module does not exist with this name, or the query name does not match the module name.")
        exit(1)
    # Reading the sql
    try:
        sql = open(query, "r").read()
    except FileNotFoundError:
        print("An appropriate file was not selected.")
        exit(1)

    # Getting the data and creating the appropriate viz object
    df = pd.read_sql(sql, con=conn)  # Retrieve the data into a dataframe
    fig = viz.create_viz(df)  # Retrieving the figure object by calling the appropriate create_viz method

    # Generating the visualization. By default, this script is configured to use the browser renderer
    fig.show()


if __name__ == '__main__':
    # Execute only when run as the main script
    main()
