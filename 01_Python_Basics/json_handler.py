"""
TOPIC: External Data Handling (JSON File I/O)

THE PROBLEM: 
In Machine Learning, data is rarely hardcoded. It usually comes from 
External APIs or Kaggle datasets in JSON format. If we don't save 
this data to a file, it disappears as soon as the program stops.

THE SOLUTION:
Using the 'json' library and Python 'Context Managers' (the 'with' keyword), 
we can safely write data to the hard drive and read it back later. 
This ensures our data is persistent and formatted correctly.
"""

import json
import os

# 1. THE MOCK DATA
# This represents structured data we might get from a web scraper or API
pakistan_car_data = [
    {"brand": "Toyota", "model": "Corolla", "units_sold": 45000, "city": "Karachi"},
    {"brand": "Suzuki", "model": "Alto", "units_sold": 82000, "city": "Lahore"},
    {"brand": "Honda", "model": "Civic", "units_sold": 18000, "city": "Islamabad"}
]

# Define the file path
file_path = "01_Python_Basics/pakistan_cars.json"

# 2. WRITING DATA (Saving to Hard Drive)
# 'w' mode stands for Write. 'indent=4' makes the JSON readable for humans.
with open(file_path, "w") as file:
    json.dump(pakistan_car_data, file, indent=4)

print(f"--- SUCCESS: Data written to {file_path} ---")

# 3. READING DATA (Loading into Python)
# 'r' mode stands for Read. This turns the file back into a Python List.
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        loaded_data = json.load(file)
    
    print(f"--- SUCCESS: Loaded {len(loaded_data)} records from file ---")
    
    # Verify by printing the first model loaded
    print(f"First car in record: {loaded_data[0]['model']}")