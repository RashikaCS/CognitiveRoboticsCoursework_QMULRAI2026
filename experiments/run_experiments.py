import os
import sys
import pandas as pd

# Ensure project root is in Python path so src/ and experiments/ can be imported
sys.path.append(os.path.abspath("."))

from experiments.configs import EXPERIMENTS
from src.simulation import run_single_trial


def main():
    """
    Run all experiment conditions and save results.

    Each condition is repeated multiple times because the DBN includes
    sensory noise. Repeating trials provides more stable and reliable
    estimates of model performance.
    """

    all_rows = []

    # Number of repeated trials for each experimental condition
    n_trials = 100

    for experiment in EXPERIMENTS:
        for trial_id in range(n_trials):

            # Run one trial for the current cue configuration
            trial_results = run_single_trial(
                gaze=experiment["gaze"],
                hand=experiment["hand"],
                trajectory=experiment["trajectory"],
                true_target=experiment["true_target"]
            )

            # Add experiment metadata to each stage result (gaze, hand, trajectory)
            for row in trial_results:
                row["trial_id"] = trial_id
                row["experiment"] = experiment["name"]
                row["description"] = experiment["description"]
                all_rows.append(row)

    # Convert collected results into a DataFrame
    df = pd.DataFrame(all_rows)

    # Create output directories if they do not exist
    os.makedirs("results/logs", exist_ok=True)
    os.makedirs("results/figures", exist_ok=True)

    # Save structured results
    results_path = "results/results.csv"
    df.to_csv(results_path, index=False)

    # Save readable log file
    log_path = "results/logs/experiment_log.txt"
    with open(log_path, "w", encoding="utf-8") as file:
        file.write(df.to_string(index=False))

    # Print summary
    print("Experiment complete.")
    print(df.head(20))
    print(f"\nTotal rows: {len(df)}")
    print(f"Trials per experiment: {n_trials}")

    print("\nSaved:")
    print(f"- {results_path}")
    print(f"- {log_path}")


if __name__ == "__main__":
    main()