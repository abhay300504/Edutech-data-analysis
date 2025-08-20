import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the employee data (creating a sample DataFrame)
# In a real-world scenario, you would load your data using pd.read_csv('your_file.csv')
np.random.seed(42) # for reproducibility
departments = ['Sales', 'HR', 'Engineering', 'Marketing', 'Support', 'Finance']
data = {
    'Employee ID': [f'E{1000+i}' for i in range(100)],
    'Department': np.random.choice(departments, 100, p=[0.3, 0.1, 0.25, 0.15, 0.1, 0.1]),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Performance Score': np.random.randint(60, 100, 100)
}
employee_df = pd.DataFrame(data)

# 2. Calculate the frequency count for the "HR" department
hr_frequency_count = employee_df[employee_df['Department'] == 'HR'].shape[0]

# 3. Print the frequency count to the console
print(f"Frequency count for the HR department: {hr_frequency_count}")

# 4. Create a histogram showing the distribution of departments
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

department_counts = employee_df['Department'].value_counts()
department_counts.plot(kind='bar', ax=ax, color='#4A90E2')

ax.set_title('Employee Distribution Across Departments', fontsize=16, fontweight='bold')
ax.set_xlabel('Department', fontsize=12)
ax.set_ylabel('Number of Employees', fontsize=12)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

# Save the visualization as a PNG file
plt.savefig('department_distribution.png')

print("\nVisualization saved as 'department_distribution.png'")

# To fulfill the HTML requirement, we can wrap the code and output in a simple HTML file.
# Note: This is a manual step. For a self-contained interactive plot, libraries like Plotly would be used.

python_code = """
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
departments = ['Sales', 'HR', 'Engineering', 'Marketing', 'Support', 'Finance']
data = {
    'Employee ID': [f'E{1000+i}' for i in range(100)],
    'Department': np.random.choice(departments, 100, p=[0.3, 0.1, 0.25, 0.15, 0.1, 0.1]),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Performance Score': np.random.randint(60, 100, 100)
}
employee_df = pd.DataFrame(data)

hr_frequency_count = employee_df[employee_df['Department'] == 'HR'].shape[0]
print(f"Frequency count for the HR department: {hr_frequency_count}")

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

department_counts = employee_df['Department'].value_counts()
department_counts.plot(kind='bar', ax=ax, color='#4A90E2')

ax.set_title('Employee Distribution Across Departments', fontsize=16, fontweight='bold')
ax.set_xlabel('Department', fontsize=12)
ax.set_ylabel('Number of Employees', fontsize=12)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

plt.savefig('department_distribution.png')
"""

html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance Analysis</title>
    <style>
        body {{ font-family: sans-serif; margin: 2em; }}
        pre {{ background-color: #f4f4f4; padding: 1em; border-radius: 5px; }}
        img {{ max-width: 100%; height: auto; border: 1px solid #ccc; }}
    </style>
</head>
<body>
    <h1>Employee Performance Analysis</h1>
    <h2>Python Code</h2>
    <pre><code>{python_code}</code></pre>
    <h2>Console Output</h2>
    <pre>Frequency count for the HR department: {hr_frequency_count}</pre>
    <h2>Generated Visualization</h2>
    <p>Note: This HTML displays a static image. The Python script generates 'department_distribution.png' which would need to be in the same directory.</p>
    <img src="department_distribution.png" alt="Department Distribution Histogram">
</body>
</html>
'''

# Save the HTML file
with open('employee_analysis.html', 'w') as f:
    f.write(html_content)

print("HTML file 'employee_analysis.html' has been created.")