# Dictionary of pre-defined objects and their definitions
predefined_objects = {
    'Unknot': ['[()]'],
    'Trefoil knot': ['[(4, 6, 2)]', '[(-4, -6, -2)]'],
    'Figure-eight knot': ['[(6, 8, 2, 4)]', '[(-6, -8, -2, -4)]'],
    'Cinquefoil knot': ['[(6, 8, 10, 2, 4)]', '[(-6, -8, -10, -2, -4)]'],
    'Three-twist knot': ['[(6, 10, 8, 2, 4)]', '[(-6, -10, -8, -2, -4)]'],
    'Stevedore knot': ['[(8, 12, 10, 2, 6, 4)]', '[(-8, -12, -10, -2, -6, -4)]'],
    '6-2 knot': ['[(8, 10, 2, 12, 4, 6)]', '[(-8, -10, -2, -12, -4, -6)]'],
    '6-3 knot': ['[(8, 6, 12, 10, 2, 4)]', '[(-8, -6, -12, -10, -2, -4)]'],
}

# Open the text file in read mode
file_path = "C:\\Users\\User\\Downloads\\myManifold.py"

try:
    with open(file_path, 'r') as file:
        # Read all lines from the text file
        all_lines = file.readlines()

        # Check each line for pre-defined objects
        for line_number, line_from_file in enumerate(all_lines, start=1):
            line_from_file = line_from_file.strip()

            # Check if the line matches any pre-defined object
            for object_name, definitions in predefined_objects.items():
                for definition in definitions:
                    if definition in line_from_file:
                        print(f"your knot is a {object_name}")
                        print()  # Add a blank line for better readability
                        break

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
