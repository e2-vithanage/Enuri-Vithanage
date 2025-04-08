import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# CAG Repeat Data
data = {
    "CAG Repeat": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39, 42, 43],
    "European": [0.71, 0.81, 0.00, 0.71, 0.00, 0.20, 9.19, 2.73, 37.47, 14.95, 8.59,
                 6.16, 4.04, 3.74, 2.73, 2.63, 1.52, 0.81, 1.31, 0.30, 0.51, 0.20,
                 0.10, 0.30, 0.00, 0.20, 0.00, 0.10, 0.00, 0.00, 0.00],
    "African": [0.08, 0.08, 0.47, 0.78, 0.62, 1.47, 27.00, 12.02, 14.35, 10.78,
                14.58, 5.28, 3.57, 1.86, 1.78, 1.24, 1.55, 0.23, 0.93, 0.62,
                0.08, 0.08, 0.16, 0.16, 0.08, 0.00, 0.00, 0.00, 0.08, 0.08, 0.00],
    "East Asian": [0.20, 0.10, 0.00, 0.30, 0.20, 0.40, 2.83, 4.35, 55.67, 22.47,
                   6.58, 2.63, 1.21, 0.71, 0.40, 0.51, 0.40, 0.30, 0.00, 0.20,
                   0.00, 0.30, 0.10, 0.00, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
    "South Asian": [0.10, 0.31, 0.00, 0.10, 0.62, 3.75, 3.43, 3.85, 53.17, 13.63,
                    4.89, 4.89, 2.60, 2.60, 1.87, 1.56, 0.62, 0.62, 0.21, 0.31,
                    0.00, 0.42, 0.10, 0.10, 0.00, 0.10, 0.10, 0.00, 0.00, 0.00, 0.00],
    "Admixed American": [0.73, 0.73, 0.15, 0.15, 0.88, 0.44, 16.28, 4.69, 33.87,
                         13.64, 7.48, 4.40, 2.79, 2.49, 3.37, 1.47, 2.05, 1.03,
                         0.73, 0.88, 0.59, 0.44, 0.29, 0.00, 0.00, 0.00, 0.15,
                         0.00, 0.00, 0.00, 0.29]
}

# DataFrame setup
df = pd.DataFrame(data)
df.set_index('CAG Repeat', inplace=True)

# Capitalize population names and transpose
df.columns = [col.upper() for col in df.columns]
df_T = df.transpose()

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(18, 12), gridspec_kw={'height_ratios': [3, 1]})

# (a) Heatmap
sns.heatmap(
    df_T,
    annot=True,
    cmap='YlOrRd',
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={'label': 'FREQUENCY (%)'},
    ax=axes[0]
)
axes[0].set_xlabel("CAG Repeat Length", fontsize=12)
axes[0].set_ylabel("Population", fontsize=12)
axes[0].set_yticklabels(axes[0].get_yticklabels(), rotation=0)
axes[0].text(-0.02, 1.02, "(a)", transform=axes[0].transAxes, fontsize=14, fontweight='bold')

# (b) Bar plot
avg_frequencies = df.mean(axis=1)
x_vals = np.arange(len(avg_frequencies))
bar_labels = avg_frequencies.index.astype(str)

axes[1].bar(x_vals, avg_frequencies.values, color='tomato', alpha=0.8)
axes[1].set_xticks(x_vals)
axes[1].set_xticklabels(bar_labels, rotation=45, ha='right')
axes[1].set_xlabel("CAG Repeat Length", fontsize=12)
axes[1].set_ylabel("Mean Frequency (%)", fontsize=12)
axes[1].grid(True, axis='y', linestyle='--', alpha=0.5)
axes[1].text(-0.02, 1.05, "(b)", transform=axes[1].transAxes, fontsize=14, fontweight='bold')

axes[1].set_xlim(-0.5, len(x_vals) - 0.5)

# Final layout
plt.tight_layout()
plt.savefig("CAG_REPEAT_HEATMAP_MEANFREQ.png", dpi=301, bbox_inches='tight')
plt.show()
