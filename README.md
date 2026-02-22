# K-Nearest Neighbors (KNN) from Scratch — Python & NumPy

This repository contains a **from-scratch implementation of the K-Nearest Neighbors (KNN) algorithm**
using only **Python and NumPy**, without any machine learning libraries.

The goal of this project is to demonstrate **conceptual understanding of instance-based learning**
and distance-driven decision making.

## 🎯 Goal
To deeply understand:
- How distance-based classification works
- The role of similarity metrics in supervised learning
- How the choice of **K** affects bias–variance tradeoff
- Why KNN has no explicit training phase

## 🧠 Algorithm Overview

KNN is a **supervised, non-parametric, lazy learning** algorithm.

### Core idea:
1. Store all training samples
2. For a new input point:
   - Compute distance to all training points
   - Select the **K nearest neighbors**
   - Predict the label using **majority voting**

## ✏️ Mathematical Intuition

### Distance Metric
Euclidean distance is used:

d(x, xᵢ) = √(∑(x − xᵢ)²)

Manhattan distance is used:

d(x,y)=∑∣xi​−yi​∣

### Prediction Rule
ŷ = most frequent label among the K nearest neighbors

## 📊 Observations & Results

- Small K values:
  - Low bias
  - High variance
  - Sensitive to noise
- Large K values:
  - Smoother decision boundary
  - Potential underfitting

This implementation clearly shows the **bias–variance tradeoff** controlled by K.

## ✅ Advantages
- Very simple to understand and implement
- No explicit training phase
- Works well on small to medium datasets
- Highly interpretable

## ❌ Disadvantages
- Slow inference on large datasets (**O(n)**)
- High memory usage (stores all data)
- Sensitive to noisy data
- Strongly affected by feature scaling
- Choosing K is non-trivial

## 🛠 Tech Stack
- Python
- NumPy (read and visualization dataset)
- Matplotlib (for visualization and debugging)

## 🚀 Why this project?
This project focuses on **understanding, not abstraction**.
It demonstrates my ability to:
- Strong understanding of KNN fundamentals
- Ability to implement algorithms from scratch
- Awareness of real-world limitations and solutions
