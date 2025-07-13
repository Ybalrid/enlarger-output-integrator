import pandas as pd

# Parameters
gamma = 2.2  # Standard for sRGB images

# Load brightness data
csv_path = "brightness_data.csv"
df = pd.read_csv(csv_path)

# User input
framerate = float(input("Enter framerate (frames per second): "))
max_lux = float(input("Enter LUX value corresponding to full brightness (255): "))

# Convert brightness to linear intensity
brightness = df["brightness"]
normalized = brightness / brightness.max()
linear = normalized ** gamma

# Convert to lux
lux_values = linear * max_lux

# Integrate over time (lux·seconds)
delta_t = 1.0 / framerate
lux_seconds = lux_values.sum() * delta_t

# Output result
print(f"\nEstimated total exposure: {lux_seconds:.4f} lux·seconds")
