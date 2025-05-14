Here's a comprehensive Python code snippet that demonstrates different data types with explanations and examples, perfect for learning and practicing Python's fundamental data types:

```python
"""
Python Data Types Learning Snippet
Covers: Basic types, sequences, mappings, sets, and special types
"""

# ===== BASIC DATA TYPES =====
# 1. Integers (int)
age = 25
temperature = -10
binary_number = 0b1010  # Binary literal (10 in decimal)
hex_number = 0xFF       # Hexadecimal literal (255 in decimal)

print("\n=== INTEGERS ===")
print(f"Age: {age} (type: {type(age)})")
print(f"Binary 1010: {binary_number}")

# 2. Floating-point numbers (float)
pi = 3.14159
scientific = 2.5e-3  # 0.0025

print("\n=== FLOATS ===")
print(f"Pi: {pi:.2f}")  # Formatted to 2 decimal places
print(f"Scientific: {scientific}")

# 3. Booleans (bool)
is_active = True
has_permission = False

print("\n=== BOOLEANS ===")
print(f"5 > 3: {5 > 3}")  # Expression evaluates to boolean

# 4. Strings (str)
name = "Alice"
multiline = """This is a
multi-line string"""
raw_string = r"C:\new_folder"  # Raw string (ignores escape characters)

print("\n=== STRINGS ===")
print(f"Name: {name.upper()}")  # String methods
print(f"First letter: {name[0]}")  # Indexing
print(raw_string)

# ===== SEQUENCE TYPES =====
# 5. Lists (list) - Mutable sequence
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
numbers = [1, 2.5, "three"]  # Can hold mixed types

print("\n=== LISTS ===")
print(f"Fruits: {fruits}")
print(f"Sliced: {fruits[1:3]}")  # Slicing

# 6. Tuples (tuple) - Immutable sequence
coordinates = (10.5, 20.3)
single_element = (42,)  # Note the comma for single-element tuples

print("\n=== TUPLES ===")
print(f"Coordinates: {coordinates}")
print(f"Unpacking: x={coordinates[0]}, y={coordinates[1]}")

# 7. Range (range)
even_numbers = range(0, 10, 2)  # Start, stop, step

print("\n=== RANGE ===")
print(f"Range: {list(even_numbers)}")  # Convert to list to view

# ===== MAPPING TYPE =====
# 8. Dictionaries (dict) - Key-value pairs
person = {
    "name": "Bob",
    "age": 30,
    "skills": ["Python", "SQL"]
}

print("\n=== DICTIONARIES ===")
print(f"Person: {person}")
print(f"Skills: {person.get('skills', [])}")

# ===== SET TYPES =====
# 9. Sets (set) - Unique, unordered elements
unique_numbers = {1, 2, 3, 3, 2}  # Duplicates removed
empty_set = set()  # {} creates empty dict!

# 10. Frozen sets (frozenset) - Immutable set
constants = frozenset([3.14, 2.71, 1.62])

print("\n=== SETS ===")
print(f"Unique numbers: {unique_numbers}")
print(f"Intersection: {unique_numbers & {2, 4, 6}}")

# ===== SPECIAL TYPES =====
# 11. NoneType
result = None

print("\n=== NONETYPE ===")
print(f"Result: {result} (type: {type(result)})")

# 12. Bytes (bytes) and Bytearray (bytearray)
binary_data = b"Python"  # Immutable
mutable_binary = bytearray(binary_data)

print("\n=== BINARY TYPES ===")
print(f"Bytes: {binary_data}")
print(f"Bytearray: {mutable_binary}")

# ===== TYPE CONVERSION =====
print("\n=== TYPE CONVERSION ===")
num_str = "123"
print(f"String to int: {int(num_str)}")
print(f"Float to int: {int(3.99)}")  # Truncates
print(f"List to tuple: {tuple([1, 2, 3])}")
print(f"Dict to list (keys): {list(person.keys())}")

# ===== TYPE CHECKING =====
print("\n=== TYPE CHECKING ===")
print(f"Is 'hello' a string? {isinstance('hello', str)}")
print(f"Is 3.14 numeric? {isinstance(3.14, (int, float))}")

"""
Practice Exercises:
1. Create a dictionary with mixed types
2. Convert between string/list/tuple
3. Experiment with set operations
4. Try invalid conversions and handle exceptions
"""
```

### Key Features of This Snippet:
1. **Covers all major Python data types**:
   - Numeric (int, float, complex)
   - Sequences (str, list, tuple, range)
   - Mappings (dict)
   - Sets (set, frozenset)
   - Binary (bytes, bytearray)
   - NoneType

2. **Practical Demonstrations**:
   - Shows type conversion between different types
   - Includes common operations for each type
   - Demonstrates type checking with isinstance()

3. **Learning-Friendly**:
   - Clear section headers
   - Example outputs in comments
   - Suggested practice exercises
   - Real-world examples (coordinates, person data)

4. **Best Practices**:
   - Uses f-strings for formatting
   - Shows proper tuple syntax
   - Demonstrates correct empty set creation

To use this snippet:
1. Copy the entire code
2. Run it to see all the examples
3. Modify values and experiment with the types
4. Try the practice exercises at the bottom
