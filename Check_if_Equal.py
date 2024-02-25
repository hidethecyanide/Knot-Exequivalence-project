# Dictionary of pre-defined objects and their definitions
predefined_objects = {
    'Unknot': ['[()]'],
    'Trefoil knot': ['[(4, 6, 2)]', '[(-4, -6, -2)]'],
    'Figure-eight knot': ['[(6, 8, 2, 4)]', '[(-6, -8, -2, -4)]', ],
    'Cinquefoil': ['[(6, 8, 10, 2, 4)]', '[(-6, -8, -10, -2, -4)]'],
    'Three-twist knot': ['[(6, 10, 8, 2, 4)]', '[(-6, -10, -8, -2, -4)]'],
    'Stevedore knot': ['[(8, 12, 10, 2, 6, 4)]', '[(-8, -12, -10, -2, -6, -4)]'],
    '6-2 knot': ['[(8, 10, 2, 12, 4, 6)]', '[(-8, -10, -2, -12, -4, -6)]'],
    '6-3 knot': ['[(8, 6, 12, 10, 2, 4)]', '[(-8, -6, -12, -10, -2, -4)]'],
}

# Open the text file in read mode
file_path = 'Downloads/your_text_file.txt'

try:
    with open(file_path, 'r') as file:
        # Read a line from the text file
        line_from_file = file.readline().strip()

        # Check if the line starts with #[ and remove the #
        if line_from_file.startswith('#['):
            line_from_file = line_from_file[1:]  # Remove the # at the beginning

            # Check if the line matches any pre-defined object
            for object_name, definitions in predefined_objects.items():
                if line_from_file == object_name:
                    print(f"Object: {object_name}")
                    for definition in definitions:
                        print(f"  - {definition}")
                    break
            else:
                print(f"The line '{line_from_file}' does not match any pre-defined object.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
