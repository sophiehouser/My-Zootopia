import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


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
        'X-Api-Key': API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not data:
            print(f"Error: No animals found with the given name: {animal_name}.")
            return []
        else:
            return data
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None
