import os

def create_alias(alias_name, file_path):
    """Creates an alias for the specified command."""
    shell_profile = os.path.expanduser('~/.bashrc')  # Adjust for your shell if necessary
    alias_changes_dir = os.path.join(os.path.expanduser('~'), '.alias_changes')
    os.makedirs(alias_changes_dir, exist_ok=True)

    alias_command = f"\nalias {alias_name}='/home/$USER/.alias_changes/{alias_name}_alias.sh'\n"
    
    with open(shell_profile, 'a') as file:
        file.write(alias_command)
    
    print(f"Added alias for {alias_name} to {shell_profile}.")

    # Create log file for alias changes
    log_file_path = os.path.join(alias_changes_dir, 'oem_before_alias_log')
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{alias_name}\t{os.path.join(alias_changes_dir, f'{alias_name}_alias.sh')}\n")

    # Determine the command to write in the alias script
    if alias_name.endswith('.py'):
        command = f"python3 {file_path} \"$@\""
    else:
        command = f"{file_path} \"$@\""
    
    # Create script for the alias
    script_file_path = os.path.join(alias_changes_dir, f"{alias_name}_alias.sh")
    with open(script_file_path, 'w') as script_file:
        script_file.write(f"""#!/bin/bash
# Execute {alias_name} with passed arguments
{command}
""")
    
    # Make the script executable
    os.chmod(script_file_path, 0o755)

    print(f"Alias script created: {script_file_path}")

    return alias_changes_dir, script_file_path


def main():
    alias_name = input("Enter the name for the alias: ")
    file_path = input("Enter the file path (including .py for Python scripts): ")
    
    alias_changes_dir, script_file_path = create_alias(alias_name, file_path)

    # Open default file explorer to the alias changes directory
    os.system(f"xdg-open {alias_changes_dir}")

    # Open the alias script in a text editor
    os.system(f"xed {script_file_path}")

    # Prompt the user to source their shell configuration file to apply the alias changes immediately
    print("Please run the following command to apply the alias changes immediately:")
    print("source ~/.bashrc")

if __name__ == "__main__":
    main()
