import os
import subprocess

# Save the original directory
orig_dir = os.getcwd()

# run the ghp-import -n -p -f _build/html
subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"], check=True)

# Run the command jb build --all . after the loop
subprocess.run(["jb", "build", "--all", "."], check=True)

# Push and sync the repository to GitHub
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Update the repository"])
subprocess.run(["git", "push"])
