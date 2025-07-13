def find_tallest_student():
    # Store student data as a dictionary: {name: height}
    students = {
        "John": 170,
        "Alice": 172,
        "Bob": 150
    }

    print("Sample Output:")
    # Print the student heights as shown in the example
    for name, height in students.items():
        print(f"• {name}: {height} cm")

    print("\nExpected output")

    tallest_student_name = ""
    max_height = -1  # Initialize with a value lower than any possible height

    # Iterate through the students to find the tallest
    for name, height in students.items():
        if height > max_height:
            max_height = height
            tallest_student_name = name

    print(f"• {tallest_student_name} is the tallest")

# Run the function
find_tallest_student()
