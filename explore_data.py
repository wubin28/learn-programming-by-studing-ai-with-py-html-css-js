import pandas as pd

# Read the Excel file - row 1 (index 1) contains headers, row 0 is title
file_path = 'first-80-rows-agentic_ai_performance_dataset_20250622.xlsx'
df = pd.read_excel(file_path, header=1)

print("=" * 80)
print("DATASET EXPLORATION")
print("=" * 80)

print("\n1. BASIC INFO:")
print(f"   Total rows: {len(df)}")
print(f"   Total columns: {len(df.columns)}")

print("\n2. COLUMN NAMES:")
for i, col in enumerate(df.columns, 1):
    print(f"   {i}. {col}")

print("\n3. DATA TYPES:")
print(df.dtypes)

print("\n4. FIRST 5 ROWS:")
print(df.head())

print("\n5. KEY COLUMNS FOR BUSINESS QUESTIONS:")
required_cols = ['agent_type', 'multimodal_capability', 'model_architecture',
                 'task_category', 'bias_detection']

for col in required_cols:
    if col in df.columns:
        print(f"\n   {col}:")
        print(f"   - Unique values: {df[col].nunique()}")
        print(f"   - Value counts:")
        print(df[col].value_counts())
    else:
        print(f"\n   ⚠️ WARNING: Column '{col}' NOT FOUND in dataset!")

print("\n6. MISSING VALUES:")
print(df.isnull().sum())

print("\n" + "=" * 80)
print("EXPLORATION COMPLETE")
print("=" * 80)
