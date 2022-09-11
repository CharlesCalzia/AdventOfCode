import os

def read(dayn):
    file = os.path.dirname(os.path.realpath(__file__)) + f"\\day{dayn}.txt"
    with open(file, "r") as f:
        return f.read().strip()