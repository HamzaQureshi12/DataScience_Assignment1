# Scattor Plot

import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [0,10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110,120]  # Updated marks_range

# Create the scatter plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size

# Plot the data points for Math Marks
plt.scatter(math_marks, science_marks, label="Science Marks", color="blue", marker="o")

# Set labels for the axes
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")  # Updated y-axis label
# Set a title for the plot
plt.title("Scatter Plot: Math Marks vs. Science Marks")
# Plot the data points for Science Marks
plt.scatter(science_marks, math_marks, label="Math Marks", color="green")
# Show the legend (two labels)
plt.legend()
# Show the plot
plt.xticks(marks_range)  # Updated x-axis ticks
plt.yticks(marks_range)  # Updated y-axis ticks
plt.show()

# Bar Plot
import matplotlib.pyplot as plt

# Sample data
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a bar chart
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(languages, popularity, color=['orange'])

# Add labels and a title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages Among Developers")

# Add labels to the bars
for i in range(len(languages)):
    plt.text(i, popularity[i], f"{popularity[i]}%", ha='center', va='bottom')

# Show the bar chart
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()

#  Line Plot

import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib.ticker import MaxNLocator
amazon_data = pd.read_csv('AMZN_data.csv')
google_data = pd.read_csv('GOOGL_data.csv')
apple_data = pd.read_csv('AAPL_data.csv')
facebook_data = pd.read_csv('FB_data.csv')
microsoft_data = pd.read_csv('MSFT_data.csv')
plt.figure(figsize=(12, 6))
fig, ax = plt.subplots(figsize=(12, 6))
plt.plot(amazon_data['date'], amazon_data['close'], label='Amazon')
plt.plot(google_data['date'], google_data['close'], label='Google')
plt.plot(apple_data['date'], apple_data['close'], label='Apple')
plt.plot(facebook_data['date'], facebook_data['close'], label='Facebook')
plt.plot(microsoft_data['date'], microsoft_data['close'], label='Microsoft')
plt.title('Stock Prices of Big Five Companies (Past 5 Years)')
plt.xlabel('date')
plt.ylabel('Closing Price (USD)')
num_dates = len(amazon_data['date'])
step = num_dates // 30
ax.set_xticks(ax.get_xticks()[::step])
plt.xticks(rotation=45)
ax.set_yticks(range(0, int(max(amazon_data['close'])) + 100, 100))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
