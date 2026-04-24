# CognitiveRoboticsCoursework_QMULRAI2026

## Title
The eye in hand: predicting others' behaviour by integrating multiple sources

## Overview
This project implements a computational cognitive model for human action prediction using a Dynamic Bayesian Network (DBN).

The model is inspired by the paper "The eye in hand: predicting others' behavior by integrating multiple sources of information". The aim is to model how humans integrate multiple cues such as gaze direction, hand preshape, and arm trajectory to infer another person's action goal.

## Computational Technique
Dynamic Bayesian Network (DBN)

A DBN is a probabilistic model that updates beliefs over time. In this project, the hidden state is the predicted action target, and the observed cues arrive sequentially.

## Cognitive Model
The model predicts which object a human actor intends to reach:

- `0` = small object
- `1` = large object

Observed cues:

- `gaze`: early but less reliable cue
- `hand`: stronger motor cue
- `trajectory`: strongest late cue

The DBN updates belief after each cue.

## Repository Structure

```text
src/
  dbn_model.py       Core Dynamic Bayesian Network model
  simulation.py      Trial-level simulation logic
  utils.py           Helper functions

experiments/
  configs.py         Experimental conditions
  run_experiments.py Runs DBN experiments
  plots.py           Generates result figures
  results.csv        Experiment output

results/
  figures/           Generated plots
  logs/              Experiment logs

docs/
  Report and slides

media/
  Screenshots or demo files