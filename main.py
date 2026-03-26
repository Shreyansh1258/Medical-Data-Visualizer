# main.py
from medical_data_visualiser import load_and_process_data, cat_plot, heat_map

# Load and process the data
df = load_and_process_data("medical_examination.csv")

# Generate and save plots
cat_plot(df)
heat_map(df)

print("Plots generated: catplot.png and heatmap.png")