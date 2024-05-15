# Alias Creation Script
>>>>>>> mainly for lazy personal use

## Description

This script facilitates the creation of command aliases. It prompts the user for an alias name and the file path of the script or command to be aliased. If the alias name ends with `.py`, it prepends `python3` to the command. The script ensures that the alias is added to the shell configuration file (`.bashrc`) and creates a corresponding alias script in the `.alias_changes` directory. It logs all alias changes and opens the created alias script in a text editor for further modifications.

The script performs the following tasks:
- Creates the `/home/$USER/.alias_changes` directory if it doesn't already exist.
- Appends the alias to the `.bashrc` file.
- Logs the alias changes in `oem_before_alias_log`.
- Creates an alias script in the `.alias_changes` directory.
- Opens the alias script in the default text editor (`xed`).

## Examples

### ***Example 1: Creating an Alias for a Python Script***

```
# Run the script
python3 path/to/this_script.py

# Enter the alias name and file path when prompted
Enter the name for the alias: testthis.py
Enter the file path (including .py for Python scripts): /home/whonow/python_testing/testthis.py

# Apply the alias changes
source ~/.bashrc

# Now you can run the alias directly
testthis.py
```
### ***Example 2: Creating an Alias for a Shell Command***
```
# Run the script
python3 path/to/this_script.py

# Enter the alias name and file path when prompted
Enter the name for the alias: mycommand
Enter the file path (including .py for Python scripts): /home/whonow/scripts/mycommand.sh

# Apply the alias changes
source ~/.bashrc

# Now you can run the alias directly
mycommand
```
### ***Example 3: Creating an Alias for a Custom Script***
```
# Run the script
python3 path/to/this_script.py

# Enter the alias name and file path when prompted
Enter the name for the alias: runscript
Enter the file path (including .py for Python scripts): /home/whonow/custom/runscript

# Apply the alias changes
source ~/.bashrc

# Now you can run the alias directly
runscript

```

### Future Improvements

- Future versions of this script will include the ability to select and delete no longer desired aliases, providing a more comprehensive alias management system.
