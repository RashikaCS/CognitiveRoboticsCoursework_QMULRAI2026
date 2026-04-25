from src.dbn_model import DynamicBayesianNetwork


def run_single_trial(gaze, hand, trajectory, true_target):
    """
    Run one action-prediction trial using the DBN.

    Cue order:
    1. gaze
    2. hand
    3. trajectory
    """

    dbn = DynamicBayesianNetwork()

    cue_sequence = [
        ("gaze", gaze),
        ("hand", hand),
        ("trajectory", trajectory)
    ]

    results = []

    for stage, observation in cue_sequence:
        # Update belief and get noisy observation
        belief, noisy_observation = dbn.update(observation, stage, true_target)

        # Predict most likely target
        prediction = dbn.predict()

        results.append({
            "stage": stage,
            "observation": observation,              # original cue
            "noisy_observation": noisy_observation,  # noisy cue (important for analysis)
            "small_prob": float(belief[0]),
            "large_prob": float(belief[1]),
            "prediction": prediction,
            "true_target": true_target,
            "correct": int(prediction == true_target)
        })

    return results