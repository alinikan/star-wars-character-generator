import json
import requests


def get_resource_page(resource, page):
    """ Get a single page from the resource. """
    response = requests.get(f"https://swapi.dev/api/{resource}/?page={page}")
    if response.status_code == 200:
        return response.json()


def API_scrape(resource, property=None):
    """ Call the SWAPI and create a list of data. """
    data_list = []
    page = 1
    while True:
        data = get_resource_page(resource, page)
        if data is None:
            break
        else:
            filtered_data = data["results"]
            for item in filtered_data:
                data_list.append(item if not property else item[f'{property}'])
        page += 1

    print(f'Successfully fetched {len(data_list)} {resource}.')
    return data_list


def main():
    database = {}
    database['starships'] = API_scrape('starships', 'model')
    database['planets'] = API_scrape('planets', 'name')
    database['species'] = API_scrape('species', 'name')
    database['characters'] = API_scrape('people')

    file = 'sw_database.json'
    with open(file, 'w') as f:
        json.dump(database, f)

    print('Database saved successfully.')


if __name__ == "__main__":
    main()
