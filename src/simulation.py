from src.dbn_model import DynamicBayesianNetwork


def run_single_trial(gaze, hand, trajectory, true_target):
    dbn = DynamicBayesianNetwork()

    cue_sequence = [
        ("gaze", gaze),
        ("hand", hand),
        ("trajectory", trajectory)
    ]

    results = []

    for stage, observation in cue_sequence:
        belief = dbn.update(observation, stage)
        prediction = dbn.predict()

        results.append({
            "stage": stage,
            "observation": observation,
            "small_prob": float(belief[0]),
            "large_prob": float(belief[1]),
            "prediction": prediction,
            "true_target": true_target,
            "correct": int(prediction == true_target)
        })

    return results