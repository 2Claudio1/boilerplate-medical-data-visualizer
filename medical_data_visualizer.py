import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# 2 Create the overweight column in the df variable (overweight is when BMI >= 25.0)
# Sets overweight as 1 if the MBI > 25 else overweight = 0. BMI = weight (kg) / height (m)^2
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2))).apply(lambda x: 1 if x > 25.0 else 0)

# 3 Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0.
# If the value is more than 1, set the value to 1.

# For each row sets, checks if cholesterol == 1 and sets it as 0. Colesterol must always be > 0. Same thing with gluc
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)

df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4 Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, 
    # smoke, alco, active, and overweight in the df_cat variable.
    df_cat = None


    # 6 Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. 
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    

    # 7Convert the data into long format and create a chart that shows the value counts of the categorical features 
    # using the following method provided by the seaborn library import : sns.catplot()



    # 8 Get the figure for the output and store it in the fig variable
    fig = None


    # 9 Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# 10 Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 11 Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    # diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))

    # height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))

    # height is more than the 97.5th percentile

    # weight is less than the 2.5th percentile

    df_heat = None

    # 12 Calculate the correlation matrix and store it in the corr variable
    corr = None

    # 13 Generate a mask for the upper triangle and store it in the mask variable
    mask = None

    # 14 Set up the matplotlib figure
    fig, ax = None

    # 15 Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap()


    # 16 Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
