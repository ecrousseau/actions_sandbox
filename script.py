import os

print("# terraform-aws-ec2-instance\n")
print("## Files and Folders\n")
for (dirpath, dirnames, filenames) in os.walk(f"{os.getcwd()}/terraform-aws-ec2-instance"):
    print(f"### {dirpath}\n")
    for filename in filenames:
        if filename.endswith('.tf'):
            print(f"* **{filename}**\n")
        else:
            print(f"* {filename}\n")
    print("\n")