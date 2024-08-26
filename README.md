# message-decoder
Access data from a url and decode the message. The url contains a table with three columns: x-coordinate, y-coordinate, and a symbol character.

## Requirements:
`pip install requests beautifulsoup4 pandas`

## A sample test:
`DOCUMENT_URL = https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub`

`print_grid(DOCUMENT_URL)`

Letter 'F' should be printed
