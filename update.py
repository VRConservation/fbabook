import os
import subprocess

# Save the original directory
orig_dir = os.getcwd()

# run the ghp-import -n -p -f _build/html
subprocess.run(["ghp-import", "-n", "-p", "-f", "_build/html"], check=True)

# Run the command jb build --all . after the loop
subprocess.run(["jb", "build", "--all", "."], check=True)

# Push and sync the repository to GitHub make sure to change the 'Update repo' message
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "New clean and build"], check=True)
subprocess.run(["git", "push"], check=True)

# Open local build in web browser
# Define the path to the intro.html file
file_path = r'file://D:\OneDrive\1_Consulting\CAL FIRE Biz Devo\CAL FIRE Biz Devo Shared\Communications\fbabook\_build\html\index.html'

# Define the command to open the file in Brave or Chrome
# For Brave
command_brave = f'start brave "{file_path}"'

# For Chrome
# command_chrome = f'start chrome "{file_path}"'

# Execute the command in Brave. Use command_chrome for Chrome
subprocess.run(command_brave, shell=True)  # Use command_chrome for Chrome
