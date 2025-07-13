def sort_list_of_dicts(list_of_dicts, key_to_sort_by, reverse=False):
    """
    Sorts a list of dictionaries by the value of a specified key.

    Args:
        list_of_dicts: A list of dictionaries.
        key_to_sort_by: The key whose values will be used for sorting.
        reverse: If True, sort in descending order. Defaults to False (ascending).

    Returns:
        A new list of dictionaries, sorted as specified.
    """
    
    return sorted(list_of_dicts, key=lambda person: person[key_to_sort_by], reverse=reverse)


print("\n--- Sort List of Dictionaries ---")
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 24, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"},
    {"name": "David", "age": 24, "city": "Berlin"}
]

print("Original list:")
for p in people:
    print(p)

print("\nSorted by 'age' (ascending):")
sorted_by_age = sort_list_of_dicts(people, 'age')
for p in sorted_by_age:
    print(p)
 Bob, David (tie-break by original order or stable sort), Alice, Charlie

print("\nSorted by 'age' (descending):")
sorted_by_age_desc = sort_list_of_dicts(people, 'age', reverse=True)
for p in sorted_by_age_desc:
    print(p)


print("\nSorted by 'name' (ascending):")
sorted_by_name = sort_list_of_dicts(people, 'name')
for p in sorted_by_name:
    print(p)
# Expected: Alice, Bob, Charlie, David
