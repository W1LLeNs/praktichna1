import pandas as pd
from sklearn.datasets import load_diabetes
#4.1
diabetes = load_diabetes()
#tablitsya data frame
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
#4.2
print("---Перші 5 записів датасету---")
print(df.head())
#4.3
print("\n---Основна статистична інформація---")
print(df.describe())
#4.4
print("\n---Кількість записів за ознакою статі---")
print(df['sex'].value_counts())