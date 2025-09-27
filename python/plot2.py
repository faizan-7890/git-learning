import matplotlib.pyplot as plt
import pandas as pd

# 🔹 Load real dataset (AirPassengers dataset)
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url)

# Preview dataset
print(df.head())

# x = Months, y = Passengers
x = df["Month"]
y = df["Passengers"]

# 🔹 Simple Line Plot
plt.figure(figsize=(10,4))
plt.plot(x, y, color="blue", linestyle="-", marker="o")
plt.title("Simple Line Plot: Airline Passengers Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=45)
plt.show()