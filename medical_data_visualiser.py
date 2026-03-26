# medical_data_visualiser.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process_data(csv_file):
    
    df = pd.read_csv(csv_file)

    # Clean column names 
    df.columns = df.columns.str.strip().str.lower()

    # Check required columns exist
    required_cols = ["weight", "height", "cholesterol", "gluc", "smoke", "alco", "active", "cardio", "ap_lo", "ap_hi"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in CSV!")

    # Add overweight column (BMI > 25)
    df["overweight"] = (df["weight"] / ((df["height"]/100)**2) > 25).astype(int)

    # Normalize cholesterol and glucose 
    df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
    df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

    return df

def cat_plot(df):
    """
    Draw categorical plot and save as catplot.png
    """
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # Count occurrences
    df_cat["total"] = 1
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()

    # Plot
    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar"
    ).fig

    fig.savefig("catplot.png")
    return fig

def heat_map(df):
    
    # Remove outliers
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Correlation
    corr = df_heat.corr(method="pearson")

    # Mask upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Plot heatmap
    fig, ax = plt.subplots(figsize=(12,12))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig("heatmap.png")
    return fig