import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('Datasets/medical_examination.csv')

# Add 'overweight' column
bmi = (df['weight'] / (df['height'])**2).to_numpy()
df['overweight'] = np.where(bmi > 25, 1 , 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cardio'], var_name='variable', value_name='value')
  
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x='variable', col='cardio',kind='count', hue='value')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = (df = df[df['ap_lo'] <= df['ap_hi']]) & (df[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))]) & (df[(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]))
  
    # Calculate the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    fig = sn.heatmap(corr_matrix, mask=mask, annot=True, fmt=".1f", center=0, square=True, linewidths=.3, linecolor='white', cmap="coolwarm")
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
