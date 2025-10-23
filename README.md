# python-beautifulsoup-amazon-price-notifier

This application checks the price of a list of products on Amazon and sends out an email to the user if the price for one or more of the products is below a certain user defined price point.

The application works by:
* Being given a set of product pages and price points from a user
* Scrapes the product page for each product using beautifulsoup
* Sends out an email, using smtp, to the user if one or more of the products have met the user defined price points

Upgrades
* Expand to support the product lists of multiple users
* Track the prices of all the products (from all the user product lists) in a database OR rely on https://www.camelcamelcamel.com for this information
* Provide an intuitive web interface that allows users to specify the aforementioned
* Send text messages instead of emails
* Perform analytics on the user base to see what people are interested in
