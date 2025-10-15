import os
import requests
from bs4 import BeautifulSoup
from email_account import EmailAccount

EMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

# gets the current price for the product at the specified URL
def get_price_for_product(url):
    response = requests.get(url)
    #print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML element that contains the price
    price = soup.find(class_="a-offscreen").get_text()

    # Remove the dollar sign using split
    price_without_currency = price.split("$")[1]

    # Convert to floating point number
    price_as_float = float(price_without_currency)
    print(price_as_float)
    return price_as_float

# create a [ { "product_name", "product_url", "target_price" } ] that we want to monitor
products_to_monitor = [
    {
        "product_name": "Instant Pot",
        "product_url": "https://appbrewery.github.io/instant_pot/",
        "target_price": 100.00
    }
]

# create an empty list of products that met the target price
# create a [ { "product_name", "product_url", "target_price", "actual_price" } ] that we want to monitor
matching_products = []

# loop through all the products, adding the ones that met target_price to matching_products
for product in products_to_monitor:
    # get the price of the current product
    actual_price = get_price_for_product(product['product_url'])

    # if the actual_price is lower than the target_price, add the item to matching_products
    if actual_price <= product['target_price']:
        # TODO make a deep copy of product
        tmp_product = product
        tmp_product['actual_price'] = actual_price
        matching_products.append(tmp_product)

# if one or more products in our list fell at or below their target prices, then send an email to the user
if len(matching_products) > 0:
    # create an EmailAccount object
    email = EmailAccount(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # craft the contents of the email
    to = "earthmabus@hotmail.com"
    subject = f"{len(matching_products)} products met your target prices!"
    message = f"Here are the {len(matching_products)} products that met your pricing targets\n"
    for product in matching_products:
        message += f"- '{product['product_name']}' is currently ${product['actual_price']} (your target = ${product['target_price']})\n"

    # send an email to the user
    email.send_email(to, subject, message)

