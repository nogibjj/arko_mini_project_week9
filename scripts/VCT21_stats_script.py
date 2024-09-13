import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt


def get_summary_stats(df):

    summary_stats = df.describe()

    return summary_stats


def plot_pie_chart(df, label_column, value_column, title="Pie Chart"):
    """
    Plots a pie chart using columns from a DataFrame.

    Parameters:
    - df: pandas DataFrame containing the data
    - label_column: column name in the DataFrame to use for labels
    - value_column: column name in the DataFrame to use for values
    - title: title of the pie chart (optional)
    """
    labels = df[label_column].tolist()
    values = df[value_column].tolist()

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title(title)

    return fig, ax


if __name__ == "__main__":

    current_dir = Path(os.getcwd())
    data_folder = current_dir / "data"
    data_file = data_folder / "banned_maps_stats.csv"

    input_df = pd.read_csv(data_file)
    print(input_df.head(5))
    print(get_summary_stats(input_df))
    fig, ax = plot_pie_chart(
        input_df, "Map", "Total", title="Ratio of maps banned (Valorant VCT'21)"
    )
    ax.set_facecolor("lightgrey")

    fig.savefig("pie_chart.png")

    plt.show()
