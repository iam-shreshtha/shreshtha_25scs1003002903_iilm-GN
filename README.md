# shreshtha_25scs1003002903_iilm-GN
# 🌿 Wildlife Migration & Smart Lighting System

## 📌 Overview
This project simulates a **smart environmental monitoring system** that uses:
- Satellite migration signals  
- Distance of animals from human areas  
- Current light intensity  

to:
- Detect wildlife migration risk  
- Recommend optimal lighting conditions  
- Predict lighting decisions using a Machine Learning model  

---

## 🚀 Features

### 1. 📊 Data Generation
- Automatically creates a dataset (`migration_data.csv`)
- Includes:
  - Location types (Forest, River, City, etc.)
  - Migration signals from satellites
  - Distance from human settlements
  - Light intensity levels

---

### 2. ⚠️ Migration Risk Detection
Classifies migration into:
- **High Migration**
- **Medium Migration**
- **Low Migration**

Based on satellite signal strength.

---

### 3. 💡 Smart Light Recommendation
Rule-based system:
- **LOW Light** → When animals are near humans (reduce disturbance)
- **MEDIUM Light** → Moderate migration activity
- **HIGH Light OK** → Low migration

---

### 4. 🤖 Machine Learning Model
- Uses **Decision Tree Classifier**
- Learns from generated data
- Predicts lighting recommendations for new scenarios

Example:Input: Migration=90, Distance=1km, Light=85
Output: LOW Light Recommended

---

### 5. 📈 Data Visualization
- Scatter plot showing:
  - Migration signal vs Light intensity
- Helps understand environmental patterns

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas 📊
- Matplotlib 📈
- Scikit-learn 🤖

---

## 📂 Project Structure
├── main.py
├── migration_data.csv # Auto-generated
└── README.md

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas matplotlib scikit-learn
```

### 2. Run script 
```bash
python main.py
