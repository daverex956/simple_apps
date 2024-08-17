import os
import subprocess

def list_scripts(directory):
    # List all Python scripts in the specified directory
    scripts = [f for f in os.listdir(directory) if f.endswith('.py')]
    if not scripts:
        print("No Python scripts found in the directory.")
        return []
    else:
        print("")
        print("--- Choose App --- ")
        for i, script in enumerate(scripts, 1):
            print(f"{i}. {script}")
        print("")
    return scripts

def choose_script(scripts):
    # Allow the user to choose a script by number
    while True:
        try:
            choice = int(input("Enter the number of the script you want to run: ")) - 1
            if 0 <= choice < len(scripts):
                return scripts[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def run_script(directory, script):
    # Run the chosen script
    script_path = os.path.join(directory, script)
    print(f"Running script: {script_path}")
    subprocess.run(['python3', script_path])

def main():
    # Get the directory where this script is located, and append 'apps' folder
    base_directory = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(base_directory, 'apps')

    if not os.path.isdir(directory):
        print("Invalid directory.")
        return
    
    scripts = list_scripts(directory)
    if scripts:
        chosen_script = choose_script(scripts)
        run_script(directory, chosen_script)

if __name__ == "__main__":
    main()
