import os

print("# terraform-aws-ec2-instance\n")
print("## Files and Folders\n")
for (dirpath, dirnames, filenames) in os.walk(f"{os.getcwd()}/terraform-aws-ec2-instance"):
    print(f"### {dirpath}\n")
    for filename in filenames:
        if (not filename.startswith('.')) and filename.endswith('.tf'):
            print(f"* **{filename}**\n")
        elif not filename.startswith('.'):
            print(f"* {filename}\n")
    print("\n")
    _dirnames = []
    for dirname in dirnames:
        if not dirname.startswith('.'):
            _dirnames.append(dirname)
    dirnames = _dirnames