import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
from pathlib import Path
from IPython.display import display
from google.colab import files

# Set OpenAI API key from environment variable
openai.api_key = os.environ.get("AIPROXY_TOKEN")

def analyze_csv(data, filename):
    # Summary statistics
    summary_stats = data.describe(include='all').transpose()
    missing_values = data.isnull().sum()
    correlation_matrix = data.corr(numeric_only=True)
    
    # Save summaries to strings for GPT-4o-Mini
    data_preview = data.head().to_string()
    column_types = data.dtypes.to_dict()

    # Generate story and suggestions using GPT
    prompt = f"""
You are analyzing a dataset. Here are the details:

1. Column types: {column_types}
2. Missing values: {missing_values.to_dict()}
3. Sample data:
{data_preview}

Provide:
1. Key insights from the dataset.
2. Suggestions for meaningful visualizations.
3. A brief story summarizing these insights.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        gpt_response = response['choices'][0]['message']['content']
    except Exception as e:
        gpt_response = f"Failed to get GPT response: {e}"

    # Create charts based on analysis
    charts = []
    output_dir = Path(filename).stem
    os.makedirs(output_dir, exist_ok=True)

    # Chart 1: Missing values barplot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing_values.index, y=missing_values.values)
    plt.xticks(rotation=45, ha='right')
    plt.title("Missing Values per Column")
    plt.ylabel("Count")
    chart_path = os.path.join(output_dir, "missing_values.png")
    plt.savefig(chart_path)
    charts.append(chart_path)
    plt.close()

    # Chart 2: Correlation heatmap (if numeric data exists)
    if not correlation_matrix.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        chart_path = os.path.join(output_dir, "correlation_heatmap.png")
        plt.savefig(chart_path)
        charts.append(chart_path)
        plt.close()

    # Chart 3: Distribution of a sample numeric column (if available)
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    if not numeric_cols.empty:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[numeric_cols[0]], kde=True, bins=30)
        plt.title(f"Distribution of {numeric_cols[0]}")
        chart_path = os.path.join(output_dir, f"{numeric_cols[0]}_distribution.png")
        plt.savefig(chart_path)
        charts.append(chart_path)
        plt.close()

    # Write README.md
    with open(os.path.join(output_dir, "README.md"), "w") as readme:
        readme.write("# Dataset Analysis Report\n\n")
        readme.write(f"**Dataset:** {filename}\n\n")
        readme.write("## Summary Statistics\n")
        readme.write(summary_stats.to_markdown())
        readme.write("\n\n## Missing Values\n")
        readme.write(missing_values.to_markdown())
        readme.write("\n\n## GPT-4o-Mini Analysis\n")
        readme.write(gpt_response)
        readme.write("\n\n## Visualizations\n")
        for chart in charts:
            readme.write(f"![{chart}]({chart})\n")

if __name__ == "__main__":
    # Upload CSV file
    print("Please upload your CSV file:")
    uploaded = files.upload()

    # Get the first uploaded file
    if uploaded:
        filename = next(iter(uploaded.keys()))
        data = pd.read_csv(filename)
        analyze_csv(data, filename)
        print(f"Analysis completed. Check the '{Path(filename).stem}' folder for results.")
    else:
        print("No file uploaded. Exiting.")
