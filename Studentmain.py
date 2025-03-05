def get_free_tables(tables):
    return [table for table, status in tables.items() if status == "Free"]

def level1(tables):
    free_tables = get_free_tables(tables)
    print(f"LEVEL 1: Free Tables = {free_tables}")

def level2(tables):
    free_tables = get_free_tables(tables)
    if free_tables:
        print(f"LEVEL 2: One table for party size 2 = {free_tables[0]}")

def level3(tables):
    free_tables = get_free_tables(tables)
    print(f"LEVEL 3: All tables for party size 2 = {free_tables}")

def level4(tables):
    free_tables = get_free_tables(tables)
    possible_combos = []

    if 3 in free_tables and 4 in free_tables:
        possible_combos.append((3, 4))
    if 4 in free_tables:
        possible_combos.append((4,))

    print(f"LEVEL 4: Single or combined tables for party size 5 = {possible_combos}")

def bonus_output(tables):
    free_tables = get_free_tables(tables)
    
    if 3 in free_tables and 4 in free_tables:
        print(f"Tables 3 and 4 together can seat 8 people.")
    
    if 4 in free_tables:
        print(f"Table 4 is free and can seat 6 people.")

def main():
    tables = {1: "Free", 2: "Reserved", 3: "Free", 4: "Free"}
    
    level1(tables)
    level2(tables)
    level3(tables)
    level4(tables)
    print("\nBONUS: Friendly output for the combos above")
    bonus_output(tables)

main()
