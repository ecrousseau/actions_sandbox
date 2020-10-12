import os

print("# terraform-aws-ec2-instance\n")
print("## Files and Folders\n")
for (dirpath, dirnames, filenames) in os.walk(f"{os.getcwd()}/terraform-aws-ec2-instance"):
    dirnames[:] = [d for d in dirnames if not d.split('/')[-1].startswith('.')]
    print(f"### {dirpath}\n")
    for f in filenames:
        if (not f.startswith('.')) and f.endswith('.tf'):
            print(f"* **{f}**\n")
        elif not f.startswith('.'):
            print(f"* {f}\n")
    print("\n")