import hashlib
import json
import os

HASH_FILE = "hashes.json"

# Function to generate SHA-256 hash
def generate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


# Load saved hashes
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as file:
        hashes = json.load(file)
else:
    hashes = {}

# Ask user for file
file_path = input("Enter the file path: ")

# Check if file exists
if not os.path.exists(file_path):
    print("❌ File not found.")
    exit()

# Generate current hash
current_hash = generate_hash(file_path)

# First time checking the file
if file_path not in hashes:
    hashes[file_path] = current_hash

    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

    print("✅ File hash saved successfully.")

# Compare with saved hash
else:
    if hashes[file_path] == current_hash:
        print("✅ File is unchanged.")
    else:
        print("❌ Warning! The file has been modified.")

        # Update the saved hash
        hashes[file_path] = current_hash

        with open(HASH_FILE, "w") as file:
            json.dump(hashes, file, indent=4)

        print("✅ New hash has been saved.")