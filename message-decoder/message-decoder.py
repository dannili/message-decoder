import requests
from bs4 import BeautifulSoup
import pandas as pd

# A function to print a 2D grid with symbols at their assgined coordinates
def print_grid(url):
    symbol = ''
    x = 0
    y = 0
    df = get_data_from_url(url)
    df.iloc[1:, 0] = df.iloc[1:, 0].astype(int)
    df.iloc[1:, 2] = df.iloc[1:, 2].astype(int)
    counter = len(df)
    # Find the largest x and y to determin the size of the grid
    x_max = (df.iloc[1:, 0]).max()
    y_max = (df.iloc[1:, 2]).max()

    # Initialize the grid
    grid = [['' for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    # Put the symbol at the right position of the grid
    for i in range(1, counter):
        x = df.iloc[i][0]
        y = df.iloc[i][2]
        # set content to space if not specified
        if symbol is None:
            symbol = ' ' 
        else: symbol = df.iloc[i][1]

        grid[y][x] = symbol

    # Print the grid.
    # Reverse the order of rows because direction of y goes from bottom to top
    for row in reversed(grid):
        print(''.join(row))


# Helper function to get the datafram from a given url
def get_data_from_url(url):
    # Fetch the document
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table
    table = soup.find('table')  # Adjust if there are multiple tables or if a specific table is needed

    # Extract table rows
    rows = []
    for tr in table.find_all('tr'):
       cells = [td.get_text() for td in tr.find_all('td')]
       if cells:  # Avoid adding empty rows
          rows.append(cells)

    # Create the dataframe
    # Hardcode the headers since 
    HEADERS = ['x-coordinate', 'Character', 'y-coordinate']
    df = pd.DataFrame(rows, columns=HEADERS)

    # return the dataframe
    return df


# A Test url which print "F":
# DOCUMENT_URL = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
DOCUMENT_URL = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
print_grid(DOCUMENT_URL)
