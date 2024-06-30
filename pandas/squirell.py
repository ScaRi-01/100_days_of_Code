import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with multiple columns
data = {
    'Name': ['Rishabh', 'Ankit', 'Rohit', 'Pulaks'],
    'Age': [23, 34, 45, 56],
    'Salary': [50000, 60000, 75000, 90000],
    'Experience': [2, 5, 8, 10]
}
df = pd.DataFrame(data)

# Plot multiple columns against each other
df.set_index('Name')[['Age', 'Salary', 'Experience']].plot(kind='bar', figsize=(10, 6))

# Set titles and labels
plt.title('Multiple Columns Plot')
plt.xlabel('Name')
plt.ylabel('Value')

# Show plot
plt.show()
