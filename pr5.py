import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

#5.1
means = np.mean(diabetes.data, axis=0)
print("---5.1 Середні значення атрибутів---")
for name, value in zip(diabetes.feature_names, means):
    print(f"{name}:{value:.6f}")

#5.2
df.hist(figsize=(10,8), bins=15, color='skyblue', edgecolor='black')
plt.suptitle('5.2 Гістограми всіх атрибутів')
plt.show()

#5.3
plt.figure(figsize=(10,6))
df.drop('target', axis=1).boxplot()
plt.title('5.3 Бокс-плоти базових ознак')
plt.show()

#5.4
df.boxplot(column='target', by='sex', figsize=(6,5), color='red')
plt.title('5.4 Розподіл прогресування хвороби за статтю')
plt.suptitle('')
plt.show()

#5.5
corr_matrix = df.corr()
print("\n--- 5.5 Кореляційна матриця ---")
print(corr_matrix)