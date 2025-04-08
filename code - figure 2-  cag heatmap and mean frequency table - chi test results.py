import pandas as pd
from scipy.stats import chi2_contingency

# Data extracted from the documents
# Dictionary format: repeat_length: [european, african, east_asian, south_asian, admixed_american]
allele_counts = {
    9:  [7, 1, 2, 1, 5],
    10: [8, 1, 1, 3, 5],
    11: [0, 6, 0, 0, 1],
    12: [7,10,3,1,1],
    13: [0, 8,2,6,6],
    14: [2,19,4,36,3],
    15: [91,348,28,33,111],
    16: [27,155,43,37,32],
    17: [371,185,550,511,231],
    18: [148,139,222,131,93],
    19: [85,188,65,47,51],
    20: [61,68,26,47,30],
    21: [40,46,12,25,19],
    22: [37,24,7,25,17],
    23: [27,23,4,18,23],
    24: [26,16,5,15,10],
    25: [15,20,4,6,14],
    26: [8, 3,3,6,7],
    27: [13,12,0,2,5],
    28: [3, 8,2,3,6],
    29: [5, 1,0,0,4],
    30: [2, 1,3,4,3],
    31: [1, 2,1,1,2],
    32: [3, 2,0,1,0],
    33: [0, 1,1,0,0],
    34: [2, 0,0,1,0],
    35: [0, 0,0,1,1],
    36: [1, 0,0,0,0],
    39: [0, 1,0,0,0],
    42: [0, 1,0,0,0],
    43: [0, 0,0,0,2],
}

# Create DataFrame
df = pd.DataFrame.from_dict(allele_counts, orient='index',
                            columns=['European', 'African', 'East Asian', 'South Asian', 'Admixed American'])
df.fillna(0, inplace=True)

# Run Chi-squared test
chi2, p, dof, expected = chi2_contingency(df)

# Output results
print("Chi-squared Test Results:")
print(f"Chi2 Statistic = {chi2:.4f}")
print(f"Degrees of Freedom = {dof}")
print(f"P-value = {p:.4e}")

if p < 0.05:
    print("Result: Significant differences exist between the populations (p < 0.05).")
else:
    print("Result: No significant differences found between the populations (p >= 0.05).")
