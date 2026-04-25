"""
Experiment configurations for DBN model evaluation.

Each experiment simulates a different combination of cues:
- gaze: early perceptual cue (weak)
- hand: intermediate motor cue (moderate)
- trajectory: late movement cue (strong)

Values:
0 = small object
1 = large object
"""

EXPERIMENTS = [

    # Case 1: All cues are correct (baseline condition)
    {
        "name": "all_cues_correct_small",
        "gaze": 0,
        "hand": 0,
        "trajectory": 0,
        "true_target": 0,
        "description": "All cues correctly indicate the small object."
    },

    # Case 2: Gaze is misleading, later cues correct
    {
        "name": "gaze_wrong_hand_trajectory_correct_small",
        "gaze": 1,
        "hand": 0,
        "trajectory": 0,
        "true_target": 0,
        "description": "Gaze is misleading; hand and trajectory indicate the correct target."
    },

    # Case 3: Hand is misleading, other cues correct
    {
        "name": "gaze_correct_hand_wrong_trajectory_correct_large",
        "gaze": 1,
        "hand": 0,
        "trajectory": 1,
        "true_target": 1,
        "description": "Hand is misleading; gaze and trajectory indicate the correct target."
    },

    # Case 4: All cues are correct (large object)
    {
        "name": "all_cues_correct_large",
        "gaze": 1,
        "hand": 1,
        "trajectory": 1,
        "true_target": 1,
        "description": "All cues correctly indicate the large object."
    },

    # Case 5: Early cues misleading, final cue correct
    {
        "name": "gaze_and_hand_wrong_trajectory_correct_small",
        "gaze": 1,
        "hand": 1,
        "trajectory": 0,
        "true_target": 0,
        "description": "Gaze and hand are misleading; trajectory indicates the correct target."
    }
]