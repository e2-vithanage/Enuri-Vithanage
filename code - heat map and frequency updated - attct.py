import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data setup
data = {'ATTCT Repeat': [
        7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 37, 84, 168, 224, 345, 364, 366, 396, 600, 654
    ],
    "EUROPEAN": [
        0.46, 0.00, 0.15, 1.22, 12.84, 24.31, 35.78, 14.07, 5.20, 2.14,
        1.38, 0.61, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
        0.15, 0.15, 0.15, 0.15, 0.15
    ],
    "AFRICAN": [
        1.25, 0.08, 0.16, 1.01, 3.74, 19.72, 31.64, 26.42, 10.99, 3.66,
        0.78, 0.31, 0.16, 0.08, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        0.00, 0.00, 0.00, 0.00, 0.00
    ],
    "EAST ASIAN": [
        0.00, 0.00, 0.31, 0.10, 0.83, 6.81, 13.93, 36.33, 22.29, 10.32,
        5.26, 2.27, 1.14, 0.21, 0.21, 0.00, 0.00, 0.00, 0.00, 0.00,
        0.00, 0.00, 0.00, 0.00, 0.00
    ],
    "SOUTH ASIAN": [
        0.00, 0.00, 0.21, 0.21, 1.72, 13.20, 26.93, 29.72, 14.70, 6.22,
        3.00, 2.68, 1.29, 0.11, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        0.00, 0.00, 0.00, 0.00, 0.00
    ],
    "ADMIXED AMERICAN": [
        0.00, 0.00, 0.15, 0.10, 2.29, 13.33, 23.44, 33.85, 11.04, 8.85,
        3.54, 1.77, 1.56, 0.21, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        0.00, 0.00, 0.00, 0.00, 0.00
    ]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('ATTCT Repeat', inplace=True)
df_T = df.transpose()

# Create figure
fig, axes = plt.subplots(2, 1, figsize=(16, 12), gridspec_kw={'height_ratios': [3, 1]})

# 🔥 Heatmap (top)
sns.heatmap(
    df_T,
    annot=True,
    cmap='YlOrRd',
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={'label': 'Frequency (%)'},
    ax=axes[0]
)
axes[0].set_xlabel("ATTCT Repeat Length", fontsize=12)
axes[0].set_ylabel("Population", fontsize=12)
axes[0].text(-0.02, 1.02, "(a)", transform=axes[0].transAxes, fontsize=14, fontweight='bold')

# 📊 Centered Bar Plot (bottom)
avg_frequencies = df.mean(axis=1)
x_vals = np.arange(len(avg_frequencies))
bar_labels = avg_frequencies.index.astype(str)

axes[1].bar(x_vals, avg_frequencies.values, color='tomato', alpha=0.8)
axes[1].set_xticks(x_vals)
axes[1].set_xticklabels(bar_labels, rotation=45, ha='right')

axes[1].set_xlabel("ATTCT Repeat Length", fontsize=12)
axes[1].set_ylabel("Mean Frequency (%)", fontsize=12)
axes[1].grid(True, axis='y', linestyle='--', alpha=0.5)
axes[1].text(-0.02, 1.05, "(b)", transform=axes[1].transAxes, fontsize=14, fontweight='bold')

# Center graph padding
axes[1].set_xlim(-0.5, len(x_vals) - 0.5)

# Final layout
plt.tight_layout()
plt.savefig("ATTCT_Heatmap_with_Subfigure_Labels.png", dpi=300, bbox_inches='tight')
plt.show()
