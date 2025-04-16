import os

def get_files():
    """Return a space-separated string of filenames (without .py extension) in the current directory"""
    base_dir = os.path.dirname(__file__)
    return "\n".join(
        os.path.splitext(f)[0]  # remove .py
        for f in os.listdir(base_dir)
        if f.endswith(".py") and os.path.isfile(os.path.join(base_dir, f)) and f != "files.py"
    )
