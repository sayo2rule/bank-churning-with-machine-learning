# Import the necessary modules
import matplotlib.pyplot as plt


# Define a function to look through a column and its return unique values in the column and desplay relates statistics
def col_checker(df, col_names):
    for col_name in col_names:
        col_uniq = df[col_name].value_counts().sort_index()

        # Plot a bar chart to visualize unique values
        plt.figure(figsize=(6, 4))
        plt.bar(col_uniq.index, col_uniq.values)
        plt.title("Unique Values in Column: " + col_name)
        plt.xlabel("Unique Values")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

        # Print the count of unique values
        print("Count unique in", col_name + ":", len(col_uniq))
