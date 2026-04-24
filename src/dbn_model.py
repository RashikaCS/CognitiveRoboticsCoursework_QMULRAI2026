import numpy as np


class DynamicBayesianNetwork:
    def __init__(self):
        self.states = [0, 1]  # 0 = small object, 1 = large object
        self.initial_belief = np.array([0.5, 0.5], dtype=float)
        self.belief = self.initial_belief.copy()

        self.transition = np.array([
            [0.90, 0.10],
            [0.10, 0.90]
        ])

        self.reliability = {
            "gaze": 0.60,
            "hand": 0.80,
            "trajectory": 0.95
        }

    def reset(self):
        self.belief = self.initial_belief.copy()

    def likelihood(self, observation, state, cue_type):
        reliability = self.reliability[cue_type]
        return reliability if observation == state else 1 - reliability

    def update(self, observation, cue_type):
        predicted = self.transition.T @ self.belief

        likelihoods = np.array([
            self.likelihood(observation, state, cue_type)
            for state in self.states
        ])

        posterior = predicted * likelihoods
        posterior = posterior / posterior.sum()

        self.belief = posterior
        return posterior

    def predict(self):
        return int(np.argmax(self.belief))