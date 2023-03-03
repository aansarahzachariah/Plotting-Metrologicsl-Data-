
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # Read the file




def read_excel_file(file_path):
    """
    Reads an excel file from the specified file path and returns a pandas DataFrame.
    
    Args:
    file_path (str): Path to the excel file
    
    Returns:
    pandas.DataFrame: DataFrame containing the data from the excel file
    """

    df = pd.read_excel(file_path)
    
    return df


# 
# # Line Plot




def plot_annual_precipitation(df):
    """
    Plots the annual precipitation for each season from 1919 to 2022.

    Args:
    df (pandas.DataFrame): A pandas DataFrame containing precipitation data.

    Returns:
    None
    """
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10,5))

    plt.plot(df["year"], df["ann"], label="Annual Precipitation")
    plt.plot(df["year"], df["win"], label="Winter Precipitation")
    plt.plot(df["year"], df["spr"], label="Spring Precipitation")
    plt.plot(df["year"], df["sum"], label="Summer Precipitation")
    plt.plot(df["year"], df["aut"], label="Autumn Precipitation")

    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Precipitation (mm)")
    plt.title("Annual Precipitation from 1919 to 2022")

    plt.show()


# # Stacked bar charts
# 
# One alternative visualization method is a stacked bar chart, where each bar represents a year and is divided into segments representing the contribution of each season to the total precipitation. This visualization method can help us to compare the relative contribution of each season to the total precipitation and how it changes over time. We can use the following code to produce the stacked bar chart:




def plot_seasonal_precipitation(df, seasons):
    '''
    Plots the seasonal precipitation of a given DataFrame containing the following columns:
    - year: the year of the data
    - win: winter precipitation
    - spr: spring precipitation
    - sum: summer precipitation
    - aut: autumn precipitation
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing the seasonal precipitation data
    
    Returns:
    None
    '''
    plt.figure(figsize=(10,5))

    
    colors = ["tab:blue", "tab:green", "tab:orange", "tab:red"]

    plt.bar(df["year"], df[seasons[0]], label=seasons[0], color=colors[0])
    for i in range(1, len(seasons)):
        plt.bar(df["year"], df[seasons[i]], label=seasons[i], color=colors[i], bottom=df[seasons[:i]].sum(axis=1))

    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Precipitation (mm)")
    plt.title("Seasonal Precipitation from 1919 to 2022")

    plt.show()


# # Scatter plot
# 
# Another alternative visualization method is a scatter plot with trend lines, where each point represents a year and the x-coordinate is the total precipitation while the y-coordinate is the precipitation in a particular season. This visualization method can help us to examine the relationship between the total precipitation and the precipitation in each season. We can use the following code to produce the scatter plot:




def plot_annual_seasonal_relationship(df, seasons):
    """
    Plots the relationship between annual and seasonal precipitation from 1919 to 2022 using scatter and dashed line plots.

    Parameters:
    df (pandas.DataFrame): A pandas DataFrame containing the annual and seasonal precipitation data.

    Returns:
    None
    """
    plt.figure(figsize=(10,5))

    colors = ["tab:blue", "tab:green", "tab:orange", "tab:red"]

    for i in range(len(seasons)):
        plt.scatter(df["ann"], df[seasons[i]], label=seasons[i], color=colors[i])

    for i in range(len(seasons)):
        z = np.polyfit(df["ann"], df[seasons[i]], 1)
        p = np.poly1d(z)
        plt.plot(df["ann"], p(df["ann"]), linestyle="dashed", color=colors[i])

    plt.legend()
    plt.xlabel("Annual Precipitation (mm)")
    plt.ylabel("Seasonal Precipitation (mm)")
    plt.title("Relationship between Annual and Seasonal Precipitation from 1919 to 2022")

    plt.show()
    
# # Main Body


df = read_excel_file("sunshine.xlsx")
print(df.head())

seasons = ["win", "spr", "sum", "aut"]


plot_annual_precipitation(df)

plot_seasonal_precipitation(df, seasons)

plot_annual_seasonal_relationship(df, seasons)

