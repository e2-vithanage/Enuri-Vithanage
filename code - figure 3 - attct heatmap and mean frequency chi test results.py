import pandas as pd
from scipy.stats import chi2_contingency

# Allele counts for ATXN10 gene by population
allele_counts = {
    7: [0, 16, 0, 0, 3],
    8: [0, 1, 0, 0, 0],
    9: [0, 2, 3, 2, 1],
    10: [1, 13, 1, 2, 2],
    11: [22, 48, 8, 16, 8],
    12: [128, 253, 66, 123, 84],
    13: [225, 406, 135, 251, 159],
    14: [325, 339, 352, 277, 234],
    15: [106, 141, 216, 137, 92],
    16: [85, 47, 100, 58, 34],
    17: [34, 10, 51, 28, 14],
    18: [17, 4, 22, 25, 9],
    19: [15, 2, 11, 12, 4],
    20: [2, 1, 2, 1, 1],
    21: [0, 0, 2, 0, 1],
    37: [0, 0, 0, 0, 1],
    84: [0, 0, 0, 0, 1],
    168: [0, 0, 0, 0, 1],
    224: [0, 0, 0, 0, 1],
    345: [0, 0, 0, 0, 1],
    364: [0, 0, 0, 0, 1],
    366: [0, 0, 0, 0, 1],
    396: [0, 0, 0, 0, 1],
    600: [0, 0, 0, 0, 1],
    654: [0, 0, 0, 0, 1],
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
