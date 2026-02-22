import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 1200
file_name = f"house_type_dataset_{n_samples}.csv"

area = np.random.normal(110, 35, n_samples).clip(40, 300)
rooms = np.clip((area / 35).astype(int), 1, 6)
age = np.random.exponential(scale=20, size=n_samples).clip(0, 60)
distance = np.random.gamma(shape=2, scale=4, size=n_samples).clip(0.5, 25)

floor = np.random.randint(0, 15, n_samples)
has_elevator = (floor >= 3).astype(int)
has_parking = np.random.binomial(1, 0.65, n_samples)

# Realistic price formula
price = (
    area * 3_500
    + rooms * 25_000
    - age * 1_200
    - distance * 4_000
    + has_elevator * 40_000
    + has_parking * 50_000
    + np.random.normal(0, 40_000, n_samples)
)

price = price.clip(100_000, None)

# Convert type to categories
type_category = pd.qcut(
    price,
    q=5,
    labels=[0, 1, 2, 3, 4]
)

df = pd.DataFrame({
    "Area": area.astype(int),
    "Rooms": rooms,
    "BuildingAge": age.astype(int),
    "DistanceToCenter": distance.round(1),
    "Floor": floor,
    "HasElevator": has_elevator,
    "HasParking": has_parking,
    "TypeCategory": type_category.astype(int)
})

df.to_csv(file_name, index=False)
print(f"{file_name} Saved ✅")
