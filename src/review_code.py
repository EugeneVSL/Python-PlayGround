import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prepare_smartphone_data(file_path):
    """
    To prepare the smartphone data for visualization, a number of transformations 
    will be applied after reading in the raw DataFrame to memory, including:
        - reducing the number of columns to only those needed for later analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount
    
    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """
    
    if os.path.exists(file_path):
        raw_data = pd.read_csv(file_path, skipinitialspace=True)
        print(raw_data.head())  # TODO: Use this for checking out the dataset, remove before submission
    else:
        raise Exception(f"File containing smartphone data not found at path {file_path}")

    columns = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]
    
    trimmed_data = raw_data.loc[:, columns]
    
    # Remove records without a battery_capacity value
    reduced_data = trimmed_data.dropna(subset=['battery_capacity', 'os'], how='any')
    
    # Divide the price column by 100 to find the dollar amount
    reduced_data["price"] /= 100
    
    return reduced_data


# Call the function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")

def column_to_label(column_name):
    """
    Converts a column name in a pandas DataFrame to a string that can be
    used as a label in a plot.
    
    :param column_name: string containing original column name
    :return: string that is ready to be presented on a plot
    """
    
    # Validate that column_name is a string
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
    
    # If the value provided is not a string, raise an Exception
    else:
        raise Exception("Please makes sure to pass a value of type 'str'.")


def visualize_versus_price(clean_data, x):
    """
    Use seaborn and matplotlib to identify a pattern between avg_rating and 
    battery_capacity.
    
    :param clean_data: a pandas DataFrame containing cleaned smartphone data
    :param x: variable to be plotted on the x-axis
    :return: None
    """
    
    # Create the scatterplot
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    
    x_label = column_to_label(x)
    
    # Add x and y labels
    plt.xlabel(x_label)
    plt.ylabel("Price ($)")
    
    # Add a title to the plot
    plt.title(f"{x_label} vs. Price")
    
    
# Call the visualize_versus_price function
visualize_versus_price(cleaned_data, "processor_speed")