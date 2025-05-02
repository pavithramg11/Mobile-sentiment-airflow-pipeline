import pandas as pd
import os

def export_csv():
    input_path = '/tmp/data/combined_cleaned_data.csv'
    output_file = 'data/final_sentiment_report.csv'
    local_repo_path = '/usr/local/airflow'  # This is where your Git repo lives in Astronomer
    full_output_path = os.path.join(local_repo_path, output_file)
    
    #  Safety check: Prevents FileNotFoundError
    if not os.path.exists(input_path):
        print(f" File not found: {input_path}")
        return

    df = pd.read_csv(input_path)
    os.makedirs(os.path.dirname(full_output_path), exist_ok=True)
    df.to_csv(full_output_path, index=False)

    print(" CSV updated in repo. Now committing...")
    # Automate Git commit & push
    repo = Repo(local_repo_path)
    repo.git.add(output_file)
    repo.index.commit("Auto-update: sentiment report from Airflow DAG")
    repo.git.push()

    print("CSV pushed to GitHub.")

