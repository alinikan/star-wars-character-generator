import json
import requests


def get_resource_page(resource, page):
    """ Get a single page from the resource. """
    # Requests the API data for a specific resource and page number.
    response = requests.get(f"https://swapi.dev/api/{resource}/?page={page}")
    # If the status code is 200, meaning the request was successful, return the JSON data.
    if response.status_code == 200:
        return response.json()


def API_scrape(resource, property=None):
    """ Call the SWAPI and create a list of data. """
    data_list = []
    page = 1
    while True:
        # Calls the function get_resource_page to get data
        data = get_resource_page(resource, page)
        if data is None:
            break
        else:
            # Appends the results to data_list
            filtered_data = data["results"]
            for item in filtered_data:
                # If a property is specified, appends only the property value of each item, else appends the whole item.
                data_list.append(item if not property else item[f'{property}'])
        # Increments the page number
        page += 1

    print(f'Successfully fetched {len(data_list)} {resource}.')
    return data_list


def main():
    database = {}
    # Calls API_scrape for each Star Wars category and adds them to database dictionary
    database['starships'] = API_scrape('starships', 'model')
    database['planets'] = API_scrape('planets', 'name')
    database['species'] = API_scrape('species', 'name')
    database['characters'] = API_scrape('people')

    file = 'sw_database.json'
    with open(file, 'w') as f:
        # Dumps the database dictionary into a JSON file
        json.dump(database, f)

    print('Database saved successfully.')


if __name__ == "__main__":
    main()
