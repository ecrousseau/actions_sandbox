import os

print("# Example Page\n")
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    print(f"# {dirpath}\n")
    for filename in filenames:
        if filename.endswith('.tf'):
            print(f"* **{filename}**\n")
        else:
            print(f"* {filename}\n")
    print("\n")