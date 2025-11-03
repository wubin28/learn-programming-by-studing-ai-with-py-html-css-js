import pandas as pd

# Read the Excel file
file_path = 'first-80-rows-agentic_ai_performance_dataset_20250622.xlsx'
df = pd.read_excel(file_path, header=1)

print("=" * 80)
print("BUSINESS QUESTIONS ANALYSIS")
print("=" * 80)
print(f"Total records analyzed: {len(df)}\n")

# ============================================================================
# QUESTION 1: Top 3 agent_types with highest multimodal capability percentage
# ============================================================================
print("-" * 80)
print("QUESTION 1: Top 3 Agent Types with Highest Multimodal Capability %")
print("-" * 80)

# Group by agent_type and calculate multimodal percentage within each type
agent_type_stats = df.groupby('agent_type').agg({
    'multimodal_capability': ['sum', 'count']
}).reset_index()

# Flatten column names
agent_type_stats.columns = ['agent_type', 'multimodal_count', 'total_count']

# Calculate percentage within each agent_type
agent_type_stats['multimodal_percentage'] = (
    agent_type_stats['multimodal_count'] / agent_type_stats['total_count'] * 100
)

# Sort by percentage descending and get top 3
top3_agent_types = agent_type_stats.sort_values(
    'multimodal_percentage', ascending=False
).head(3)

print("\nTop 3 Agent Types (by multimodal % within each type):")
for idx, row in enumerate(top3_agent_types.itertuples(), 1):
    print(f"  {idx}. {row.agent_type}")
    print(f"     - Multimodal agents: {int(row.multimodal_count)} out of {int(row.total_count)}")
    print(f"     - Percentage: {row.multimodal_percentage:.2f}%")

# Show all agent types for reference
print("\nAll Agent Types (sorted by multimodal %):")
for row in agent_type_stats.sort_values('multimodal_percentage', ascending=False).itertuples():
    print(f"  {row.agent_type:25} | {int(row.multimodal_count):2}/{int(row.total_count):2} | {row.multimodal_percentage:6.2f}%")

# ============================================================================
# QUESTION 2: Top 3 model_architectures with highest multimodal capability %
# ============================================================================
print("\n" + "-" * 80)
print("QUESTION 2: Top 3 Model Architectures with Highest Multimodal Capability %")
print("-" * 80)

# Group by model_architecture and calculate multimodal percentage within each architecture
model_arch_stats = df.groupby('model_architecture').agg({
    'multimodal_capability': ['sum', 'count']
}).reset_index()

# Flatten column names
model_arch_stats.columns = ['model_architecture', 'multimodal_count', 'total_count']

# Calculate percentage within each model_architecture
model_arch_stats['multimodal_percentage'] = (
    model_arch_stats['multimodal_count'] / model_arch_stats['total_count'] * 100
)

# Sort by percentage descending and get top 3
top3_model_archs = model_arch_stats.sort_values(
    'multimodal_percentage', ascending=False
).head(3)

print("\nTop 3 Model Architectures (by multimodal % within each architecture):")
for idx, row in enumerate(top3_model_archs.itertuples(), 1):
    print(f"  {idx}. {row.model_architecture}")
    print(f"     - Multimodal agents: {int(row.multimodal_count)} out of {int(row.total_count)}")
    print(f"     - Percentage: {row.multimodal_percentage:.2f}%")

# Show all architectures for reference
print("\nAll Model Architectures (sorted by multimodal %):")
for row in model_arch_stats.sort_values('multimodal_percentage', ascending=False).itertuples():
    print(f"  {row.model_architecture:20} | {int(row.multimodal_count):2}/{int(row.total_count):2} | {row.multimodal_percentage:6.2f}%")

# ============================================================================
# QUESTION 3: Top 3 task_categories with highest median bias_detection_score
# ============================================================================
print("\n" + "-" * 80)
print("QUESTION 3: Top 3 Task Categories with Highest Median Bias Detection Score")
print("-" * 80)

# Group by task_category and calculate median bias_detection_score
task_bias_stats = df.groupby('task_category').agg({
    'bias_detection_score': ['median', 'mean', 'count']
}).reset_index()

# Flatten column names
task_bias_stats.columns = ['task_category', 'median_bias_score', 'mean_bias_score', 'count']

# Sort by median descending and get top 3
top3_task_categories = task_bias_stats.sort_values(
    'median_bias_score', ascending=False
).head(3)

print("\nTop 3 Task Categories (by median bias detection score - higher is better):")
for idx, row in enumerate(top3_task_categories.itertuples(), 1):
    print(f"  {idx}. {row.task_category}")
    print(f"     - Median bias score: {row.median_bias_score:.3f}")
    print(f"     - Mean bias score: {row.mean_bias_score:.3f}")
    print(f"     - Number of agents: {int(row.count)}")

# Show all task categories for reference
print("\nAll Task Categories (sorted by median bias score):")
for row in task_bias_stats.sort_values('median_bias_score', ascending=False).itertuples():
    print(f"  {row.task_category:30} | Median: {row.median_bias_score:6.3f} | Mean: {row.mean_bias_score:6.3f} | N={int(row.count):2}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

# Export data for HTML dashboard
print("\n" + "=" * 80)
print("EXPORTING DATA FOR HTML DASHBOARD")
print("=" * 80)

# Prepare data for export
export_data = {
    'dataset_info': {
        'total_records': len(df),
        'total_columns': len(df.columns)
    },
    'question1': {
        'all_data': agent_type_stats.sort_values('multimodal_percentage', ascending=False).to_dict('records'),
        'top3': top3_agent_types.to_dict('records')
    },
    'question2': {
        'all_data': model_arch_stats.sort_values('multimodal_percentage', ascending=False).to_dict('records'),
        'top3': top3_model_archs.to_dict('records')
    },
    'question3': {
        'all_data': task_bias_stats.sort_values('median_bias_score', ascending=False).to_dict('records'),
        'top3': top3_task_categories.to_dict('records')
    }
}

# Save to JSON for HTML dashboard
import json
with open('dashboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(export_data, f, indent=2, ensure_ascii=False)

print("✓ Data exported to 'dashboard_data.json'")
print("\nThis JSON file will be embedded in the HTML dashboard.")
