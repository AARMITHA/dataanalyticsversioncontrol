import pandas as pd

# Sample data
data = pd.DataFrame({
    'Age': [22, 25, 28, 29, 31],
    'Salary': [50000, 60000, 55000, 58000, 61000]
})

# Basic analysis
average_salary = data['Salary'].mean()
max_age = data['Age'].max()
min_age = data['Age'].min()

print('📊 Basic Data Analysis Report')
print('Average Salary:', average_salary)
print('Oldest Age:', max_age)
print('Youngest Age:', min_age)
