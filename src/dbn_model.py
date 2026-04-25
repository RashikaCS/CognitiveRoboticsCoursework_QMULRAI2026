import numpy as np


class DynamicBayesianNetwork:
    def __init__(self):
        # Hidden states: 0 = small object, 1 = large object
        self.states = [0, 1]

        # Initial belief (complete uncertainty)
        self.initial_belief = np.array([0.5, 0.5], dtype=float)
        self.belief = self.initial_belief.copy()

        # Transition probabilities between states
        self.transition = np.array([
            [0.90, 0.10],
            [0.10, 0.90]
        ])

        # Reliability of each cue
        self.reliability = {
            "gaze": 0.55,
            "hand": 0.70,
            "trajectory": 0.85
        }

        # Noise probabilities (simulate human perception errors)
        self.noise_probability = {
            "gaze": 0.20,
            "hand": 0.12,
            "trajectory": 0.08
        }

        # Learning rate
        self.learning_rate = 0.05

    def reset(self):
        """Reset belief to initial state"""
        self.belief = self.initial_belief.copy()

    def apply_noise(self, observation, cue_type):
        """Flip observation with some probability (simulate noise)"""
        if np.random.rand() < self.noise_probability[cue_type]:
            return 1 - observation
        return observation

    def likelihood(self, observation, state, cue_type):
        """Compute likelihood P(observation | state)"""
        reliability = self.reliability[cue_type]
        return reliability if observation == state else 1 - reliability

    def update(self, observation, cue_type, true_target=None):
        """
        DBN update step:
        - apply noise
        - predict belief
        - update posterior
        - update reliability (learning)
        """

        # Apply noise
        noisy_observation = self.apply_noise(observation, cue_type)

        # Predict next belief
        predicted = self.transition.T @ self.belief

        # Likelihood
        likelihoods = np.array([
            self.likelihood(noisy_observation, state, cue_type)
            for state in self.states
        ])

        # Posterior update
        posterior = predicted * likelihoods
        posterior = posterior / posterior.sum()

        self.belief = posterior

        # Learning
        if true_target is not None:
            prediction = self.predict()
            correct = int(prediction == true_target)

            self.reliability[cue_type] += self.learning_rate * (
                correct - self.reliability[cue_type]
            )

            self.reliability[cue_type] = float(
                np.clip(self.reliability[cue_type], 0.5, 0.95)
            )

        return posterior, noisy_observation

    def predict(self):
        """Return predicted class"""
        return int(np.argmax(self.belief))