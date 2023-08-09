import seaborn as sns
import pandas as pd

df = pd.read_csv('pokemon.csv')

pearson_coef = {}
spearman_coef = {}

for col in ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']:
  pearson_coef[col] = round(df['Total'].corr(df[col]), 2)
  spearman_coef[col] = round(df['Total'].corr(df[col], method='spearman'), 2)

corr = pd.DataFrame(pearson_coef, index=['Total'])
corr.rename(columns={'Total': 'Pearson coefficient'}, inplace=True)
corr['Spearman coefficient'] = spearman_coef

sns.heatmap(corr, annot=True, cmap='viridis')
plt.show()
