import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------
# 1. CREATE CSV AUTOMATICALLY (Migration + Satellite + Light)
# ---------------------------------------------------------

data_dict = {
    "location": ["Forest Zone", "River Side", "Village Edge", "Highway Side", "City Park"],

    # 1. Satellite detecting migration (0 = none, 100 = many animals)
    "satellite_migration_signal": [85, 70, 40, 20, 10],

    # 2. Distance of migrating animals from human areas (km)
    "distance_from_humans_km": [1.5, 3.0, 6.0, 10.0, 12.0],

    # 3. Current light intensity at night (0-100 scale)
    "current_light_intensity": [80, 60, 50, 40, 30]
}

df = pd.DataFrame(data_dict)
df.to_csv("migration_data.csv", index=False)

print("CSV FILE CREATED!\n")
print(df)


# ---------------------------------------------------------
# 2. ANALYZE MIGRATION RISK
# ---------------------------------------------------------

def detect_risk(row):
    if row['satellite_migration_signal'] > 70:
        return "High Migration"
    elif row['satellite_migration_signal'] > 40:
        return "Medium Migration"
    else:
        return "Low Migration"

df["migration_risk"] = df.apply(detect_risk, axis=1)

print("\n--- MIGRATION RISK DETECTED ---")
print(df[['location', 'satellite_migration_signal', 'migration_risk']])


# ---------------------------------------------------------
# 3. LIGHT INTENSITY RECOMMENDATION (Rule-based)
# ---------------------------------------------------------

def light_control(row):
    if row['satellite_migration_signal'] > 70 and row['distance_from_humans_km'] < 3:
        return "LOW Light Recommended"
    elif row['satellite_migration_signal'] > 40:
        return "MEDIUM Light Recommended"
    else:
        return "HIGH Light OK"

df["light_recommendation"] = df.apply(light_control, axis=1)

print("\n--- LIGHT INTENSITY RECOMMENDATIONS ---")
print(df[['location', 'migration_risk', 'light_recommendation']])


# ---------------------------------------------------------
# 4. SIMPLE ML MODEL (Decision Tree)
# ---------------------------------------------------------

# ML Input features
X = df[['satellite_migration_signal', 'distance_from_humans_km', 'current_light_intensity']]

# ML Output (label we want to predict)
y = df['light_recommendation']

# Create decision tree model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Test ML with a new satellite reading
new_data = [[90, 1.0, 85]]   # (High migration, close distance, high light)
prediction = model.predict(new_data)

print("\n--- ML PREDICTION ---")
print("For migration=90, distance=1 km, light intensity=85 →")
print("ML Suggests:", prediction[0])


# ---------------------------------------------------------
# 5. GRAPH: Migration detected vs Light Intensity
# ---------------------------------------------------------

plt.figure(figsize=(8,5))
plt.scatter(df['satellite_migration_signal'], df['current_light_intensity'])
plt.title("Satellite-detected Migration vs Light Intensity")
plt.xlabel("Migration Signal (Satellite)")
plt.ylabel("Current Light Intensity")
plt.grid(True)
plt.show()