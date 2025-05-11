import pandas as pd

# Load your dataset
df = pd.read_csv("/data set.csv")

# Detect missing values
missing_summary = df.isnull().sum()
print("Missing values per column:\n", missing_summary)

# Drop rows with any missing values (if necessary)
df_cleaned = df.dropna()

# OR fill missing values with a strategy (mean, median, etc.)
df_filled = df.fillna(df.mean(numeric_only=True))