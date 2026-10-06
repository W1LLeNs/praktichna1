import numpy as np

arr_1d = np.array([10,20,30])
arr_2d = np.array([[1,2,3], [4,5,6]])

print("Розмірність одномірного масиву:", arr_1d.shape)
print("Розмірність двомірного масиву:", arr_2d.shape)

print("\n Додаємо 7 до всього масиву:", arr_2d+7)
print("Множимо весь масив на 3:", arr_2d*3)

arr_step = np.arange(0, 1.1, 0.1)
print("\n Масив з кроком 0.1:\n", arr_step)

a=np.array([1,2,3])
b=np.array([4,5,6])
dot_result = np.dot(a,b)
print("\n Скалярний добуток масивів a і b:", dot_result)