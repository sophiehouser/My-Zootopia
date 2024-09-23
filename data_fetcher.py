import requests
from animals_web_generator import NEW_HTML_FILE


def fetch_data(animal_name):
    """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {
        'X-Api-Key': 'HrahvM/EI8yih9CcACb4VQ==gfldZjQFdDlsr3bA'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not data:
            print("Error: No animals found with the given name.")
            return []
        else:
            print(f"Website was successfully generated to the file {NEW_HTML_FILE}.")
            return data
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None
