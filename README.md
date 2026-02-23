# K-Nearest Neighbors (KNN) from Scratch — Python & NumPy

This repository contains a **from-scratch implementation of the K-Nearest Neighbors (KNN) algorithm**  
using only **Python and NumPy**, without any machine learning libraries.

It includes a **realistic synthetic dataset of houses** with multiple features, scaling, and optional PCA visualization for insights.

---

## 🎯 Goal

To deeply understand:

- How distance-based classification works
- The role of similarity metrics in supervised learning
- How the choice of **K** affects bias–variance tradeoff
- Why KNN has no explicit training phase
- How preprocessing (scaling, PCA) affects model performance

## 🧠 Algorithm Overview

KNN is a **supervised, non-parametric, lazy learning** algorithm.

### Core Idea

1. Store all training samples
2. For a new input point:
   - Compute distance to all training points (**Euclidean** or **Manhattan**)
   - Select the **K nearest neighbors**
   - Predict the label using **majority voting**

## ✏️ Mathematical Intuition

### Distance Metrics

- **Euclidean distance**:

> d(x, xᵢ) = √(∑(x − xᵢ)²)

- **Manhattan distance**:

> d(x,y)=∑∣xi​−yi​∣

### Prediction Rule
ŷ = most frequent label among the K nearest neighbors

---

## 🏡 Dataset Scenario

- Synthetic housing dataset with **1200 samples**
- Features:
  - Area (m²), Rooms, Building Age, Distance to City Center
  - Floor, Elevator, Parking
- Target: **Price Category (5 classes: Economy → Luxury)**
- Includes realistic noise and overlapping classes
- Suitable for KNN, visualization, and PCA exploration

## 📊 Observations & Results

- **Small K values**:
  - Low bias
  - High variance
  - Sensitive to noise
- **Large K values**:
  - Smoother decision boundary
  - Potential underfitting
- Scaling and PCA clearly show **clusters and separability**
- Distance metric choice affects nearest neighbor selection

## ✅ Advantages

- Very simple to understand and implement
- No explicit training phase
- Works well on small to medium datasets
- Highly interpretable
- Provides clear insight with visualization

## ❌ Disadvantages

- Slow inference on large datasets (**O(n)**)
- High memory usage (stores all data)
- Sensitive to noisy data
- Strongly affected by feature scaling
- Choosing K is non-trivial

## 🛠 Tech Stack

- Python  
- NumPy (for calculation and data manipulation)  
- Matplotlib (for visualization and debugging)  
- Scikit-learn **only for StandardScaler / PCA** (optional)

---

## 🚀 Why this project?

This project demonstrates **understanding, not abstraction**.  
It shows my ability to:

- Implement algorithms from scratch
- Handle preprocessing and dimensionality reduction
- Reason about bias–variance tradeoff and distance metrics
- Visualize high-dimensional data intuitively
