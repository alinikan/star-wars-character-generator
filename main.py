import random
import json

WEAPONS = ('lightsaber', 'bowcaster', 'blaster pistol', 'electrostaff', 'flamethrower', 'vibroblade', 'force pike',
           'thermal detonator')


def load_data(file):
    """ Load the Star Wars data from a JSON file."""
    try:
        with open(file, 'r') as f:
            # Tries to load JSON data from the specified file
            data = json.load(f)
        print('Data loaded successfully.')
        return data
    except FileNotFoundError:
        print(f"Could not find file {file}. Did you run api_scrape.py?")
        return None


def choose_random_item(database, category):
    """ Choose a random item from a database category """
    # Chooses a random item from the specified category in the database
    return random.choice(database[category])


def build_character(database, name):
    """ Return a Star Wars character sheet."""
    if not database:
        return

    # Chooses random values from different categories in the database
    species = choose_random_item(database, 'species')
    planet = choose_random_item(database, 'planets')
    starship = choose_random_item(database, 'starships')
    weapon = random.choice(WEAPONS) # Chooses a random weapon from the predefined list of weapons
    character_info = choose_random_item(database, 'characters')

    # Constructs the character sheet string
    character = f"""
    =====================
    Name: {name}
    Height: {character_info['height']} cm
    Weight: {character_info['mass']} kg
    Species: {species}
    Home Planet: {planet}
    Starship: {starship}
    Weapon of Choice: {weapon}
    =====================
    """
    return character


def main():
    print("Welcome to the Star Wars Character Generator!")
    # Loads data from the JSON file created by api_scrape.py
    database = load_data('sw_database.json')
    while True:
        # Prompts the user for a name input until the user inputs 'quit'
        name = input("\nEnter a name for your character (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break
        # Builds and prints a Star Wars character using the user's input name
        print(build_character(database, name))


if __name__ == "__main__":
    main()
