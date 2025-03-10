import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import re

matplotlib.use("Agg")  # Ensures Matplotlib does NOT try to open a GUI window

# Set correct data path
csv_directory = "/home/tina/ee250/labs/lab5/data"

# Get all CSV files
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

# Dictionary to store files by their common number
file_groups = {}

# Regex to match iperf_tcp_15m.csv and iperf_udp_15m.csv
pattern = re.compile(r'iperf_(tcp|udp)_(\d+)m\.csv')

# Organize files into groups based on their number
for file in csv_files:
    match = pattern.match(file)
    if match:
        protocol, num = match.groups()
        if num not in file_groups:
            file_groups[num] = {}
        file_groups[num][protocol] = os.path.join(csv_directory, file)

print("Grouped files:", file_groups)

# Process and plot data
for num, files in file_groups.items():
    print(f"\n🔹 Processing files for {num}m: {files}")

    try:
        plt.figure(figsize=(8, 6))  # Ensure each figure is separate

        for protocol, file_path in files.items():
            print(f"Reading {protocol.upper()} data from {file_path}")

            # Read the CSV safely
            try:
                df = pd.read_csv(file_path)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            print(f"✔ CSV shape: {df.shape}")
            print(f"Columns in {file_path}: {df.columns}")
            print(df.head())  # Preview data

            # Ensure "Distance" exists, but we will NOT use it for X-axis
            if "Distance" not in df.columns:
                print(f"⚠ Skipping {protocol.upper()} {num}m (missing Distance column)")
                continue

            # Extract test run columns (Run1, Run2, ...)
            run_columns = [col for col in df.columns if "Run" in col]

            if not run_columns:
                print(f"⚠ No test run columns found in {file_path}, skipping.")
                continue

            # Convert to numeric
            df[run_columns] = df[run_columns].apply(pd.to_numeric, errors='coerce')
            # X-axis labels should be "Run1", "Run2", ...
            x_axis_labels = run_columns
            y_values = df.iloc[0][run_columns]  # Extract first row for runs

            # Plot TCP throughput (solid line)
            if protocol == "tcp":
                plt.plot(x_axis_labels, y_values, marker='o', linestyle='-', label="TCP Throughput (Mbps)", color="orange")

            # Plot UDP throughput (dashed line)
            elif protocol == "udp":
                plt.plot(x_axis_labels, y_values, marker='s', linestyle='dashed', label="UDP Throughput (Mbps)", color="orangered")

        # Formatting
        plt.xlabel("Test Runs", fontsize=12)
        plt.ylabel("Throughput (Mbps)", fontsize=12)
        plt.xticks(rotation=45)

        # Set title with bold styling
        plt.title(f"TCP & UDP Throughput at {num}m Distance", fontsize=14, fontweight="bold")

        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save plot (DO NOT SHOW to prevent crashes)
        plot_filename = os.path.join(csv_directory, f"iperf_combined_{num}.png")
        plt.savefig(plot_filename)
        print(f"Saved plot: {plot_filename}")

        plt.close()  # **Prevents excessive memory usage & segmentation faults**

    except Exception as e:
        print(f"Unexpected error processing {num}m: {e}")

print("\nAll plots created and saved successfully!")