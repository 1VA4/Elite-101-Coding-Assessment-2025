# Define the tables and their availability status
tables = {1: "Free", 2: "Reserved", 3: "Free", 4: "Free"}

# Function to get a list of free tables
def get_free_tables(tables):
    return [table for table, status in tables.items() if status == "Free"]

# LEVEL 1: Print all free tables
def level1(tables):
    free_tables = get_free_tables(tables)
    print(f"LEVEL 1: Free Tables = {free_tables}")

# LEVEL 2: Find one free table for a party of 2
def level2(tables):
    free_tables = get_free_tables(tables)
    if free_tables:  # Check if there is at least one free table
        print(f"LEVEL 2: One table for party size 2 = {free_tables[0]}")  # Pick the first available table

# LEVEL 3: List all tables that can fit 2 people
def level3(tables):
    free_tables = get_free_tables(tables)
    print(f"LEVEL 3: All tables for party size 2 = {free_tables}")

# LEVEL 4: Find single or combined tables for a party of 5
def level4(tables):
    free_tables = get_free_tables(tables)
    possible_combos = []

    # Check if tables 3 and 4 are free, and if so, combine them
    if 3 in free_tables and 4 in free_tables:
        possible_combos.append((3, 4))

    # Check if table 4 alone is a good option
    if 4 in free_tables:
        possible_combos.append((4,))

    print(f"LEVEL 4: Single or combined tables for party size 5 = {possible_combos}")

# BONUS: Print a more user-friendly output
def bonus_friendly_output(tables):
    free_tables = get_free_tables(tables)
    
    # If tables 3 and 4 are free, they can be combined for a larger party
    if 3 in free_tables and 4 in free_tables:
        print(f"Tables 3 and 4 together can seat 8 people.")

    # If table 4 is free by itself, print its capacity
    if 4 in free_tables:
        print(f"Table 4 is free and can seat 6 people.")

# Main function to run everything
def main():
    # Print all levels step by step
    level1(tables)
    level2(tables)
    level3(tables)
    level4(tables)

    # Add a space before the bonus output for better readability
    print("\nBONUS: Friendly output for the combos above")
    bonus_friendly_output(tables)

# Run the program
main()
