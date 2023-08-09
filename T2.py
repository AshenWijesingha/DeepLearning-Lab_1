import pandas as pd

# 1. Download the Au_nanoParticle_dataset.csv and load the data of the csv file as a dataframe in a new colab notebook.
df = pd.read_csv('Au_nanoParticle_dataset.csv')

# 2. Create a new dataframe by filtering all the columns [i.e., features] except N_total, N_bulk, N_surface and R_avg columns.
new_df = df[['Temp', 'Time', 'N_atoms', 'N_ligands']]

# 3. Display the first 20 samples of this dataframe.
print(new_df.head(20))

# 4. Calculate the mean, standard deviation and quartile values for each of the above 4 features.
for col in new_df.columns:
  print('Column name:', col)
  print('Mean:', new_df[col].mean())
  print('Standard deviation:', new_df[col].std())
  print('25th percentile:', new_df[col].quantile(0.25))
  print('50th percentile:', new_df[col].quantile(0.5))
  print('75th percentile:', new_df[col].quantile(0.75))

# 5. Plot the histogram of each of these features in a 1x4 layout.
fig, axes = plt.subplots(1, 4, figsize=(12, 4))
for i in range(len(new_df.columns)):
  axes[i].hist(new_df.iloc[:, i])
  axes[i].set_title(new_df.columns[i])
plt.show()


# 6. Visualize the scatter plots and histograms of this dataframe using the pairplot functionality of seaborn library.
import seaborn as sns

sns.pairplot(new_df)
plt.show()


# 7. Add the below code and change it such that.
# new_df is the dataframe containing only the above mentioned 4 features.
g = sns.PairGrid(new_df)
g.map_upper(sns.histplot) #bivariate histogram
g.map_diag(sns.histplot) 
g.map_lower(sns.kdeplot) 

