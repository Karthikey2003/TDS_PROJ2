import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
from pathlib import Path
from IPython.display import display
from google.colab import files

# Gotham calls. Set the secret key for the OpenAI Bat-Signal.
openai.api_key = os.environ.get("AIPROXY_TOKEN")

def analyze_csv(data, filename):
    # Scanning Gotham's data landscape for crucial details...
    summary_stats = data.describe(include='all').transpose()
    missing_values = data.isnull().sum()
    correlation_matrix = data.corr(numeric_only=True)

    # Save these findings for the Oracle (GPT-4o-Mini knows all).
    data_preview = data.head().to_string()
    column_types = data.dtypes.to_dict()

    # Summon the Oracle for insights, visualization ideas, and the story of Gotham's dataset.
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
        # Sometimes the Oracle fails. Note it down, Batman style.
        gpt_response = f"The Oracle failed to respond: {e}"

    # Craft the visual tools to battle the darkness of ignorance.
    charts = []
    output_dir = Path(filename).stem
    os.makedirs(output_dir, exist_ok=True)

    # Visualization 1: Expose the lurking shadows of missing values.
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing_values.index, y=missing_values.values)
    plt.xticks(rotation=45, ha='right')
    plt.title("Missing Values per Column")
    plt.ylabel("Count")
    chart_path = os.path.join(output_dir, "missing_values.png")
    plt.savefig(chart_path)
    charts.append(chart_path)
    plt.close()

    # Visualization 2: Use the heatmap lens to decode Gotham's numeric connections.
    if not correlation_matrix.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        chart_path = os.path.join(output_dir, "correlation_heatmap.png")
        plt.savefig(chart_path)
        charts.append(chart_path)
        plt.close()

    # Visualization 3: Spotlight a numeric column's secrets.
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    if not numeric_cols.empty:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[numeric_cols[0]], kde=True, bins=30)
        plt.title(f"Distribution of {numeric_cols[0]}")
        chart_path = os.path.join(output_dir, f"{numeric_cols[0]}_distribution.png")
        plt.savefig(chart_path)
        charts.append(chart_path)
        plt.close()

    # Prepare the Bat-Report.
    with open(os.path.join(output_dir, "README.md"), "w") as readme:
        readme.write("# Dataset Analysis Report\n\n")
        readme.write(f"**Dataset:** {filename}\n\n")
        readme.write("## Summary Statistics\n")
        readme.write(summary_stats.to_markdown())
        readme.write("\n\n## Missing Values\n")
        readme.write(missing_values.to_markdown())
        readme.write("\n\n## Oracle's Wisdom\n")
        readme.write(gpt_response)
        readme.write("\n\n## Visualizations\n")
        for chart in charts:
            readme.write(f"![{chart}]({chart})\n")

if __name__ == "__main__":
    # The call comes in. Time to upload the evidence.
    print("Upload your CSV file. Gotham needs answers.")
    uploaded = files.upload()

    # Pick the first uploaded file, the first clue to the mystery.
    if uploaded:
        filename = next(iter(uploaded.keys()))
        data = pd.read_csv(filename)
        analyze_csv(data, filename)
        print(f"Analysis complete. Check the '{Path(filename).stem}' folder for the Bat-Report.")
    else:
        # No file, no mission. Gotham will wait.
        print("No file uploaded. Mission aborted.")
