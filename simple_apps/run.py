import os
import subprocess

def list_categories(directory):
    # List all subfolders (categories) in the specified directory, excluding __pycache__
    categories = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f)) and f != '__pycache__']
    
    if not categories:
        print("No categories found in the directory.")
        return []
    else:
        print("")
        print("--- Choose Category ---")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        print(f"{len(categories) + 1}. Exit")
        print("")
    return categories

def list_scripts(directory, category):
    # List all Python scripts in the specified category
    category_path = os.path.join(directory, category)
    scripts = [f for f in os.listdir(category_path) if f.endswith('.py')]

    if not scripts:
        print(f"No Python scripts found in the {category} category.")
        return []
    else:
        print("")
        print(f"--- Choose App in {category} ---")
        for i, script in enumerate(scripts, 1):
            script_name = script.replace('.py', '')  # Remove the .py extension
            print(f"{i}. {script_name}")
        print(f"{len(scripts) + 1}. Exit")
        print("")
    return scripts

def choose_option(options, prompt):
    # Generic function to choose an option from a list
    while True:
        try:
            choice = int(input(prompt)) - 1
            if choice == len(options):  # Option to exit
                return None
            elif 0 <= choice < len(options):
                return options[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def run_script(directory, category, script):
    # Run the chosen script
    script_path = os.path.join(directory, category, script)
    print(f"Running script: {script_path}")
    subprocess.run(['python3', script_path])

def main():
    # Get the directory where this script is located, and append 'apps' folder
    base_directory = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(base_directory, 'apps')

    if not os.path.isdir(directory):
        print("Invalid directory.")
        return
    
    while True:
        # Step 1: List categories (subfolders), excluding __pycache__
        categories = list_categories(directory)
        if not categories:
            return

        chosen_category = choose_option(categories, "Enter the number of the category you want to choose (or Exit): ")
        if chosen_category is None:
            print("Exiting...")
            break

        # Step 2: List scripts in the chosen category
        scripts = list_scripts(directory, chosen_category)
        if not scripts:
            return

        chosen_script = choose_option(scripts, "Enter the number of the script you want to run (or Exit): ")
        if chosen_script is None:
            print("Exiting...")
            break
        
        run_script(directory, chosen_category, chosen_script)

if __name__ == "__main__":
    main()
