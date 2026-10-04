import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Marks": [78, 65, 92, 55, 88]
}

# DataFrame banana
df = pd.DataFrame(data)

print("----- Student Marks -----")
print(df)

# Average marks
average = df["Marks"].mean()

# Highest marks
highest = df["Marks"].max()

# Lowest marks
lowest = df["Marks"].min()

# Pass/Fail
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("\n----- Analysis -----")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print("\n----- Result -----")
print(df)

# Bar chart
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()