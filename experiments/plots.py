import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_belief_over_time(df):
    os.makedirs("results/figures", exist_ok=True)

    experiment_name = "gaze_wrong_hand_trajectory_correct_small"
    selected = df[df["experiment"] == experiment_name]

    plt.figure()
    plt.plot(selected["stage"], selected["small_prob"], marker="o", label="Small Object")
    plt.plot(selected["stage"], selected["large_prob"], marker="o", label="Large Object")
    plt.xlabel("Cue Stage")
    plt.ylabel("Belief Probability")
    plt.title("Belief Updating Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/figures/belief_over_time.png", dpi=300, bbox_inches="tight")
    plt.show()


def plot_final_accuracy(df):
    final_stage = df[df["stage"] == "trajectory"]
    accuracy = final_stage.groupby("experiment")["correct"].mean()

    plt.figure()
    accuracy.plot(kind="bar")
    plt.ylabel("Final Accuracy")
    plt.xlabel("Experiment Condition")
    plt.title("Final DBN Prediction Accuracy")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("results/figures/accuracy_plot.png", dpi=300, bbox_inches="tight")
    plt.show()


def plot_stage_accuracy(df):
    stage_accuracy = df.groupby("stage")["correct"].mean()
    stage_accuracy = stage_accuracy.reindex(["gaze", "hand", "trajectory"])

    plt.figure()
    stage_accuracy.plot(kind="bar")
    plt.ylabel("Mean Accuracy")
    plt.xlabel("Cue Stage")
    plt.title("Prediction Accuracy Across Temporal Cue Stages")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("results/figures/stage_accuracy.png", dpi=300, bbox_inches="tight")
    plt.show()


def main():
    df = pd.read_csv("experiments/results.csv")

    plot_belief_over_time(df)
    plot_final_accuracy(df)
    plot_stage_accuracy(df)

    print("Plots saved in results/figures/")


if __name__ == "__main__":
    main()