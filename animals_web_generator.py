import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animals(data):
    """ Prints all animals """
    for animal_data in data:
        if 'name' in animal_data and animal_data['name']:
            print(f"Name: {animal_data['name']}")

        if 'characteristics' in animal_data:
            if 'diet' in animal_data['characteristics'] and animal_data['characteristics']['diet']:
                print(f"Diet: {animal_data['characteristics']['diet']}")
            if 'type' in animal_data['characteristics'] and animal_data['characteristics']['type']:
                print(f"Type: {animal_data['characteristics']['type']}")

        if 'locations' in animal_data and animal_data['locations']:
            print(f"Location: {animal_data['locations'][0]}")

        print()


def main():
    data = load_data('animals_data.json')
    print_animals(data)


if __name__ == '__main__':
    main()
