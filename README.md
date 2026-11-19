# Inventory Management System

A command-line inventory management system for a hardware store. It was my final project for the Programming 1 course at UTN (Universidad Tecnológica Nacional).

## What it does

- Load tools and their initial stock quantities
- Display the full inventory
- Search for a tool and check its available stock
- Generate a report of out-of-stock products
- Add new products to the inventory
- Update stock by registering sales or new deliveries
- Validate user input and prevent invalid stock operations

## Built with

Python 3

## My part

I wrote the program, splitting the main menu and the inventory functions into separate files. I implemented the stock operations, product search and input validation, with error handling to prevent invalid data and insufficient-stock sales.

The inventory is stored in a list of dictionaries while the program is running.

## Run it locally

```bash
git clone https://github.com/lucianacalisaya/inventory-management-system-utn.git

cd inventory-management-system-utn

python3 main.py
```
