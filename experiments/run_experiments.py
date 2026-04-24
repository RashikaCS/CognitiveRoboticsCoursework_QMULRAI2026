import os
import sys
import pandas as pd

sys.path.append(os.path.abspath("."))

from experiments.configs import EXPERIMENTS
from src.simulation import run_single_trial


def main():
    all_rows = []

    for experiment in EXPERIMENTS:
        trial_results = run_single_trial(
            gaze=experiment["gaze"],
            hand=experiment["hand"],
            trajectory=experiment["trajectory"],
            true_target=experiment["true_target"]
        )

        for row in trial_results:
            row["experiment"] = experiment["name"]
            row["description"] = experiment["description"]
            all_rows.append(row)

    df = pd.DataFrame(all_rows)

    os.makedirs("results/logs", exist_ok=True)
    os.makedirs("results/figures", exist_ok=True)

    df.to_csv("experiments/results.csv", index=False)

    with open("results/logs/experiment_log.txt", "w", encoding="utf-8") as file:
        file.write(df.to_string(index=False))

    print("Experiment complete.")
    print(df)
    print("\nSaved:")
    print("- experiments/results.csv")
    print("- results/logs/experiment_log.txt")


if __name__ == "__main__":
    main()