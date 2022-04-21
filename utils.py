def read(file_name="today.txt"):
    with open("today.txt", "r") as f:
        return f.read().strip()