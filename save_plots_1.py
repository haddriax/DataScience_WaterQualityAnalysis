import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.io as pio
from pandas import DataFrame

# Create the "plots" directory if it does not exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Load the data
data = pd.read_csv("water_potability.csv")

# Drop missing values
data = data.dropna()

# Matplotlib and Seaborn plots
# Plot 1: Distribution of Unsafe and Safe Water
plt.figure(figsize=(15, 10))
sns.histplot(data["Potability"], bins=30, kde=False)
plt.title("Distribution of Unsafe and Safe Water")
plt.xlabel("Potability")
plt.ylabel("Frequency")
plt.xticks(ticks=[0, 1], labels=["Unsafe", "Safe"])
plt.savefig("plots/distribution_of_unsafe_and_safe_water.png")
plt.clf()

# Plot 2: Distribution of Potability
plt.figure(figsize=(15, 10))
sns.histplot(data["Potability"], bins=2, kde=False)
plt.title("Distribution of Potability")
plt.xlabel("Potability")
plt.ylabel("Frequency")
plt.xticks(ticks=[0, 1], labels=["Unsafe", "Safe"])
plt.savefig("plots/distribution_of_potability.png")
plt.clf()


def save_plotly_histogram(_data: DataFrame, column: str, title: str, filename: str):
    """
    Save Plotly Histogram

    :param _data: The input data as a DataFrame.
    :param column: The name of the column in the DataFrame used for the histogram.
    :param title: The title of the histogram.
    :param filename: The filename to save the histogram as.
    :return: None

    """
    try:
        figure = px.histogram(_data, x=column, color="Potability", title=title)
        # pio.write_image(figure, f"plots/{filename}", format="png", engine="kaleido")
        pio.write_image(figure, f"plots/{filename}", format="png", engine="orca")

        print(f"Plotly histogram '{filename}' saved successfully.")
    except Exception as e:
        print(f"Error saving Plotly histogram '{filename}': {str(e)}")


# Plot 3: Factors Affecting Water Quality: PH
save_plotly_histogram(data, "ph", "Factors Affecting Water Quality: PH", "ph.png")

# Plot 4: Factors Affecting Water Quality: Hardness
save_plotly_histogram(
    data, "Hardness", "Factors Affecting Water Quality: Hardness", "hardness.png"
)

# Plot 5: Factors Affecting Water Quality: Solids
save_plotly_histogram(
    data, "Solids", "Factors Affecting Water Quality: Solids", "solids.png"
)

# Plot 6: Factors Affecting Water Quality: Chloramines
save_plotly_histogram(
    data,
    "Chloramines",
    "Factors Affecting Water Quality: Chloramines",
    "chloramines.png",
)

# Plot 7: Factors Affecting Water Quality: Sulfate
save_plotly_histogram(
    data, "Sulfate", "Factors Affecting Water Quality: Sulfate", "sulfate.png"
)

# Plot 8: Factors Affecting Water Quality: Conductivity
save_plotly_histogram(
    data,
    "Conductivity",
    "Factors Affecting Water Quality: Conductivity",
    "conductivity.png",
)

# Plot 9: Factors Affecting Water Quality: Organic Carbon
save_plotly_histogram(
    data,
    "Organic_carbon",
    "Factors Affecting Water Quality: Organic Carbon",
    "organic_carbon.png",
)

# Plot 10: Factors Affecting Water Quality: Trihalomethanes
save_plotly_histogram(
    data,
    "Trihalomethanes",
    "Factors Affecting Water Quality: Trihalomethanes",
    "trihalomethanes.png",
)

# Plot 11: Factors Affecting Water Quality: Turbidity
save_plotly_histogram(
    data, "Turbidity", "Factors Affecting Water Quality: Turbidity", "turbidity.png"
)

print("All plots saved successfully.")
