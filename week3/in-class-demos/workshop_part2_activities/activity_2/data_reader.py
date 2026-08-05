# Remember you file paths when you attempt use this file reader
# import the reuseable csv library - docs at: https://docs.python.org/3/library/csv.html
import csv

# Function to read data from CSV file
def read_sales_data(filename):
    # Read data from CSV file
    sales_data =[]

    with open (filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Units Sold"] = int(row['Units Sold'])
            row["Units Price"] = float(row['Unit Price'])
            row["Total Revenue"] = float(row['Total Revenue'])
            sales_data.append(row)
    
    return sales_data

sales_data = read_sales_data('./sales_data.csv')

# Calculate total revenue for each product
product_revenue = {}
for sale in sales_data:
    product = sale['Product']
    revenue = sale['Total Revenue']
    product_revenue[product] = product_revenue.get(product, revenue)
    product_revenue = dict(sorted(product_revenue.items(), key=lambda item: item[1], reverse=True))
    
# TODO: Identify the product with the highest total units sold
max_units_sold_product = {'Product' : 0}
for sale in sales_data:
    product = sale['Product']
    sale_units = sale['Units Sold']
    if sale_units > list(max_units_sold_product.values())[0]:
        max_units_sold_product = {product : sale_units}
    elif sale_units == list(max_units_sold_product.values())[0]:
        max_units_sold_product[product] = sale_units

# TODO: Calculate average unit price for each product - watch out for division by zero
product_unit_price = {}
# sort the product data into a dictionary
for sale in sales_data:
    product = sale['Product']
    unit_price = sale['Unit Price']
    if product not in product_unit_price:
        product_unit_price[product] = [float(unit_price)]
    elif product in product_unit_price:
        product_unit_price[product].append(float(unit_price))
print(product_unit_price)
# Average the values
for product in product_unit_price:
    num_of_values = len(product_unit_price[product])
    sum_of_values = sum(product_unit_price[product])
    average_price = sum_of_values / num_of_values
    product_unit_price[product] = average_price

# Display results
print("Total revenue for each product:")
for product, revenue in product_revenue.items():
    print(f"{product}: ${revenue:.2f}")

print("\nThe product/s with the highest total units sold:")
for key, value in max_units_sold_product.items():
    print(f"{key}: {value}")

print("\nAverage unit price for each product:")
for product, avg_price in product_unit_price.items():
    print(f"{product}: ${avg_price:.2f}")