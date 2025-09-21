# Printing a message first
print("Welcome to Star Pattern Printing!\n")

rows = 5   # you can change the number of rows

# Printing a pyramid star pattern
print("Here is a Pyramid Pattern:\n")
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Printing a closing message
print("\nPattern printing completed successfully!")

print("Making a second commit")