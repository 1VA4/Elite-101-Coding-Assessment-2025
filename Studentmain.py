# Import the restaurant table layout from the restaurant_tables.py file
from restaurantTables import restaurant_tables  # Assuming restaurant_tables.py exists in the same directory

# Function for Level 1: List all free tables
def get_free_tables(tables, timeslot):
    """
    Returns a list of table IDs that are currently free at the given timeslot.
    """
    free_tables = []
    for col in range(1, len(tables[0])):
        if tables[timeslot][col] == 'o':
            free_tables.append(tables[0][col])
    return free_tables

# Function for Level 2: Find one table for the party size
def find_one_table_for_size(tables, party_size, timeslot):
    """
    Returns the first table that can seat the party_size and is free during the given timeslot.
    """
    for col in range(1, len(tables[0])):
        table_info = tables[0][col]
        capacity = int(table_info.split('(')[1].split(')')[0])
        if tables[timeslot][col] == 'o' and capacity >= party_size:
            return tables[0][col]
    return None

# Function for Level 3: Find all tables for the party size
def find_all_tables_for_size(tables, party_size, timeslot):
    """
    Returns a list of all table IDs that can seat the party_size and are free during the given timeslot.
    """
    suitable_tables = []
    for col in range(1, len(tables[0])):
        table_info = tables[0][col]
        capacity = int(table_info.split('(')[1].split(')')[0])
        if tables[timeslot][col] == 'o' and capacity >= party_size:
            suitable_tables.append(tables[0][col])
    return suitable_tables

# Function for Level 4: Find tables that can accommodate the party size, including combinations of adjacent tables
def find_tables_including_combos(tables, party_size, timeslot):
    """
    Returns a list of single or combined adjacent tables that can seat the party_size during the given timeslot.
    """
    results = []

    for col in range(1, len(tables[0])):
        table_info = tables[0][col]
        capacity = int(table_info.split('(')[1].split(')')[0])
        # Check if this single table fits
        if tables[timeslot][col] == 'o' and capacity >= party_size:
            results.append((tables[0][col],))

        # Check adjacent tables for combo seating
        if col + 1 < len(tables[0]):
            next_capacity = int(tables[0][col + 1].split('(')[1].split(')')[0])
            if tables[timeslot][col] == 'o' and tables[timeslot][col + 1] == 'o' and (capacity + next_capacity) >= party_size:
                results.append((tables[0][col], tables[0][col + 1]))

    return results

# Bonus: Friendly output for level 4 combinations
def friendly_output(tables, combos):
    """
    Prints a user-friendly message for each combination of tables found in level 4.
    """
    for group in combos:
        if len(group) == 1:
            print(f"Table {group[0]} is free and can seat {int(group[0].split('(')[1].split(')')[0])} people.")
        else:
            total_capacity = sum([int(table.split('(')[1].split(')')[0]) for table in group])
            print(f"Tables {', '.join(group)} together can seat {total_capacity} people.")

# Example usage/testing
if __name__ == "__main__":
    # Test timeslot 1 (second row, index 1)
    timeslot = 1

    # Level 1: Get all free tables at timeslot 1
    free_tables = get_free_tables(restaurant_tables, timeslot)
    print(f"Level 1: Free tables at timeslot {timeslot}: {free_tables}")

    # Level 2: Find one table for a party of size 2 at timeslot 1
    one_table = find_one_table_for_size(restaurant_tables, 2, timeslot)
    print(f"Level 2: One table for party size 2 at timeslot {timeslot}: {one_table}")

    # Level 3: Find all tables for a party of size 2 at timeslot 1
    all_tables = find_all_tables_for_size(restaurant_tables, 2, timeslot)
    print(f"Level 3: All tables for party size 2 at timeslot {timeslot}: {all_tables}")

    # Level 4: Find tables that can accommodate a party size of 5 at timeslot 1
    combos = find_tables_including_combos(restaurant_tables, 5, timeslot)
    print(f"Level 4: Tables or combos for party size 5 at timeslot {timeslot}: {combos}")

    # Bonus: Friendly output for combos found in level 4
    print("\nBonus: Friendly output for level 4 combos:")
    friendly_output(restaurant_tables, combos)
