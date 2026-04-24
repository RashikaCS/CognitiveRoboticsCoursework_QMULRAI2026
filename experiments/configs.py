EXPERIMENTS = [
    {
        "name": "all_cues_correct_small",
        "gaze": 0,
        "hand": 0,
        "trajectory": 0,
        "true_target": 0,
        "description": "All cues correctly indicate the small object."
    },
    {
        "name": "gaze_wrong_hand_trajectory_correct_small",
        "gaze": 1,
        "hand": 0,
        "trajectory": 0,
        "true_target": 0,
        "description": "Gaze is misleading, but hand and trajectory correctly indicate the small object."
    },
    {
        "name": "gaze_correct_hand_wrong_trajectory_correct_large",
        "gaze": 1,
        "hand": 0,
        "trajectory": 1,
        "true_target": 1,
        "description": "Gaze and trajectory indicate large object, hand is misleading."
    },
    {
        "name": "all_cues_correct_large",
        "gaze": 1,
        "hand": 1,
        "trajectory": 1,
        "true_target": 1,
        "description": "All cues correctly indicate the large object."
    },
    {
        "name": "gaze_and_hand_wrong_trajectory_correct_small",
        "gaze": 1,
        "hand": 1,
        "trajectory": 0,
        "true_target": 0,
        "description": "Gaze and hand are misleading, but trajectory correctly indicates small object."
    }
]