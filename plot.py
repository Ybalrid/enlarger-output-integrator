import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
output_csv = "brightness_data.csv"

# Read CSV file from disk
df = pd.read_csv(output_csv)

# Plot brightness vs frame
plt.plot(df["frame"], df["brightness"])
plt.xlabel("Frame")
plt.ylabel("Brightness")
plt.title("Lamp Brightness Over Time")
plt.grid(True)
plt.show()