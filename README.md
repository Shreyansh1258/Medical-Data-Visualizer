# Medical Data Visualizer

A Python project to analyze and visualize medical examination data, focusing on cardiovascular health. This project uses **Pandas**, **Seaborn**, and **Matplotlib** to generate insights through **categorical plots** and **correlation heatmaps**.

---

## **Features**

- **Data Processing**
  - Computes BMI to classify patients as overweight or not.
  - Normalizes cholesterol and glucose values (0 = normal, 1 = above normal).
  
- **Visualizations**
  - **Categorical Plot:** Displays counts of binary features like smoking, alcohol intake, physical activity, cholesterol, glucose, and overweight status, split by cardiovascular disease presence.
  - **Heatmap:** Shows the correlation matrix between all numerical features, highlighting relationships among variables.

---

## **Dataset**

The project uses a CSV file `medical_examination.csv` with the following columns:

| Column | Description |
|--------|-------------|
| age | Age in days |
| height | Height in cm |
| weight | Weight in kg |
| gender | 1 = male, 2 = female |
| ap_hi | Systolic blood pressure |
| ap_lo | Diastolic blood pressure |
| cholesterol | 1 = normal, 2 = above normal, 3 = well above normal |
| gluc | 1 = normal, 2 = above normal, 3 = well above normal |
| smoke | 0 = non-smoker, 1 = smoker |
| alco | 0 = no alcohol, 1 = alcohol intake |
| active | 0 = inactive, 1 = physically active |
| cardio | 0 = no cardiovascular disease, 1 = has cardiovascular disease |

> Note: A sample CSV with test data is included for demonstration purposes.

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/medical-data-visualiser.git
cd medical-data-visualiser
