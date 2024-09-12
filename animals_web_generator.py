import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_info(data):
    """ Prints all animals """
    output = ''
    for animal_data in data:
        output += '<li class="cards__item">'

        if 'name' in animal_data and animal_data['name']:
            output += f"<div class=\"card__title\">{animal_data['name']}</div>"

        output += "<p class=\"card__text\">"
        if 'characteristics' in animal_data:
            if 'diet' in animal_data['characteristics'] and animal_data['characteristics']['diet']:
                output += f"<strong>Diet:</strong> {animal_data['characteristics']['diet']}<br/>"
            if 'type' in animal_data['characteristics'] and animal_data['characteristics']['type']:
                output += f"<strong>Type:</strong> {animal_data['characteristics']['type']}<br/>"

        if 'locations' in animal_data and animal_data['locations']:
            output += f"<strong>Location:</strong> {animal_data['locations'][0]}<br/>"

        output += '</li>'

    return output


def generate_animals_html(template_path, data):
    """ Generates HTML content by replacing placeholder with animal info """
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    animal_info = get_animal_info(data)

    generated_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)

    return generated_html


def main():
    data = load_data('animals_data.json')
    new_html = generate_animals_html("animals_template.html", data)

    with open('animals.html', 'w') as output_file:
        output_file.write(new_html)


if __name__ == '__main__':
    main()
