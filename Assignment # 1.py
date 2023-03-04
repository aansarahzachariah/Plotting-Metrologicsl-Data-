


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



def plot_annual_sunshine(df):
    """
    Plots the annual sunshine for each season from 1919 to 2022.

    Args:
    df (pandas.DataFrame): A pandas DataFrame containing precipitation data.

    Returns:
    None
    """
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10,5))

    plt.plot(df["year"], df["ann"], label="Annual sunshine")
    plt.plot(df["year"], df["win"], label="Winter sunshine")
    plt.plot(df["year"], df["spr"], label="Spring sunshine")
    plt.plot(df["year"], df["sum"], label="Summer sunshine")
    plt.plot(df["year"], df["aut"], label="Autumn sunshine")

    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("sunshine (hrs)")
    plt.title("Annual sunshine from 1919 to 2022")

    plt.show()





# # Scatter plot
# 
# Another alternative visualization method is a scatter plot with trend lines, where each point represents a year and the x-coordinate is the total precipitation while the y-coordinate is the precipitation in a particular season. This visualization method can help us to examine the relationship between the total precipitation and the precipitation in each season. We can use the following code to produce the scatter plot:




def plot_annual_seasonal_relationship(df, seasons):
    """
    Plots the relationship between annual and seasonal sunshine from 1919 to 2022 using scatter and dashed line plots.

    Parameters:
    df (pandas.DataFrame): A pandas DataFrame containing the annual and seasonal sunshine data.

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
    plt.xlabel("Annual sunshine (hrs)")
    plt.ylabel("Seasonal sunshine (hrs)")
    plt.title("Relationship between Annual and Seasonal sunshine from 1919 to 2022")

    plt.show()
    
    
# # Mean rainfall of each month


def plot_monthly_avg_sunshine(df):
    """
    Extracts the monthly columns of rainfall data from a given DataFrame and computes the average sunshine for each month.
    Plots the average sunshine for each month using a bar chart.
    
    Args:
    - df: A pandas DataFrame containing rainfall data.
    
    Returns:
    - None
    """
    monthly = df.iloc[:, 1:13] # Extract monthly columns
    monthly_avg = monthly.mean() # Compute average rainfall for each month
    
    plt.figure(figsize=(8, 5))
    plt.bar(monthly_avg.index, monthly_avg.values)
    plt.xlabel("Month")
    plt.ylabel("Average sunshine (mm)")
    plt.title("Average Monthly sunshine from 1919 to 2022")
    plt.show()


# # Main Body

df = read_excel_file("sunshine.xlsx")
print(df.head())

seasons = ["win", "spr", "sum", "aut"]


plot_annual_sunshine(df)


plot_annual_seasonal_relationship(df, seasons)

plot_monthly_avg_sunshine(df)


