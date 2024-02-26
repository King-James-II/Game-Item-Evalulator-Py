import xml.etree.ElementTree as ET
import os

# Define a class for video game items
class Item:
    def __init__(self, name, category, value):
        self.name = name
        self.category = category
        self.value = value

# Function to parse XML data and create Item objects
def parse_xml(filename):
    if not os.path.exists(filename):
        print("XML file not found. Creating a new one...")
        with open(filename, 'w') as f:
            f.write('<items></items>')
    items = []
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        name = child.find('name').text
        category = child.find('category').text
        value = int(child.find('value').text)
        item = Item(name, category, value)
        items.append(item)
    return items

# Function to display information about items
def display_items(items):
    print("Items in the game:")
    for item in items:
        print(f"Name: {item.name}, Category: {item.category}, Value: {item.value}")

# Function to find the most valuable item based on value
def find_most_valuable_item(items):
    most_valuable = None
    max_value = 0
    for item in items:
        if item.value > max_value:
            most_valuable = item
            max_value = item.value
    return most_valuable

# Function to calculate the average value of items
def calculate_average_value(items):
    total_value = 0
    for item in items:
        total_value += item.value
    return total_value / len(items)

# Main program entry point
if __name__ == "__main__":
    # Parse XML data and create Item objects
    items = parse_xml("items.xml")

    # Display information about items
    display_items(items)

    # Find the most valuable item
    most_valuable = find_most_valuable_item(items)
    if most_valuable:
        print(f"The most valuable item is {most_valuable.name} with a value of {most_valuable.value}.")

    # Calculate the average value of items
    average_value = calculate_average_value(items)
    print(f"The average value of items is {average_value}.")
