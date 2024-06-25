import requests
import csv
import pandas as pd

# URL of the SWAPI people endpoint
url = 'https://swapi.dev/api/people/'

# List to store the data
people_data = []

# Pagination
while url:
    # Make the API request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the data in JSON format
        data = response.json()
        people = data['results']
        
        for person in people:
            name = person['name']
            height = person['height']
            mass = person['mass']
            hair_color = person['hair_color']
            skin_color = person['skin_color']
            eye_color = person['eye_color']
            birth_year = person['birth_year']
            gender = person['gender']
            people_data.append([name, height, mass, hair_color, skin_color, eye_color, birth_year, gender])
        
        # Update the URL to the next page
        url = data['next']
    else:
        print(f'Request error: {response.status_code}')
        break

# Save the data to a CSV file
with open('swapi_people.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Height', 'Mass', 'Hair Color', 'Skin Color', 'Eye Color', 'Birth Year', 'Gender'])
    writer.writerows(people_data)

print('Data collected and saved in swapi_people.csv')


# Read the CSV file
df = pd.read_csv('swapi_people.csv')

# Show the first 5 characters
print(df.head())

# Count the number of characters collected
print(f'Total characters collected: {len(df)}')