import os
from pathlib import Path

def rename_files(folder, prefix="file"):
    p = Path(folder)
    files = [f for f in p.iterdir() if f.is_file()]
    for i, f in enumerate(files, start=1):
        new = f.parent / f"{prefix}_{i}{f.suffix}"
        f.rename(new)
    return len(files)

if __name__ == "__main__":
    folder = input("Folder path: ").strip() or "."
    count = rename_files(folder, prefix="renamed")
    print(f"Renamed {count} files")