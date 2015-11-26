import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_csv('/Users/dogerdespeville/Desktop/article_segolene/raw_data_2.csv')

adapted_table = pd.DataFrame(columns=['Learning score','MG and CG','Learning'])

for i, row in raw_data.iterrows():
    new_rows_m = []
    new_rows_m.append([row['moyennesyne'],row['M/C'],'t1'])
    new_rows_m.append([row['moyenco'],row['M/C'],'t2'])
    for new_row in new_rows_m:
        adapted_table.loc[len(adapted_table)+1] = new_row

fig = plt.figure()
ax = fig.add_subplot(111)
plot1 = sns.pointplot(x="Learning",
                      y="Learning score",
                      hue="MG and CG",
                      data=adapted_table,
                      ax=ax)

plt.show()
fig.savefig('plot1.png')

adapted_table = pd.DataFrame(columns=['Recognition Score','MG and CG','Object'])

for i, row in raw_data.iterrows():
    new_rows_r = []
    new_rows_r.append([row['recupbanane'],row['M/C'],'Banana'])
    new_rows_r.append([row['recupcitron'],row['M/C'],'Lemon'])
    new_rows_r.append([row['recuplavande'],row['M/C'],'Lavender'])
    new_rows_r.append([row['recuptruffe'],row['M/C'],'Truffle'])
    for new_row in new_rows_r:
        adapted_table.loc[len(adapted_table)+1] = new_row

fig = plt.figure()
ax = fig.add_subplot(111)
plot2 = sns.barplot(x="MG and CG",
                    y="Recognition Score",
                    hue="Object",
                    data=adapted_table,
                    hue_order = ['Banana','Lemon','Lavender','Truffle'],
                    palette=['green','yellow','blue','red'],
                    ax=ax)
plt.show()

fig.savefig('plot2.png')
