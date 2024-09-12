import json
import requests


def load_data(file_path):
    """
    Loads a JSON file
    @rtype: object
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize an animal object to HTML
    @param animal_obj: Dict
    @return: String
    """
    output = '<li class="cards__item">'

    if 'name' in animal_obj and animal_obj['name']:
        output += f"<div class=\"card__title\">{animal_obj['name']}</div>"

    output += "<p class=\"card__text\">"
    if 'characteristics' in animal_obj:
        if 'diet' in animal_obj['characteristics'] and animal_obj['characteristics']['diet']:
            output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>"
        if 'type' in animal_obj['characteristics'] and animal_obj['characteristics']['type']:
            output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>"

    if 'locations' in animal_obj and animal_obj['locations']:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>"

    output += '</li>'

    return output


def serialize_animals(data):
    """ Prints all animals
    @param data: Dict
    @return: String
    """
    output = ''
    for animal_obj in data:
        animal_html = serialize_animal(animal_obj)
        output += animal_html

    return output


def generate_animals_html(template_path, data):
    """ Generates HTML content by replacing placeholder with animal info
    @param template_path: String
    @param data: Dict
    @return: String
    """
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    animal_info = serialize_animals(data)

    generated_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)

    return generated_html


def get_animal_data(name):
    """
    Retrieves animal data from the API-Ninjas endpoint
    @param name: String
    @return: Dict
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={name}"
    headers = {
        'X-Api-Key': 'HrahvM/EI8yih9CcACb4VQ==gfldZjQFdDlsr3bA'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None


def main():
    data = get_animal_data("Fox")
    new_html = generate_animals_html("animals_template.html", data)

    with open('animals.html', 'w') as output_file:
        output_file.write(new_html)


if __name__ == '__main__':
    main()
