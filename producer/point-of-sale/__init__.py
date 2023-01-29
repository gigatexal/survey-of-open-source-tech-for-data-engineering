import sys
import pathlib

paths = sys.path

current_path = pathlib.Path(".")

folders_to_import = [f.resolve() for f in current_path.glob("*") if f.is_dir()] 

for folder in folders_to_import:
    paths.append(str(folder))

