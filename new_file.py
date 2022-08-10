import os


def foo():
    x = os.environ.get("Something", "Not fond")
    return 5
