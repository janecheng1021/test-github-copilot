import pandas as pd
import json
import matplotlib.pyplot as plt

# Load Excel
df = pd.read_excel("Copilot_Refactor_Metrics_Sample.xlsx")

# Display the contents of the Excel file
print("Contents of the Excel file:")
print(df.to_string(index=False))

# Convert data to JSON format
projects_data = []
for _, row in df.iterrows():
    projects_data.append({
        "name": row["File/Module Name"],
        "progress": row["Progress (%)"] if "Progress (%)" in row else 0
    })

# Save JSON data to projects.json
with open("projects.json", "w") as json_file:
    json.dump({"projects": projects_data}, json_file, indent=4)

print("Data successfully loaded into projects.json")

# Plot data from the Excel file
plt.figure(figsize=(10, 6))

# Example: Plotting 'Time Saved (min)' for each 'File/Module Name'
df.plot(x="File/Module Name", y="Time Saved (min)", kind="bar", legend=False)
plt.title("Time Saved per File")
plt.xlabel("File/Module Name")
plt.ylabel("Time Saved (min)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()