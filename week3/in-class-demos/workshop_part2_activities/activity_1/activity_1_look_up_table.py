# We sometimes want to use nested loops to create multidimensional structures
# Now using dictionaries to associate each product code
# with a tuple containing the product name and its price.

# Define a function that creates the product lookup dictionary
def build_catalogue(product_code_grid, product_data_grid):
    # TODO: Initialise an empty dictionary to store the catalogue
    catalogue = {}
    # TODO: Iterate over the outer keys (e.g., rows or categories)
    for category in product_code_grid:
        # TODO: Iterate over the inner keys (e.g., individual product codes)
        for key, value in product_code_grid[category].items():
            # TODO: Retrieve the product code
            product_code = value
            # TODO: Use the corresponding product data as the value
            value = product_data_grid[category][key]
            # TODO: Add the code-data pair to the catalog
            catalogue[product_code] = value
    # Return the completed catalog
    return catalogue

# Define the product code grid as a dictionary of dictionaries
product_code_grid = {
    'row1': {
        'col1': 'P1001',
        'col2': 'P1002'
    },
    'row2': {
        'col1': 'P1003',
        'col2': 'P1004'
    }
}

# Define the product data grid (names and prices) as a matching structure
product_data_grid = {
    'row1': {
        'col1': ('Apple', 1.20),
        'col2': ('Banana', 0.50)
    },
    'row2': {
        'col1': ('Cherry', 0.75),
        'col2': ('Date', 1.50)
    }
}

# Call the function with the new dictionary-based inputs
product_catalog = build_catalogue(product_code_grid, product_data_grid)

# Display the resulting product catalog
print(product_catalog)

# Expected Output:
# {
#     'P1001': ('Apple', 1.2),
#     'P1002': ('Banana', 0.5),
#     'P1003': ('Cherry', 0.75),
#     'P1004': ('Date', 1.5)
# }
