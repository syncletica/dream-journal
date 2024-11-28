"""
Bonita McBride
CS 521 - Fall 1
October 12, 2024
Final Project - Dream Log
"""

from dream import Dream

def add_dream():
    date = input("Enter the date of the dream (YYYY-MM-DD): ")
    description = input("Enter the description of the dream: ")
    
    while True:
        dream_types_input = input(f"Enter the types of the dream, separated by \
                                  commas ({', '.join(Dream.VALID_TYPES)}): ")
        dream_types = [t.strip().capitalize() for t in dream_types_input.split(",")]
        try:
            new_dream = Dream(date, description, dream_types)  
            save_dream_to_file(new_dream)  
            break  
        except ValueError as e:
            print(e)  


# req: input/output file
def save_dream_to_file(dream, filename="dreams.txt"):
    with open(filename, 'a') as file:
        types_str = ','.join(dream.types)  
        file.write(f"{dream._date}|{types_str}|{dream._description}\n\n\n")
    print(f"Dream saved to {filename}")

def load_dreams_from_file(filename="dreams.txt"):
    # req: list container
    # req: try block with else conidition
    dreams = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines in dream.txt file        
                try:
                    date, types_str, description = line.split('|')
                    types = [t.strip() for t in types_str.split(',')]
                    dreams.append(Dream(date, description, types))  
                except ValueError:
                    print(f"Skipping malformed line: {line}")
                    continue
    except FileNotFoundError:
        print(f"{filename} not found. No dreams loaded.")
    else:
        print(f"Dreams loaded from {filename}")
    return dreams


def show_dreams_by_type(dreams):
    # req: dict container
    # user picks dream types so they can view all dreams with that type
    dreams_by_type = {}
    for dream in dreams:
        for dream_type in dream.types:
            if dream_type not in dreams_by_type:
                dreams_by_type[dream_type] = []
            dreams_by_type[dream_type].append(dream)

    # req: user defined function
    dream_type = input(f"Enter the type of dream to display \
                       ({', '.join(Dream.VALID_TYPES)}): ").strip().capitalize()
    
    if dream_type in dreams_by_type:
        print(f"\nDreams categorized as '{dream_type}':")
        for dream in dreams_by_type[dream_type]:
            print(dream)
            print()  
            
    else:
        print(f"No dreams found with the type '{dream_type}'.")

            
def search_dreams_by_keyword(dreams):
    # req: user defined function
    keyword = input("Enter keyword to search for: ").strip().lower()
    
    matches = [dream for dream in dreams if keyword in dream]
    
    if matches:
        print(f"Dreams containing keyword '{keyword}':")
        for dream in matches:
            print(dream)
            print()
    else:
        print(f"No dreams found containing keyword '{keyword}'.")
        
#USER MENUS:

def analyze_dreams():
    dreams = load_dreams_from_file()
    
    if not dreams:
        print("No dreams available to analyze.")
        return

    # analysis menu
    # req: while loop
    while True:
        print("\nAnalysis Options:")
        print("1. Search dreams by keyword")
        print("2. Show dreams by type")
        print("3. Return to main menu")
        
        choice = input("Choose an option (1-3): ")
        
        # req: if conditional
        if choice == '1':
            search_dreams_by_keyword(dreams) 
        elif choice == '2':
            show_dreams_by_type(dreams)
        elif choice == '3':
            break  
        else:
            print("Invalid choice, please try again.")


# main menu
def main():
    while True:
        print("\nDream Log Menu:")
        print("1. Add a new dream")
        print("2. Analyze dreams")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_dream()
        elif choice == '2':
            analyze_dreams()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()