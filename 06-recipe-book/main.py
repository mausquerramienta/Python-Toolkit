# Recipe Book

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent / "recipes"
BASE_DIR.mkdir(exist_ok=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def count_recipes(path):
    return len(list(Path(path).glob("**/*.txt")))

def choose_action():
    while True:
        print("\n" + "=" * 40)
        print("Recipe book menu:")
        print("=" * 40)
        print("1. Read a recipe")
        print("2. Create a new recipe")
        print("3. Create a new category")
        print("4. Delete a recipe")
        print("5. Delete a category")
        print("6. Exit program")
        print("-" * 40)
        
        choice = input("Select an option (1-6): ")
        if choice.isnumeric() and int(choice) in range(1, 7):
            return int(choice)
        print("Invalid option. Please enter a number between 1 and 6.")

def list_categories(path):
    categories = [n.name for n in Path(path).iterdir() if n.is_dir()]
    print(f"Total Categories: {len(categories)}")
    if categories:
        print("-" * 20)
        for i, name in enumerate(categories, 1):
            print(f"[{i}] {name}")
    return categories

def choose_category(path, categories):
    while True:
        choice = input("Select a category number: ")
        if choice.isnumeric() and int(choice) in range(1, len(categories) + 1):
            return path / categories[int(choice) - 1]
        print("Invalid option. Please choose a valid category number.")

def list_recipes(path):
    recipes = [n.stem for n in Path(path).glob("*.txt")]
    print(f"Total Recipes: {len(recipes)}")
    if recipes:
        print("-" * 20)
        for i, name in enumerate(recipes, 1):
            print(f"[{i}] {name}")
    return recipes

def choose_recipe(path, recipes):
    while True:
        choice = input("Select a recipe number: ")
        if choice.isnumeric() and int(choice) in range(1, len(recipes) + 1):
            return path / f"{recipes[int(choice) - 1]}.txt"
        print("Invalid option. Please choose a valid recipe number.")

def read_recipe(path):
    print("\n" + "=" * 50)
    print(path.read_text(encoding="utf-8"))
    print("=" * 50)

def create_recipe(path):
    while True:
        recipe_name = input("Name of the new recipe: ")
        file_path = path / f"{recipe_name}.txt" 
        if file_path.exists():
            print("A recipe with that name already exists. Choose a different one.")
        else:
            break
            
    print("Write the recipe instructions (Press Enter when done):")
    content = input("> ")
    file_path.write_text(content, encoding="utf-8")
    print(f"Recipe '{recipe_name}' successfully created!")

def create_category(path):
    new_category = input("Name of the new category: ")
    new_path = path / new_category
    new_path.mkdir(exist_ok=True)
    print(f"Category '{new_category}' successfully created!")

def delete_recipe(path, recipes):
    while True:
        choice = input("Select the recipe number to delete: ")
        if choice.isnumeric() and int(choice) in range(1, len(recipes) + 1):
            target_recipe = recipes[int(choice) - 1]
            file_path = path / f"{target_recipe}.txt"
            file_path.unlink()
            print(f"Recipe '{target_recipe}' successfully deleted!")
            break
        print("Invalid option.")

def delete_category(path, categories):
    while True:
        choice = input("Select the category number to delete: ")
        if choice.isnumeric() and int(choice) in range(1, len(categories) + 1):
            target_category = categories[int(choice) - 1]
            dir_path = path / target_category            
            if any(dir_path.iterdir()):
                print("⚠️ Cannot delete a category that contains recipes. Delete the recipes first.")
            else:
                dir_path.rmdir()
                print(f"Category '{target_category}' successfully deleted!")
            break
        print("Invalid option.")

def start_program(base_path):
    clear_screen()
    print(f"Welcome to the Digital Recipe Book!")
    
    while True:
        print(f"System Status: {count_recipes(base_path)} recipes saved.")
        action = choose_action()
        match action:
            case 1:
                clear_screen()
                categories = list_categories(base_path)
                if categories:
                    category_path = choose_category(base_path, categories)
                    clear_screen()
                    recipes = list_recipes(category_path)
                    if recipes:
                        recipe_path = choose_recipe(category_path, recipes)
                        clear_screen()
                        read_recipe(recipe_path)
                    else:
                        print("No recipes found in this category.")
                else:
                    print("No categories available.")
                    
            case 2:
                clear_screen()
                categories = list_categories(base_path)
                if categories:
                    category_path = choose_category(base_path, categories)
                    clear_screen()
                    create_recipe(category_path)
                else:
                    print("You must create a category first before adding a recipe.")
                    
            case 3:
                clear_screen()
                create_category(base_path)
                
            case 4:
                clear_screen()
                categories = list_categories(base_path)
                if categories:
                    category_path = choose_category(base_path, categories)
                    clear_screen()
                    recipes = list_recipes(category_path)
                    if recipes:
                        delete_recipe(category_path, recipes)
                    else:
                        print("No recipes available to delete in this category.")
                else:
                    print("No categories available.")
                    
            case 5:
                clear_screen()
                categories = list_categories(base_path)
                if categories:
                    delete_category(base_path, categories)
                else:
                    print("No categories available to delete.")
                    
            case 6:
                clear_screen()
                print("=" * 40)
                print("Thank you for using the Recipe Book!")
                print("=" * 40)
                break
                
        input("\nPress ENTER to continue...")
        clear_screen()

start_program(BASE_DIR)
