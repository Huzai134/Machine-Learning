"""
TOPIC: Memory Optimization in Python (Lists vs. Generators)

THE PROBLEM: 
When processing large datasets (like 1 million+ rows from Kaggle), 
using a List Comprehension [] attempts to load every single item 
into the computer's RAM simultaneously. This can lead to MemoryErrors 
and system crashes on standard laptops.

THE SOLUTION:
A Generator Expression () uses 'Lazy Evaluation'. It does not store 
the data in memory. Instead, it stores the 'instruction' to create 
the next item only when requested. This keeps the memory footprint 
constant (extremely low) regardless of the dataset size.
"""

import sys

# 1. Setup: A massive range of 1 million numbers
massive_data = range(1000000)

# 2. List Comprehension: Immediate memory allocation
# 
list_comp = [x * 2 for x in massive_data]

# 3. Generator Expression: 'Lazy' allocation (one at a time)
gen_exp = (x * 2 for x in massive_data)

# 4. Proof: Compare the size in bytes
list_size = sys.getsizeof(list_comp)
gen_size = sys.getsizeof(gen_exp)

print(f"List Size: {list_size} bytes")
print(f"Generator Size: {gen_size} bytes")
print(f"Efficiency Gain: The list uses ~{list_size // gen_size}x more memory!")